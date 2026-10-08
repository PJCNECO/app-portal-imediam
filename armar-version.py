#!/usr/bin/env python3
"""Arma una copia de la app con rutas relativas, lista para servir desde una carpeta.

Uso:
    python3 armar-version.py CARPETA DIRECCION

Ejemplos:
    python3 armar-version.py app  https://imediagnostico.com/app/
    python3 armar-version.py docs https://pjcneco.github.io/app-portal-imediam/

La copia usa rutas relativas, así funciona dentro de cualquier carpeta del
sitio. "Ver estudios" lleva al portal real, y el código QR para compartir
apunta a DIRECCION. Los archivos de origen son los de la raíz del repositorio.
"""
import json, os, shutil, sys

PORTAL = "https://app.imediagnostico.com/login"
if len(sys.argv) != 3:
    sys.exit(__doc__)
dest, direccion = sys.argv[1].rstrip("/"), sys.argv[2]
if not direccion.endswith("/"):
    direccion += "/"

os.makedirs(dest, exist_ok=True)
for carpeta in ("icons", "img"):
    shutil.rmtree(os.path.join(dest, carpeta), ignore_errors=True)
    shutil.copytree(carpeta, os.path.join(dest, carpeta))
shutil.copy("sw.js", os.path.join(dest, "sw.js"))

html = open("inicio.html", encoding="utf-8").read()
html = (html.replace('href="/login"', 'href="%s"' % PORTAL)
            .replace('"/manifest.webmanifest"', '"manifest.webmanifest"')
            .replace('"/icons/', '"icons/')
            .replace('"/img/', '"img/')
            .replace('"/qr-app.png"', '"qr-app.png"')
            .replace("'/sw.js'", "'sw.js'")
            .replace('"/instalar-app.js"', '"instalar-app.js"'))
assert '="/' not in html and "'/" not in html, "quedó alguna ruta absoluta"
open(os.path.join(dest, "index.html"), "w", encoding="utf-8").write(html)

js = open("instalar-app.js", encoding="utf-8").read().replace("'/icons/", "'icons/")
open(os.path.join(dest, "instalar-app.js"), "w", encoding="utf-8").write(js)

m = json.load(open("manifest.webmanifest", encoding="utf-8"))
m["start_url"], m["scope"], m["id"] = "./", "./", "./"
for i in m["icons"]:
    i["src"] = i["src"].lstrip("/")
m["shortcuts"] = [{"name": "Pedir un turno", "url": "./#turno"}, {"name": "Servicios", "url": "./#servicios"}]
json.dump(m, open(os.path.join(dest, "manifest.webmanifest"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

try:
    import qrcode
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=3)
    q.add_data(direccion); q.make(fit=True)
    q.make_image(fill_color="black", back_color="white").save(os.path.join(dest, "qr-app.png"))
except ImportError:
    print("Falta el módulo qrcode (pip install qrcode): no se generó qr-app.png")
print("%s/ listo para %s" % (dest, direccion))

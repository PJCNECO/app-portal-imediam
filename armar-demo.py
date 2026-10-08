#!/usr/bin/env python3
"""Arma en docs/ una copia de prueba de la app para publicarla con GitHub Pages.

La copia usa rutas relativas (GitHub Pages la sirve en una subcarpeta) y el
botón "Ver estudios" lleva al portal real. Los archivos para el portal son los
de la raíz del repositorio; docs/ se genera a partir de ellos con:

    python3 armar-demo.py
"""
import json, os, shutil

PORTAL = "https://app.imediagnostico.com/login"
os.makedirs("docs", exist_ok=True)
shutil.rmtree("docs/icons", ignore_errors=True)
shutil.copytree("icons", "docs/icons")
shutil.rmtree("docs/img", ignore_errors=True)
shutil.copytree("img", "docs/img")
shutil.copy("sw.js", "docs/sw.js")

# El código QR de la copia de prueba lleva a la dirección de GitHub Pages.
DEMO = "https://pjcneco.github.io/app-portal-imediam/"
try:
    import qrcode
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=3)
    q.add_data(DEMO); q.make(fit=True)
    q.make_image(fill_color="black", back_color="white").save("docs/qr-app.png")
except ImportError:
    print("Falta el módulo qrcode (pip install qrcode): no se regeneró docs/qr-app.png")

html = open("inicio.html", encoding="utf-8").read()
html = (html.replace('href="/login"', 'href="%s"' % PORTAL)
            .replace('"/manifest.webmanifest"', '"manifest.webmanifest"')
            .replace('"/icons/', '"icons/')
            .replace('"/img/', '"img/')
            .replace('"/qr-app.png"', '"qr-app.png"')
            .replace("'/sw.js'", "'sw.js'")
            .replace('"/instalar-app.js"', '"instalar-app.js"'))
assert '="/' not in html and "'/" not in html, "quedó alguna ruta absoluta"
open("docs/index.html", "w", encoding="utf-8").write(html)

js = open("instalar-app.js", encoding="utf-8").read().replace("'/icons/", "'icons/")
open("docs/instalar-app.js", "w", encoding="utf-8").write(js)

m = json.load(open("manifest.webmanifest", encoding="utf-8"))
m["start_url"], m["scope"] = "./", "./"
for i in m["icons"]:
    i["src"] = i["src"].lstrip("/")
m["shortcuts"] = [{"name": "Pedir un turno", "url": "./#turno"}, {"name": "Servicios", "url": "./#servicios"}]
json.dump(m, open("docs/manifest.webmanifest", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
open("docs/.nojekyll", "w").close()
print("docs/ listo")

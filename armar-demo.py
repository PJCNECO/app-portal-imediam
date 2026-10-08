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
shutil.copy("sw.js", "docs/sw.js")

html = open("inicio.html", encoding="utf-8").read()
html = (html.replace('href="/login"', 'href="%s"' % PORTAL)
            .replace('"/manifest.webmanifest"', '"manifest.webmanifest"')
            .replace('"/icons/', '"icons/')
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

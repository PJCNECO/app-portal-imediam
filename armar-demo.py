#!/usr/bin/env python3
"""Arma en docs/ la copia de prueba que publica GitHub Pages (ver armar-version.py)."""
import subprocess, sys
subprocess.run([sys.executable, "armar-version.py", "docs", "https://pjcneco.github.io/app-portal-imediam/"], check=True)
open("docs/.nojekyll", "w").close()

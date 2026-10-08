# App de IMEDIAM (PWA) - instalación

Con estos archivos, https://app.imediagnostico.com se puede instalar en el
celular como una app: ícono en la pantalla de inicio y pantalla completa.
No pasa por App Store ni Google Play.

Al abrirla aparece una pantalla de inicio (`inicio.html`) con estas opciones:

- **Ver estudios:** lleva al login del portal.
- **Pedir un turno:** se elige el estudio y se abre WhatsApp con el mensaje armado.
- **Hacer una consulta:** por WhatsApp o por mail.
- **Servicios:** los estudios que hace IMEDIAM, con su foto y su descripción.
- **Compartir la app:** botón de compartir del celular, envío por WhatsApp,
  copiar el enlace y un código QR.

La pantalla de inicio es una sola página, sin base de datos ni formularios que
guarden nada: los turnos y las consultas se mandan por WhatsApp
(2262 22-1071), teléfono (2262 65-4706) o mail (turnos@imediagnostico.com).

## Copia de prueba (carpeta `docs/`)

La carpeta `docs/` es una copia de la app para probarla en el celular antes de
instalarla en el portal, publicada con GitHub Pages. Es igual a la definitiva,
salvo que "Ver estudios" abre el portal en el navegador. No hay que subirla al
portal. Se vuelve a generar con `python3 armar-demo.py`.

## Para quien administra el portal

### 1. Subir archivos a la raíz de app.imediagnostico.com

- `manifest.webmanifest`  ->  https://app.imediagnostico.com/manifest.webmanifest
- `sw.js`                 ->  https://app.imediagnostico.com/sw.js
- `inicio.html`           ->  https://app.imediagnostico.com/inicio.html
- `instalar-app.js`       ->  https://app.imediagnostico.com/instalar-app.js
- carpeta `icons/`        ->  https://app.imediagnostico.com/icons/...
- carpeta `img/`          ->  https://app.imediagnostico.com/img/...   (fotos de los estudios)
- `qr-app.png`            ->  https://app.imediagnostico.com/qr-app.png  (código QR para compartir la app)

`sw.js` tiene que quedar en la raíz (no en una subcarpeta) y servirse por HTTPS.
El servidor tiene que entregar `manifest.webmanifest` como
`application/manifest+json` (o `application/json`).

### 2. Pegar el contenido de `snippet-head.html`

Las etiquetas van dentro del `<head>` y los `<script>` antes de `</body>`,
como mínimo en la página /login.

El último `<script>` (instalar-app.js) es opcional: muestra en el login un
cartel "Instalá la app de IMEDIAM". En Android abre la instalación con un
botón; en iPhone explica los dos pasos. No aparece si la app ya está
instalada, y si la persona lo cierra no vuelve a salir por 30 días.

### Si se prefiere que la app abra directo en el login

En `manifest.webmanifest`, cambiar `"start_url": "/inicio.html"` por
`"start_url": "/login"`. La pantalla de inicio se puede dejar igual, como
página aparte.

### Para cambiar los servicios, teléfonos o textos

Todo está en `inicio.html`: cada estudio es un bloque `<details class="serv">`
y el número de WhatsApp está al principio del `<script>` (`var WA`).

### 3. Íconos

Los de la carpeta `icons/` ya son los definitivos: el globo del logo de
IMEDIAM sobre fondo blanco. Si algún día cambia el logo, hay que reemplazarlos
con los mismos nombres y tamaños:

- icon-192.png            192x192
- icon-512.png            512x512
- icon-maskable-512.png   512x512, logo centrado ocupando ~60% (bordes libres)
- apple-touch-icon.png    180x180, fondo sólido (sin transparencia)

El color `#0061af` (en el manifest, el snippet y instalar-app.js) se puede
cambiar por el de la marca.

### 4. Probar

- Android (Chrome): abrir el portal -> tres puntos -> "Instalar app".
- iPhone (Safari): abrir el portal -> Compartir -> "Agregar a inicio".
- En PC: Chrome -> F12 -> Application -> Manifest, para ver si hay errores.

La app no guarda nada en el teléfono: siempre pide todo al servidor, así que
no quedan datos de pacientes almacenados y necesita conexión.

## Mensaje para los colegas (para copiar en WhatsApp o mail)

Ya podés tener el portal de IMEDIAM como una app en tu celular, para ver los
estudios de tus pacientes:

*Android:* abrí https://app.imediagnostico.com/login en Chrome, tocá los tres
puntos de arriba a la derecha y elegí "Instalar app".

*iPhone:* abrí https://app.imediagnostico.com/login en Safari, tocá el botón
Compartir (el cuadrado con la flecha) y elegí "Agregar a inicio".

Te queda el ícono de IMEDIAM junto a tus otras apps. Entrás con tu usuario y
clave de siempre.

## Código QR

`qr-portal-imediam.png` lleva a https://app.imediagnostico.com/login. Sirve
para un cartel en recepción, la firma del mail o la hoja del informe.

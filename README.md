# App de IMEDIAM (PWA) - instalación

Con estos archivos, el portal https://app.imediagnostico.com se puede instalar
en el celular como una app: ícono en la pantalla de inicio y pantalla completa.
No pasa por App Store ni Google Play.

## Para quien administra el portal

### 1. Subir archivos a la raíz de app.imediagnostico.com

- `manifest.webmanifest`  ->  https://app.imediagnostico.com/manifest.webmanifest
- `sw.js`                 ->  https://app.imediagnostico.com/sw.js
- `instalar-app.js`       ->  https://app.imediagnostico.com/instalar-app.js  (opcional)
- carpeta `icons/`        ->  https://app.imediagnostico.com/icons/...

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

### 3. Íconos

Los de la carpeta `icons/` ya son los definitivos: el globo del logo de
IMEDIAM sobre fondo blanco. Si algún día cambia el logo, hay que reemplazarlos
con los mismos nombres y tamaños:

- icon-192.png            192x192
- icon-512.png            512x512
- icon-maskable-512.png   512x512, logo centrado ocupando ~60% (bordes libres)
- apple-touch-icon.png    180x180, fondo sólido (sin transparencia)

El color `#0b5cab` (en el manifest, el snippet y instalar-app.js) se puede
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

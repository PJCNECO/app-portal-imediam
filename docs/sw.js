// Service worker minimo de IMEDIAM.
// A proposito NO guarda nada en cache: el portal maneja datos de pacientes
// y siempre debe pedir todo al servidor.
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (event) => event.waitUntil(self.clients.claim()));
self.addEventListener('fetch', () => {
  // Sin respondWith: el navegador resuelve cada pedido normalmente por red.
});

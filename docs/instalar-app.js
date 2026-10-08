// Cartel "Instalar la app de IMEDIAM" para la pagina de login.
// - Android / Chrome / Edge: muestra un boton que abre la instalacion del navegador.
// - iPhone / iPad (Safari): muestra los dos pasos, porque Apple no permite instalar con un boton.
// - No aparece si la app ya esta instalada, ni por 30 dias si la persona lo cierra.
(function () {
  var CLAVE = 'imediam-instalar-cerrado';
  var instalada = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
  if (instalada) return;
  try {
    var cerrado = +localStorage.getItem(CLAVE) || 0;
    if (Date.now() - cerrado < 30 * 24 * 3600 * 1000) return;
  } catch (e) {}

  var ua = navigator.userAgent;
  var esIOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var esSafari = /Safari/.test(ua) && !/CriOS|FxiOS|EdgiOS/.test(ua);
  var pedido = null;

  function mostrar(texto, boton) {
    if (document.getElementById('imediam-instalar')) return;
    var caja = document.createElement('div');
    caja.id = 'imediam-instalar';
    caja.setAttribute('role', 'region');
    caja.setAttribute('aria-label', 'Instalar la app de IMEDIAM');
    caja.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:99999;max-width:460px;margin:0 auto;' +
      'background:#fff;color:#13232d;border:1px solid #c9d6dd;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.18);' +
      'padding:14px 14px 12px;font:15px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif;display:flex;gap:12px;align-items:flex-start';
    var icono = document.createElement('img');
    icono.src = 'icons/icon-192.png'; icono.alt = ''; icono.width = 44; icono.height = 44;
    icono.style.cssText = 'border-radius:10px;flex:none';
    var cuerpo = document.createElement('div');
    cuerpo.style.cssText = 'flex:1;min-width:0';
    var titulo = document.createElement('strong');
    titulo.textContent = 'Instal\u00e1 la app de IMEDIAM';
    titulo.style.cssText = 'display:block;margin-bottom:2px';
    var detalle = document.createElement('div');
    detalle.textContent = texto;
    detalle.style.cssText = 'color:#4e626e;font-size:14px';
    cuerpo.appendChild(titulo); cuerpo.appendChild(detalle);
    if (boton) {
      var b = document.createElement('button');
      b.type = 'button'; b.textContent = 'Instalar';
      b.style.cssText = 'margin-top:10px;border:0;border-radius:8px;padding:9px 18px;background:#0061af;color:#fff;font:600 15px/1 inherit;cursor:pointer';
      b.onclick = boton;
      cuerpo.appendChild(b);
    }
    var cerrar = document.createElement('button');
    cerrar.type = 'button'; cerrar.textContent = '\u00d7'; cerrar.setAttribute('aria-label', 'Cerrar');
    cerrar.style.cssText = 'border:0;background:none;font-size:24px;line-height:1;color:#4e626e;cursor:pointer;padding:0 4px;flex:none';
    cerrar.onclick = function () { try { localStorage.setItem(CLAVE, Date.now()); } catch (e) {} caja.remove(); };
    caja.appendChild(icono); caja.appendChild(cuerpo); caja.appendChild(cerrar);
    document.body.appendChild(caja);
  }

  // Android, Chrome y Edge avisan cuando la pagina se puede instalar.
  window.addEventListener('beforeinstallprompt', function (ev) {
    ev.preventDefault();
    pedido = ev;
    mostrar('Queda en tu pantalla de inicio y abre el portal a pantalla completa.', function () {
      pedido.prompt();
      pedido.userChoice.then(function () { var c = document.getElementById('imediam-instalar'); if (c) c.remove(); });
    });
  });
  window.addEventListener('appinstalled', function () { var c = document.getElementById('imediam-instalar'); if (c) c.remove(); });

  // En iPhone no hay aviso: se explican los pasos.
  if (esIOS) {
    window.addEventListener('load', function () {
      mostrar(esSafari ? 'Toc\u00e1 el bot\u00f3n Compartir (el cuadrado con la flecha) y eleg\u00ed "Agregar a inicio".'
        : 'Abr\u00ed esta p\u00e1gina en Safari, toc\u00e1 Compartir y eleg\u00ed "Agregar a inicio".');
    });
  }
})();

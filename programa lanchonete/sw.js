self.addEventListener('install', event => {
  event.waitUntil(
    caches.open('tuta-cache-v1').then(cache => {
      return cache.addAll([
        '/',
        '/index.html',
        '/login.html',
        '/inicio.html',
        '/main.css',
        '/img/icon-192.png',
        '/img/icon-512.png'
        // Adicione outros arquivos importantes aqui
      ]);
    })
  );
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});
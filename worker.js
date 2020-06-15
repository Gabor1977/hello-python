addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  // Make the headers mutable by re-constructing the Request.
  request = new Request(request)
  request.headers.get('CF-Connecting-IP')
  request.headers.get('cf-ipcountry')

  return await fetch(request)
}

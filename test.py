import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

def hello():
    return "Hello from Python!"
    print(request.headers)

import requests
headers={'X-Forwarded-For':'1.1.1.1'}
r = requests.get('http://hello.dmontest.ee/', headers=headers)
if r.ok:
    print('Success.')

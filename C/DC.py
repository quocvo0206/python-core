import requests

url = 'https://widget.1688.com/front/ajax/bridge.html?target=brg-04851'
r = requests.get(url)
print(r.cookies['__mbox_csrf_token'])

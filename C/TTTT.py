import requests

url1 = 'https://widget.1688.com/front/ajax/bridge.html?target=brg-04851'
r = requests.get(url1)
print(r.cookies['__mbox_csrf_token'])
cookiess = r.cookies['__mbox_csrf_token']

url = 'https://widget.1688.com/front/ajax/getJsonComponent.json'
headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'content-length': '455',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'SameSite=none; SameSite=none; cna=p5UsF1UU/iUCAXRiNkdf1I2+; cookie2=14794391c6faa59028f2ce0ff87bbc9a; t=a5c24727f91af2a74ffd512c8f2bc00b; _tb_token_=50e78ba367f35; __cn_logon__=false; alicnweb=touch_tb_at%3D1588698114039; isg=BNjYd-rAMgrRyx6P5WGvcmkNqQ9qwTxLmkYsNRLJJJPGrXiXutEM2-6P5f2dpvQj; l=eBTyvP04QkaT8jGtBOfaFurza77OSIRYYuPzaNbMiT5POI5B5fXlWZbjY-Y6C3MNh6mHR3zsQJDBBeYBY3xonxvOCgpMGIMmn; __mbox_csrf_token='+cookiess,
    'origin': 'https://widget.1688.com',
    'referer': 'https://widget.1688.com/front/ajax/bridge.html?target=brg-04851',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

body = {
    'namespace': 'getCateMarketSN',
    'widgetId': 'getCateMarketSN',
    'methodName': 'execute',
    'params': '{"sceneId":"2181"}',
    'sceneId': 2181,
    '__mbox_csrf_token': cookiess
}

r = requests.post(url, data=body, headers=headers)
print(r)


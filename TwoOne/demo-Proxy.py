from urllib import request
url = 'http://www.httpbin.org/ip'

handler = request.ProxyHandler({'http':'211.101.154.105:43598'})

opener = request.build_opener(handler)

resp = opener.open(url)

print(resp.read())
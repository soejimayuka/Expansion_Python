# A example of `urllib.request`.
import urllib.request

url = "http://www.yoheim.net"
with urllib.request.urlopen(url) as res:
  html = res.read().decode('utf-8')

response = urllib.request.urlopen('http://www.yoheim.net')
print('url:', response.geturl())
print('Content-Type:', response.info()['Content-Type'])
print('code:', response.getcode())

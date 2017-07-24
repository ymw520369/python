import requests
import xxtea
import six
import httplib2

url = "http://192.168.199.247:8081/"

data = """{
  "accountId": 101,
  "roleName":"你的名字",
  "token":"game-token"
  }
"""

resp = requests.post("http://192.168.199.247:8082/enter/create", json=data)
print(resp.content)


# [-25, -28, 55, -83, 108, -128, 72, 68, 122, 52, -31, -6, 25, -68, -21, -1]
# [-84, 2, 90, -22, -74, 71, 1, -51, 40, -23, -74, 88, -84, -110, -48, -122, 121, 66, 94, 48]

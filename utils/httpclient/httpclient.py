import requests

url = "http://localhost:8081/center"

data = """{
  "serverId": 101,
  "serverName":"logic 3"
  }
"""
# param = {"serverId": 101, "serverName": "logic 3"}
param = {"token": "token0000101", "uuid": "100sa0s0"}
resp = requests.post("http://localhost:8081/center/vertify/credential", data=param)
print(resp.content)



# [-25, -28, 55, -83, 108, -128, 72, 68, 122, 52, -31, -6, 25, -68, -21, -1]
# [-84, 2, 90, -22, -74, 71, 1, -51, 40, -23, -74, 88, -84, -110, -48, -122, 121, 66, 94, 48]

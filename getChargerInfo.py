import requests

url = 'http://apis.data.go.kr/B552584/EvCharger/getChargerStatus'
params ={'serviceKey' : 'service key in here is hide because this repository is public', 'pageNo' : '1', 'numOfRows' : '10', 'period' : '5', 'zcode' : '11' }

response = requests.get(url, params=params)
print(response.content)
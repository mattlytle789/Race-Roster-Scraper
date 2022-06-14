import requests

url = 'https://raceroster.com/events/2022/56070/the-2022-asics-falmouth-road-race/fundraising-organization/34911'
response = requests.get(url)
print(response.text)
import requests
APP_KEY = '2433827e55eed3691414d34cca5cee88'
IMAGE_URL = 'https://www.canceranswer.co.kr/news/photo/202007/980_1425_5550.jpg'
session = requests.Session()
session.headers.update({'Authorization': 'KakaoAK ' + APP_KEY})

response = session.post('https://cv-api.kakaobrain.com/pose', data={'image_url': IMAGE_URL})
print(response.status_code, response.json())
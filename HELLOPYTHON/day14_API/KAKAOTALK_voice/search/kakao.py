import requests
import json
import speech_recognition as sr


kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = 'd988238e09a291786f4e350d554f010c'

headers = {
    "Content-Type": "application/octet-stream",
    "X-DSS-Service": "DICTATION",
    "Authorization": "KakaoAK " + rest_api_key,
}

# 오디오 파일/ 마이크에서 음성 추출하는 객체
recognizer = sr.Recognizer()
print('voice>>');
# 마이크 설정
microphone = sr.Microphone(sample_rate=16000)

# 마이크 세팅 - 에너지 임계점 설정
with microphone as source:
    recognizer.adjust_for_ambient_noise(source)

with microphone as source:
    audio_data = recognizer.listen(source)
    audio = audio_data.get_raw_data()

res = requests.post(kakao_speech_url, headers=headers,data=audio)

print(res.text)

# result_json_string = res.text[res.text.index('{type":"finalResult"'):res.text.rindex('}')+1]
# result = json.loads(result_json_string)

# print(result)
# print(result['value'])
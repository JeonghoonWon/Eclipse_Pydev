# 홀 짝 참고해서 가위바위보 만들기
import random
com = ""
mine = input("주먹/바위/보 선택하세요")
result = ""
rnd = random.random()

if rnd < 0.33:
    com = "주먹"
elif rnd < 0.66:
    com = "가위"
else :
    com = "보"

if com == mine:
    result = "비김"
elif(com=="주먹" and mine=="가위" or com=="가위" and mine=="보" or com=="보" and mine=="주먹"):
    result = "너가 짐"
elif(com=="주먹" and mine=="보" or com=="가위" and mine=="주먹" or com=="보" and mine=="가위"):
    result = "너가 이김"

print("나 :", mine)
print("컴 :", com)
print(result)

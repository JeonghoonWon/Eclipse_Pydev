import random
com = ""
mine = input("홀/짝을 선택하세요.")
result = ""
rnd = random.random() 

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == mine :
    result = "승리"
else :
    result = "패배"

print("컴 : ", com)
print("나 : ",mine)
print("결과 :",result)
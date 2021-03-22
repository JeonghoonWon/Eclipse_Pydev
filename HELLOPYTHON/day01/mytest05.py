# input("단수를 넣으세요:) 
# 2단을 출력

a= int(input("단수를 넣으세요."))
print("a :",a) 
for i in range(1,10):
    result = a*i
    print(result)

print("===================================")

dan = input("단수를 넣으세요.")

print(dan+"*1="+str(int(dan)*1))
print(dan+"*2="+str(int(dan)*2))
print(dan+"*3="+str(int(dan)*3))
print(dan+"*4="+str(int(dan)*4))
print(dan+"*5="+str(int(dan)*5))
print(dan+"*6="+str(int(dan)*6))
print(dan+"*7="+str(int(dan)*7))
print(dan+"*8="+str(int(dan)*8))
print(dan+"*9="+str(int(dan)*9))
print("===================================")
#요즘엔 주석을 많이 달지 않는다. 메서드명으로 정확히 알 수 있도록 짜는게 좋은게 아닐까?

for i in range(1,10):
    print(dan+"*"+str(i)+"="+str(int(dan)*i))
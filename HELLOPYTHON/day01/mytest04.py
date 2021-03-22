#input("시작수를 넣으세요" ) 단 작은수
# input("끝수를 넣으세요") 
# a에서 b까지 합을 구하시오.
sum = 0
a = input("시작수를 넣으세요.")

b = input("끝수를 넣으세요.")

print("시작수",a)
print("끝수",b)


for i in range(int(a),int(b)+1):
    sum += i

print("a~b의 합 :",sum)
    
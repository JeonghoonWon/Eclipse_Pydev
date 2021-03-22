# 1~ 1000 까지의 3의 배수의 합
sum = 0
for i in range(1001):
    if(i%3==0):
        sum += i

print(sum)
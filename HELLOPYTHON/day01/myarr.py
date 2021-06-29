a = []
a.append("1")
a.append("2")
a.insert(len(a), "3")   #a.insert(index, object) ==> index : 배열의 위치 / object : 입력값

print(len(a))

print(a)





lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol[0])
print(lol[2][1])
for sub in lol:
    for item in sub:
       print(item, end=" ")
    print()
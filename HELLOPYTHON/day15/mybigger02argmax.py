a = [0,0,1,0,0,
     0,0,0,0,0]
max = -1
for i in a:
    if max < i:
        max = i
        
for i,item in enumerate(a):
    if max == item:
        print(i)    
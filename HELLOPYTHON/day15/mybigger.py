import numpy as np

a = [0,0,1,0,0,
     0,0,0,0,0]

a_n = np.array(a)

#argmax : 배열 중 가장 큰 값을 불러오는 함수
# keras에서 argmax 를 많이 사용한다. predict 되는 수가 큰 수 이기 때문에
pred = np.argmax(a_n)

print(pred)    
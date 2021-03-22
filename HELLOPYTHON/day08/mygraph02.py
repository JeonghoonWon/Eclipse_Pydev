import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )

mycursor = mydb.cursor()

sql1 = "select s_price from stock where s_name = 'LG'"

mycursor.execute(sql1)

result = mycursor.fetchall()

print(result)

from matplotlib import pyplot as plt

import numpy as np                                           # numpy 호출
import matplotlib.pyplot as plt                              # pyplot 호출


plt.figure(figsize=(5, 5), dpi=100)           # figsize = 그래프 크기, dpi = dot per inch
plt.subplot(1, 1, 1)

x = np.linspace(-np.pi, np.pi, 300, endpoint=True)       # 삼각함수에 입력될 x값 생성(배열)
y, z = np.cos(x), np.sin(x)                              # 삼각함수 계산 y=cos(x), z=sin(x)

plt.plot(x, y, color="red", linewidth=2.0, linestyle="-")   #plot에 x,y 입력
plt.plot(x, z, color="blue", linewidth=2.0, linestyle="--")  #plot에 x,z 입력

plt.xlim(-5.0, 5.0)                                          # plot의 x축 최대값 설정
plt.ylim(-1.5, 1.5)                                          # plot의 y축 최대값 설정

plt.xticks(np.linspace(-5, 5, 9, endpoint=True))             # x축값 표시방식 설정
plt.yticks(np.linspace(-1.5, 1.5, 5, endpoint=True))         # y축값 표시방식 설정

plt.show()                                                   # 그래프 출력
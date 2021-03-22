# 총 출력할 주식 수
import re
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
totalStocks = 15

# db 연결
db = pymysql.connect(host='localhost', user = 'root', db='_stock_old', password='python')

# db와 상호작용하기위해 cursor 설정을 해줘야 함.
#DictCursor가 아닌 일반 cursor를 사용하면 결과가 일반적으로는 튜플 형태로 리턴됨
curs  = db.cursor()

# stock이름 가져오기. 배열생성
stock = []

sql = '''
SELECT  COLUMN_NAME
FROM    INFORMATION_SCHEMA.COLUMNS
WHERE   TABLE_NAME = 'stock_sync_0121'
AND COLUMN_NAME != 'in_time'
      ''';
      
#cursor 는 sql문과 필수로 붙어있어야 함.
curs.execute(sql)

# 데이타 Fetch
rows = curs.fetchall()
# rows = 전체 행
# rows[0] : 첫번째 row
# rows[1] : 두번째 row

#출력할 stock 수를 세기 위해서 cnt 잡아둔다. 
cnt = 0

for stockname in rows :
    stock.append(str(stockname)[2:-3])
    print(stockname)
    cnt += 1
    if(cnt == totalStocks):
        break;
    
# 정보 받아온 횟수 totalNum에 기록 time 배열 만들기
sql = "select count(*) from stock_sync_0121" 

curs.execute(sql)
rows = curs.fetchall()
for i in range(len(rows)):
    # re.findall 
    totalNum = int(re.findall('\d+',str(rows[i]))[0])
time = range(0,totalNum)

# stock 코드에 맞는 종목 검색해 가격변화 priceArr 배열에 기록하기.
priceArr = []

for i in range(len(stock)):
    sql = "select {}, in_time from stock_sync_0121 order by in_time".format(stock[i]);
    curs.execute(sql)
    rows = curs.fetchall()

    arr = []
    firstPrice = int(re.findall('\d+',str(rows[0]))[0])
    for i in range(len(rows)):
        price = int(re.findall('\d+',str(rows[i]))[0])
        priceGap = price - firstPrice
        priceGapPercent = priceGap/firstPrice * 100
        arr.append(priceGapPercent)
    priceArr.append(arr)      

fig = plt.figure()
ax = fig.gca(projection='3d')

#x 축은 0,1,2,... 고정
x = []
for i in range(len(stock)):
    x.append(np.zeros(len(time),dtype=int)+i)

# y축은 시간, z축은 가격

# 그래프 그려주기
for i in range(len(stock)):
    ax.plot(x[i],time,priceArr[i], label=stock[i])
ax.legend()

plt.show()

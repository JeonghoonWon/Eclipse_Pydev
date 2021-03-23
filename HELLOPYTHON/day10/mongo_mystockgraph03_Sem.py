import pymongo

 
def getPrices(s_name):
    # 배열 만들기
    arr = []
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.python
    stock = db.stock
    
    # sort 는 oracle 의 order by 역할
    rows = stock.find({'s_name':'삼성전자'}).sort('indate',1)
    first_price = rows[0]['s_price']
    
   # print(rows[0]['s_price'])
    
    for r in rows:
        int_s_price = int(r['s_price'])/int(first_price)
        arr.append(int_s_price)
    return arr  # 초기값으로 값들을 나누고 arr 로 나눠준다.
        
        #print(int(r['s_price'])/int(first_price)) # str 이라서 int 로 변경해준다.



if __name__ == '__main__':
    arr = getPrices('삼성전자')
    print(arr)




# row = sample.find_one()
# print(row)
# print("=================================================")
# rows = sample.find()
# for r in rows:
    # print(r)
# print("=================================================")
# for x in sample.find():
    # print(x)
    #
# print("=================================================")
#
# rows = sample.find({'col01':'1'})
# for r in rows:
    # print(r)
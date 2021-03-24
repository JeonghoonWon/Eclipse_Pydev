import pymysql

class MyEmpDao:
    def __init__(self):
        pass
        
    def getEmps(self):
        ret = []
        mydb = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "python",
        database = "python"
        )
    
        #statement
        mycursor = mydb.cursor()
        
        # 페이징 처리 가 아닌 이상 *를 사용하지 않는게 좋다. 하나씩 컬럼 적는게 좋다.
        sql = "select sabun,name,dept,mobile from emp"
        
        mycursor.execute(sql)
        
        # 실행결과를 fetchall()을 이용해 받아온다.
        rows = mycursor.fetchall()
        for e in rows:
            temp = {'sabun':e[0],'name':e[1],'dept':e[2],'mobile':e[3]}
            ret.append(temp)
        
        mydb.close()
        return ret
    def insEmp(self,sabun,name,dept,mobile):
        mydb = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "python",
            database = "python"
            )
       
        mycursor = mydb.cursor()
        sql = "insert into emp(sabun,name,dept,mobile)values(%s,%s,%s,%s)"
              
        cnt = mycursor.execute(sql,(sabun,name,dept,mobile))
        
       # print("cnt",cnt)
        
        mydb.commit()
        
        mydb.close()
        return cnt
    
    def updEmp(self,sabun,name,dept,mobile):
        mydb = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "python",
            database = "python"
            )
       
        mycursor = mydb.cursor()
        sql = "update emp set name=%s,dept=%s,mobile=%s where sabun=%s"
              
        cnt = mycursor.execute(sql,(name,dept,mobile,sabun))
        
       # print("cnt",cnt)
        
        mydb.commit()
        
        mydb.close()
        return cnt
    
    def delEmp(self,sabun):
        mydb = pymysql.connect(
            host = "localhost",
            user = "root",
            password = "python",
            database = "python"
            )
       
        mycursor = mydb.cursor()
        sql = "delete from emp where sabun=%s"
              
        cnt = mycursor.execute(sql,(sabun))
        
       # print("cnt",cnt)
        
        mydb.commit()
        
        mydb.close()
        return cnt
    

if __name__ == '__main__':
 #   list = MyEmpDao().getEmps()
 #   print(list)
    cnt = MyEmpDao().delEmp('3') #3번 sabun 데이터를 4로 변경
    print(cnt)

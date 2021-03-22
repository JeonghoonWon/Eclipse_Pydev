
import pymysql

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt


mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "python",
    database = "python"
    )
    #
mycursor = mydb.cursor()    
#
sql = "select s_price, s_name, in_date from stock where s_name = 'LG'"
#
mycursor.execute(sql)
#
rows = mycursor.fetchall()
#
#
for eachLine in rows:
    x = eachLine[0]
    y = eachLine[1]
    z = eachLine[2]
    print(x,y,z) 
    plt.plot([z],[x], label='Price ($)')




plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')          # ncol = 1
plt.legend(loc='best', ncol=2)    # ncol = 2

plt.show()


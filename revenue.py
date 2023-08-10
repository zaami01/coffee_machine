import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',
    database='COFFEE_MACHINE')
curr=zmm.cursor()
p="INSERT INTO revenue(milk,coffee,sugar,water) VALUES(%s,%s,%s,%s)"
quantity=(5000,1000,500,5000)
curr.execute(p,quantity)
zmm.commit()

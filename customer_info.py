import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',
    database='COFFEE_MACHINE')
curr=zmm.cursor()
s="INSERT INTO customer_info(customerid,username,password,points,lastorder) VALUES(%s,%s,%s,%s,%s)"
info=[(1,'zaami','zaami',0,'latte'),(2,'aarya','aarya',0,'latte'),(3,'rutu','rutu',0,'latte'),(4,'prathamesh','prathamesh',0,'latte'),(5,'janhavi','janhavi',0,'latte')]
curr.executemany(s,info)
zmm.commit()

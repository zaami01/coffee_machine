import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',
    database='COFFEE_MACHINE')
curr=zmm.cursor()
 
s="CREATE TABLE customer_info(customerid INTEGER(4), username VARCHAR(20),password VARCHAR(20), points INTEGER(4), lastorder VARCHAR(20))"
curr.execute(s)
p="CREATE TABLE quantity_info (milK INTEGER(4),coffee INTEGER(4),sugar INTEGER(3), water INTEGER(4))"
curr.execute(p)
z="CREATE TABLE menu( name varchar(20),price INTEGER(3),milk INTEGER(3),coffee INTEGER(2),sugar INTEGER(2), water INTEGER(3))"
curr.execute(z)
zmm.commit()

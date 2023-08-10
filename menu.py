import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',
    database='COFFEE_MACHINE')
curr=zmm.cursor()
s="INSERT INTO menu(item,price,milk,coffee,sugar,water) VALUES(%s,%s,%s,%s,%s,%s)"
m=[('Classic Black coffee',50,0,10,0,150),
   ('Cafe Latte',70,100,20,0,30),
   ('Cappuccino',80,80,15,0,20,),
   ('Expresso',60,0,25,0,30),
   ('Mocha',90,60,20,10,10),
   ('Iced Coffee',65,80,15,0,30),
   ('Vanilla Latte',75,90,15,0,20),
   ('Irish Coffee',100,20,15,10,20)]
curr.executemany(s,m)
zmm.commit()

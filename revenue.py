import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',
    database='COFFEE_MACHINE')
curr=zmm.cursor()
p="INSERT INTO revenue(Classicblackcoffee, cafelatte ,cappuccino ,expresso ,mocha ,IcedCoffee ,VanillaLatteIrishCoffee ,Total_revenue) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
quantity=(0,0,0,0,0,0,0,0,0)
curr.execute(p,quantity)
zmm.commit()

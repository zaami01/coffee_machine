import mysql.connector
zmm=mysql.connector.connect(
    host='localhost',
    user='root',
    password='zharana4082@gmail.com',)
curr=zmm.cursor()
curr.execute("CREATE DATABASE COFFEE_MACHINE")

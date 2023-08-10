import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='zharana4082@gmail.com',
        database='coffee_machine'
    )

def get_menu(cursor):
    cursor.execute("SELECT item_code, Item, Price FROM menu")
    menu_items = cursor.fetchall()
    return menu_items

def verify_credentials(cursor, username, password):
    sql = "SELECT * FROM customer_info WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    return result and result["password"] == password

def display_menu(menu_items):
    print("Menu:")
    for item in menu_items:
        print(f"Code: {item['item_code']}, {item['Item'].capitalize()}: Rs. {item['Price']}")

def update_material_left(cursor, chosen_item, db):
    update_material_sql = "UPDATE quantity_info SET Milk = Milk - %s, Coffee = Coffee - %s, Sugar = Sugar - %s, Water = Water - %s"
    cursor.execute(update_material_sql, (chosen_item['Milk'], chosen_item['Coffee'], chosen_item['Sugar'], chosen_item['Water']))
    db.commit()

def update_revenue(cursor, item_name, price, db):
    update_revenue_sql = f"UPDATE revenue SET {item_name.replace(' ', '').lower()} = {item_name.replace(' ', '').lower()} + 1, Total_revenue = Total_revenue + {price}"
    cursor.execute(update_revenue_sql)
    db.commit()
    

def enter_order(cursor, customer_id, menu_items,db):
    chosen_code = input("Enter the item code to order: ").strip()
    chosen_item = next((item for item in menu_items if item['item_code'] == int(chosen_code)), None)
    
    if chosen_item:
        print(f"You chose {chosen_item['Item'].capitalize()}.")
        payment = float(input(f"Please enter Rs. {chosen_item['Price']} for {chosen_item['Item'].capitalize()}: "))
        
        if payment >= chosen_item['Price']:
            change = payment - chosen_item['Price']
            print(f"Thank you! Here's your {chosen_item['Item'].capitalize()}. Your change: Rs. {change:.2f}")

            # Update last order in customer_info table
            update_last_order_sql = "UPDATE customer_info SET lastorder = %s WHERE customerid = %s"
            cursor.execute(update_last_order_sql, (chosen_item['Item'], customer_id))
            
            # Update points in customer_info table (add 10% of the order's price)
            new_points = chosen_item['Price'] * 0.1
            update_points_sql = "UPDATE customer_info SET points = points + %s WHERE customerid = %s"
            cursor.execute(update_points_sql, (new_points, customer_id))


            # Get the coffee item's ingredients from the menu table
            cursor.execute("SELECT Milk, Coffee, Sugar, Water FROM menu WHERE item_code = %s", (chosen_code,))
            ingredients = cursor.fetchone()

            # Update material left in quantity_info table
            update_material_left(cursor, ingredients, db)
            update_revenue(cursor, chosen_item['Item'], chosen_item['Price'], db)
            db.commit()
            
        else:
            print("Not enough money. Order canceled.")
    else:
        print("Item not available.")

def log_in(cursor):
    while True:
        username = input("Please enter your username: ")
        password = input("Enter your password: ")

        sql = "SELECT * FROM customer_info WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        if result and result["password"] == password:
            print("Login successful")
            return result["customerid"]
        else:
            print("Invalid username or password. Please try again or type 'exit' to go back.")

def create_account(cursor):
    while True:
        new_username = input("Enter a new username: ")
        cursor.execute("SELECT * FROM customer_info WHERE username = %s", (new_username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Sorry, this username already exists. Please enter a different username or type 'exit' to go back.")
        else:
            new_pass = input("Enter a new password:")
            cursor.execute("SELECT MAX(customerid) FROM customer_info")
            last_customer_id = cursor.fetchone()["MAX(customerid)"]

            new_userid = last_customer_id + 1
            new_points = 0
            new_lastorder = "latte"

            sql_insert = "INSERT INTO customer_info (customerid, username, password, points, lastorder) VALUES (%s, %s, %s, %s, %s)"
            data = (new_userid, new_username, new_pass, new_points, new_lastorder)
            cursor.execute(sql_insert, data)
            db.commit()

            print("Account created successfully!")
            return new_userid

def main():
    try:
        db = connect_to_database()
        cursor = db.cursor(dictionary=True)

        print("Welcome to Coffee house!")
        print("1. Log into an existing account")
        print("2. Create a new account")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            customer_id = log_in(cursor)
            if customer_id:
                menu_items = get_menu(cursor)
                display_menu(menu_items)
                enter_order(cursor, customer_id, menu_items,db)

        elif choice == "2":
            customer_id = create_account(cursor)
            if customer_id:
                menu_items = get_menu(cursor)
                display_menu(menu_items)
                enter_order(cursor, customer_id, menu_items,db)

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    main()

import mysql.connector
import os
import datetime
db = mysql.connector.connect (
    host="localhost",
    user="sqluser",
    password="password",
    database="library_management_system"
)
class pro:
    def __init__(self, product_name="", category="", unit_price=0.0, stock_level=0, supplier_id=""):
        os.system('cls')
        self.product_name = product_name
        self.category = category
        self.unit_price = unit_price
        self.stock_level = stock_level
        self.supplier_id = supplier_id
    def procuct_description(self):
        self.product_name = input("Enter the product name: ")
        self.category = input(f"which catagories of the product {self.product_name}: ")
        self.unit_price = float(input("Enter the unit price: "))
        self.stock_level = int(input("Enter Stock level: "))
        self.supplier_id = input("Enter supplier ID: ")

    def add_product(self):
        try:
            self.procuct_description()
            if self.product_name and self.stock_level > 0:
                query = '''INSERT INTO products(product_name, category , unit_price, stock_level, supplier_id) 
                values(%s,%s,%s,%s,%s)'''
                cursor = db.cursor()
                cursor.execute(query,(self.product_name,self.category,self.unit_price,self.stock_level,self.supplier_id,))
                db.commit()
                print("Product added successfully!")
            else:
                print("product not added")
        except mysql.connector.errors.DatabaseError as e:
            print(f"ERROR: {e}")
    def update_product(self):

        print("which product do you want to update")
        self.product_name = input("Enter the product name: ")
        self.unit_price = float(input("Enter the unit price: "))
        self.stock_level = int(input("Enter Stock level: "))

        cursor = db.cursor()

        cursor.execute('''UPDATE products set unit_price = %s, stock_level = stock_level + %s where product_name =  %s '''
                       , (self.unit_price, self.stock_level, self.product_name))
        db.commit()
        os.system('cls')

        print("products are updated successfully!")

    def delete_product(self):
        self.product_name = input("Enter you want to delete the product name: ")

        if self.product_name:
            query = '''delete from products where product_name = %s'''
            cursor = db.cursor()
            cursor.execute(query,(self.product_name,))
            db.commit()
            os.system('cls')
            print(f"product {self.product_name} are successfully deleted")

        else:
            print("somethings went wrong")

    def out(self):
        cursor = db.cursor()
        cursor.execute("select product_name , unit_price  from products where stock_level > 0")
        result = cursor.fetchall()

        print("AVAILABLE PRODUCTS\t\t\tunit price")
        for i in result:
            print(f"{i[0]}\t\t\t\t\t{i[1]}")


class supp:
    def __init__(self):
        print("===================================SUPPLIER REGISTRATION FORM===========================================")
        self.supplier_id = input("Enter supplier ID: ")
        self.supplier_name = input("Enter supplier name: ")
        self.address = input("Enter your address: ")
        self.phone = input("Enter phone number (+251): ")
        self.email = input("Enter your email: ")

    def registration(self):
        try:
            os.system("cls")
            cursor = db.cursor()
            query = "INSERT INTO suppliers(supplier_id, supplier_name, address, phone, email) VALUES (%s,%s,%s,%s,%s)"
            value = (self.supplier_id, self.supplier_name, self.address, '+251'+ self.phone, self.email)
            cursor.execute(query,value)
            db.commit()
            os.system('cls')
            print("you are successfully registered!")

        except mysql.connector.errors.IntegrityError as e:
            print(f"ERROR: {e}")


class sale:
    def __init__(self,product_name = '', quantity = 0,sale_date = '', revenue = "" ,discount = 0.0) -> None:
        self.product_name = product_name
        self.sale_date = sale_date
        self.quantity = quantity
        self.revenue = revenue
        self.discount = discount

    def sold_product_info(self):
        try:
            self.product_name = input("What product would you like to buy: ")
            self.quantity = int(input("What quantity of products would you like to buy: "))
            self.sale_date = datetime.datetime.now()
            
            cursor = db.cursor()
            
            cursor.execute("SELECT unit_price FROM products WHERE product_name = %s", (self.product_name,))
            unit_price = cursor.fetchone()[0]
            
          
            if self.quantity >= 5:
                self.revenue = unit_price * self.quantity * 0.9  # 10% discount
            else:
                self.revenue = unit_price * self.quantity
            
            cursor.execute(
                "UPDATE products SET stock_level = stock_level - %s WHERE product_name = %s",
                (self.quantity, self.product_name)
            )
            
            cursor.execute(
                "SELECT stock_level FROM products WHERE product_name = %s",
                (self.product_name,)
            )
            last_stock_level = cursor.fetchone()[0]
            
            if last_stock_level < 0:
                db.rollback()
                print("Insufficient stock, transaction rolled back.")
            else:
                db.commit()
                query = '''
                    INSERT INTO sales (product_id, sale_date, quantity, revenue)
                    VALUES (
                        (SELECT product_id FROM products WHERE product_name = %s), 
                        %s, 
                        CASE 
                            WHEN %s <= (SELECT stock_level FROM products WHERE product_name = %s) 
                            THEN %s ELSE 0 
                        END, 
                        %s
                    )
                '''
                values = (self.product_name, self.sale_date, self.quantity, self.product_name, self.quantity, self.revenue)
                cursor.execute(query, values)
                db.commit()
                print("Sale record inserted successfully.")

        except mysql.connector.Error as err:
            db.rollback()
            print("Database error:", err)
        
        except TypeError as e:
            print(e)

        except ValueError:
            print("Invalid input for quantity. Please enter a valid integer.")

    def forcasting_stock_demand(self):
        day = int(input("Enter the duration in days for your forecast: "))
        self.product_name = input("Please specify the product you wish to forecast: ")
        cursor = db.cursor()

        cursor.execute('''SELECT quantity FROM sales WHERE product_id = 
                       (select product_id from products where product_name = %s) ORDER BY sale_date LIMIT %s''',(self.product_name, day))
        result = cursor.fetchall()

        total_sum = sum(r[0] for r in result)
        print(f"FORCASTED DEMAND: {total_sum / day}")

    def low_stock_and_order(self,threshold = 10):
        os.system("cls")
        cursor = db.cursor()
        cursor.execute('''select product_name ,stock_level from products where stock_level < %s''',(threshold,))
   
        for item in cursor.fetchall():
            self.product_name,self.stock_level = item
            print(f"Reordering {self.product_name}. Current stock level: {self.stock_level}.")

db.close()






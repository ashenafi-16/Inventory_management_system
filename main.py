from Inventory_management_system import pro , supp, sale ,os

def owner():
    choice = input('''0. for product supplier registaration \n1. for update product \n2. for delete product\n3. for add product\n4. for Display product Information \t''')
    prod = pro()
    
    
    if choice == '0':
        sup = supp()
        sup.registration()

    elif choice == '1':
        prod.update_product()

    elif choice == '2':
        prod.delete_product()

    elif choice == '3':
        prod.add_product()

    elif choice =='4':
        prod.out()

    else:
        print("Incorrect choice please try again")

entrance = input("1. FOR CUSTOMER \n2. FOR ADMIN \t")
os.system('cls')

if entrance == '1':
    s = sale()
    choice = input("1. for Purchase product \n2. for Forcasting\n3. for Stock alert\t")

    if choice == '1':
        os.system("cls")
        s.sold_product_info()

    elif choice == '2':
        s.forcasting_stock_demand()

    elif choice == '3':
        s.low_stock_and_order(10)
    else:
        print("somethings went wrong")


elif entrance == '2':
    admin_name = input("Enter admin name: ")
    admin_password = input("Enter admin passoword: ")

    if admin_name == 'ashenafi' and admin_password == 'fefrs':
        owner() 

    else:
        print("something wrong The admin status")


# Requirements
# Make E-commerce site with class object.
# Ask the user to login or register(if user want to register add user with name,email and password )
# if user registering define user usertype buyer or seller?
# while login if the user is buyer the add features 1. View all product, 2 Purchase product and
# 3. View all user bills or print out.
# if the user is seller make user choices: 1. Add products, 2. View all seller's product and
# 3. View all user view products bills to recieve.

import json # json is universal data type it has double quotation in both key and
# value where as single quotation in dict.

class Ecommerce:

    #  user register or login or exit option.
    def __init__(self):
        while True:
            self.user_choice = input('''
                                     Do you want Register or Login or Exit.
                                        Type here:- ''').lower()
            if self.user_choice == 'register':
                Ecommerce.new_register(self)
            elif self.user_choice == 'login':
                Ecommerce.login(self)
            elif self.user_choice == 'exit':
                break
            else:
                print('Invallid Choice')

    # new user register function and store user information(usernaem,email,password and usertype)
    def new_register(self):
        username = input('Enter your name here: ').lower()
        email = input('Enter your email address here: ').lower()
        password = input('Enter password here: ')
        usertype = input('''
                        Are you buyer or seller?
                              Type here: ''').lower()
        if usertype == 'buyer' or 'seller':
            user_data = {'username': username, 'email': email, 'password': password, 'usertype': usertype}
            user_data_json =json.dumps(user_data)
            file = open('user.db.txt','a')
            content = file.write(user_data_json + '-')
            file.close()
        else:
            print('Invalid userytpe Register again')
            Ecommerce.new_register(self)

 # -------Already register user login function--------#
    def login(self):
        userid = input('Enter username or email here: ')
        user_password = input('Enter password here: ')
        file = open('user.db.txt','r')
        content = file.read()
        login = 0
        user_data = content.split('-')
        for i in user_data:
            if i != '':
                user_dict_data = json.loads(i)
                if (userid == user_dict_data.get('username')) or (userid == user_dict_data.get('email')):
                    if user_password == user_dict_data.get('password'):
                        login += 1
                        usertype = user_dict_data.get('usertype')
        if login == 1:
                if usertype == 'buyer':
                #------Buyer site choices----#
                    print('''
                        Login successfull
                            1. View all product
                            2. View my bills
                            ''')
                    userchoice = input('Enter choice number: ')
                    if userchoice == '1':
                        username = user_dict_data.get('username')
                        usertype = user_dict_data.get('usertype')
                        print(f'Welcome to Ecommerce {username}')
                        Ecommerce.view_product(self,usertype,username)
                    elif userchoice == '2':
                        username = user_dict_data.get('username')
                        usertype = user_dict_data.get('usertype')
                        print(f'The bills of {username}')
                        Ecommerce.viewBill(self,username)
                    else:
                        print('Other choice is unavailable')
                else:
                    print('''
                        Login successfull
                            1. Add Product
                            2. View Listed Product
                            ''')
                    userchoice = input('Enter choice number: ')
                    if userchoice == '1':
                        sellername = user_dict_data.get('username')
                        Ecommerce.add_product(self,sellername)
                    elif userchoice == '2':
                        username = user_dict_data.get('username')
                        usertype = user_dict_data.get('usertype')
                        Ecommerce.view_product(self,usertype,username)
                    else:
                        print('Other choices unavailable')
        else:
            print('Invalid userid or password')

#---------Buyer view and purchasee  and Seller (own product) view function-------#
    def view_product(self,usertype,username):
        if usertype == 'seller':
            file = open('Ecommerce.product.txt','r')
            content = file.read()
            product_view = content.split('-')
            for i in product_view:
                if i != '':
                    product_dict_view = json.loads(i)
                    if username == product_dict_view.get('sellername'):
                        print(product_dict_view)
        else:
            file = open('Ecommerce.product.txt','r')
            content = file.read()
            product_view = content.split('-')
            for i in product_view:
                if i != '':
                    product_dict_view = json.loads(i)
                    print(product_dict_view)
            print('''
                    Do you want to purchase
                    ''')
            user_purchase_product_name = input('Enter product name you want to purchase: ').lower()
            user_purchase_product_quantity =  int(input('Enter product quantity you want to purchase: '))
            if user_purchase_product_name == product_dict_view.get('name'):
                #---------add buyer username define----#
                product_price = int(product_dict_view.get('price'))
                total = product_price*user_purchase_product_quantity
                print(f'Total {user_purchase_product_quantity} quantity {user_purchase_product_name} Bill amount is: Nrs: {total}')
            purchase_product_dict_data ={'name': user_purchase_product_name, 'price':product_price,'quantity':user_purchase_product_quantity,\
                                         'total bill':total,'seller':product_dict_view.get('sellername'),'buyername': username}
            product_bill_details_json = json.dumps(purchase_product_dict_data)
            file = open('billing.txt','a')
            file.write(product_bill_details_json + '-')
            file.close()
 #------------Seller product adding function-------#               
    def add_product(self,sellername):
        name = input('Enter Product Name: ').lower()
        price = int(input('Enter product price: '))
        description = input('Add product description: ') 
        product_details = {'name': name, 'price': price, 'descriptiton': description, 'sellername': sellername}
        product_details_json = json.dumps(product_details)
        file = open('Ecommerce.product.txt','a')
        file.write(product_details_json + '-')
        file.close()
        
#------------Buyer puchase bill and Seller selling bills function-----#
    def viewBill(self,username):
        file = open('billing.txt','r')
        content = file.read()
        bill_data = content.split('-')
        for i in bill_data:
            if i != '':
                bill_dict_data = json.loads(i)
                if username == bill_dict_data.get('buyername'):
                    print(bill_dict_data)
                else:
                    print(bill_dict_data)
abcCompany = Ecommerce()
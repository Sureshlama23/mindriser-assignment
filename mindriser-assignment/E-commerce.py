# Requirements
# Ask the user to login or register(if user want to register add user with name,email and password )
# if user registering define user usertype buyer or seller?
# while login if the user is buyer the add features 1. View all product, 2 Purchase product and
# 3. View all user bills or print out.
# if the user is seller make user choices: 1. Add products, 2. View all user product and
# 3. View all user products bill to recieve.


import json

while True:
    user_choice = (input('''
              Choose below option           
                1. Register
                2. Login 
                3. Exit
                Type here:- ''')).lower()

    def new_register():
        user_username = input('Enter name here: ')
        user_userpassord = input('Enter password here: ')
        user_email = input('Enter email address here: ')
        user_type = input('''
                    Are you Buyer or Seller
                          Type here:  ''').lower()
        if user_type == 'buyer' or 'seller':
            user_data = {'username':user_username,'password':user_userpassord,'email':user_email,'usertype': user_type}
            data_json = json.dumps(user_data)
            file = open('user_login_data.txt','a')
            file.write(data_json + '-')
            file.close()
        else:
            print(f'invalid User Type: {user_type}')     
    def  user_login():
        use_login = input('Enter name or email address: ')
        user_userpassord = input('Enter password here: ')
        file = open('user_login_data.txt','r')
        content = file.read()
        list_data = content.split('-')
        login = 0
        user_type = None
        for i in list_data:
            if i != '':
                user_dict_data = json.loads(i)
                if (use_login == user_dict_data.get('username')) or(use_login == user_dict_data.get('email')) :
                    if user_userpassord == user_dict_data.get('password'):
                        login += 1
                        user_type = user_dict_data.get('usertype')
        if login == 1:
            if user_type == 'buyer':
                print('''Login successfull
                        1. View all product
                    ''')
                userChoice = input('Enter your choice: ')
                if userChoice == '1':
                    use_login =user_dict_data.get('username')
                    view_product(use_login)
                else:
                    print('Other choice in unavaible')
            else: 
                print('''Seller site Login successfull
                      1. Add product
                      2. View listed product
                    ''')
                userChoice = input('Enter your choice: ')
                if userChoice == '1':
                        user_login =user_dict_data.get('username')
                        add_product(user_login)
                elif userChoice == '2':
                        user_login =user_dict_data.get('usertype')
                        view_product(user_login)
                else:
                    print('Other choice in unavaible')
        else:
            print('Username or password not found')
    def view_product(usertype):
        if usertype == 'seller':
            file =open('products.txt','r')
            product =file.read()
            seller_product = product.split('-')
            for i in seller_product:
                if i != '':
                    seller_product_list = json.loads(i)
                    if usertype == seller_product_list.get('usertype'):
                        for list in seller_product_list:
                            print(seller_product_list[list])
        else:
            file =open('products.txt','r')
            product =file.read()
            seller_product = product.split('-')
            for i in seller_product:
                if i !='':
                    seller_product_list = json.loads(i)
                    for list in seller_product_list:
                            print(seller_product_list[list])
    def add_product(seller):
        name = input('Enter your products name: ')
        price = input('Enter product price: ')
        description = input('Add product description: ')
        product_dic_data ={'name':name,'price':price,'description':description,'seller':seller}
        product_data_json = json.dumps(product_dic_data)
        file = open('products.txt','a')
        file.write(product_data_json + '-')
        file.close()
    if user_choice == 'register':
        new_register()
    elif user_choice == 'login':
        user_login()
    elif user_choice == 'exit':
        break
    else:
        print('Invalid choice')
# Requirements
# Ask user for login or register or exit
# After login give him/her choices : 1. View your total amount 2. Deposit amount 3. Withdraw amount
# After a choices function is run ask the user again for login , register and exit
# Every data should be on file
# To use this this program create userdata.txt file in same the folder

#Question how to autoincreament user's accountnumber or id in the file( user's database ) per new register to make unique?

import json

class Accounting:
    account_number = 11001200
    def __init__(self):
        while True:
                user_choice = input('''
                    Welcome to ABC company
                        Do you want Register or Login or Exit:
                                    
                            Type here: ''').lower()
                if user_choice == 'register':
                     Accounting.register(self)
                elif user_choice == 'login':
                    Accounting.login(self)
                elif user_choice == 'exit':
                     break
                else:
                     print('Invalid choice')                 
    def register(self):
        username = input('Enter name here:').lower()
        if len(username) >= 3:
             if username[::].isalpha():
                  pass
             else:
                print('Invalid username input')              
        else:
             print('Name is too short')
             
       #------Valid email address input-----#
        print('                                     ')
        email = input('Enter Your Email Here: ')
        email1 = input('Enter Your Email Here Again: ')
        a=0
        b=0
        if email == email1:
             if len(email) >=7 :
                    if email[0].isalpha():
                        if ('@' in email) and (email.count('@') == 1) and ('..' not in email) and (email.count('..') !=1):
                             if (email[-4] == '.') ^ (email[-3] == '.'):
                                  for i in email:
                                      if i.isspace():
                                            a =1
                                      elif i.isalpha():
                                           continue
                                      elif i.isdigit():
                                           continue
                                      elif i =='_' or i =='@' or i =='.':
                                           continue
                                      else:
                                           b=1
                                  if a==1 or b==1:
                                      print('Invalid Email address input')
                             else:
                                  print('Invalid Email address input')
                        else:
                             print('Invalid email address input 1')
                    else:
                        print('Email should be start with alpha')
             else:
                  print('Email is too shorter')

    #-----------end here valid email input function-------#
        print('                                ')
        print('Password should be 1 uppercase and length greaterthan 5')   
        password = input('Enter password here: ')
        password1 = input('Enter password here again: ')
        a=0
        if password == password1:
             if len(password) >= 6:
                for i in password:
                     if password.isupper() >= 1:
                          a=1
                if a==1:
                     print('Password should be 1 uppercase')
             else:
                  print('Password lenght should greater than equal 6')
        else:
             print('Your passwor does not match')
        list = []
        account_db_number = None
        file= open('userdata.txt','r')
        content = file.read()
        file.close()
        user_data = content.split('-')
        for i in user_data:
             if i != '':
                  user_dict_data = json.loads(i)
                  if user_dict_data != None:
                    list.append(user_dict_data)
                    Last_data = list[-1]
                    dict_data = dict(Last_data)
                    account_db_number = dict_data['accountNumber']
        if account_db_number != None:
             account_db_number += 1
             user_details = {'username': username, 'email': email, 'password': password, 'accountNumber': account_db_number,'balance': 0.00}
             user_account_json_data = json.dumps(user_details)
             file = open('userdata.txt','a')
             file.write(user_account_json_data + '-')
             file.close()
        else:
            user_details = {'username': username, 'email': email, 'password': password, 'accountNumber': self.account_number,'balance': 0.00}
            user_account_json_data = json.dumps(user_details)
            file = open('userdata.txt','a')
            file.write(user_account_json_data + '-')
            file.close()
#---------User Login add transaction function------------------------#
    def login(self):
          username = input('Enter your name: ')
          password = input('Enter password here: ')
          file = open('userdata.txt','r')
          content = file.read()
          file.close()
          user_data = content.split('-')
          for i in user_data:
               if i != '':
                    user_dict_data = json.loads(i)
                    if user_dict_data != None:
                        if username == user_dict_data.get('username') and password == user_dict_data.get('password'):
                              while True:
                                  a = 0
                                  userChoice = input(''' 
                                    Login Successful
                                    1. View account available balance
                                    2. Add balance
                                    3. Withdraw balance
                                    4. Back Mainmenu                
                                    Typer Here:    ''')
                                  if userChoice == '1':
                                       user_account_number = user_dict_data.get('accountNumber')
                                       Accounting.viewUserAmount(self,username,password,user_account_number)
                                  elif userChoice == '2':
                                       user_account_number = user_dict_data.get('accountNumber')
                                       Accounting.deposit(self,username,password,user_account_number)
                                  elif userChoice == '3':
                                       user_account_number = user_dict_data.get('accountNumber')
                                       Accounting.WithdrawAmount(self,username,password,user_account_number)
                                  elif userChoice == '4':
                                       a =1
                                       if a == 1:
                                            break
                                  else:
                                       print('Unavailavle other choice')
                        else:
                             print('Invalid username or password')
                             break
                    

#-------------View user available balance function-------#           
    def viewUserAmount(self,username,password,accountNumber):
         file = open('userdata.txt','r')
         content = file.read()
         file.close
         user_balance = content.split('-')
         for i in user_balance:
              if i != '':
                   user_dict_balance = json.loads(i)
                   if username == user_dict_balance.get('username') and password == user_dict_balance.get('password'):
                        user_total_balance = user_dict_balance.get('balance')
                        print(f'Total available balance is Nrs: {user_total_balance}')

#---------------User Deposit balance function------------#
    def deposit(self,username,password,accountNumber):
          amount_deposit = float(input('Enter amount deposit: '))
          if amount_deposit == float:
               pass
          file = open('userdata.txt','r')
          content = file.read()
          file.close
          user_dict_data = None
          user_balance_update = None
          user_balance = content.split('-')
          for i in user_balance:
               if i != '':
                    user_dict_balance = json.loads(i)
          if username == user_dict_balance.get('username') and password == user_dict_balance.get('password'):
                         user_balance_update = (user_dict_balance['balance']) + amount_deposit
                         user_dict_data = {'username': username, 'email': user_dict_balance.get('email'),'password': password,\
                                       'accountNumber': user_dict_balance.get('accountNumber'), 'balance': user_balance_update}
          user_dict_balance_json = json.dumps(user_dict_data)
          file = open('userdata.txt','w')
          file.write(user_dict_balance_json + '-')
          file.close
          print(f'Your amount Nrs: {amount_deposit} successfully deposit')
          print(f'Avaible balance is Nrs: {user_balance_update}')

#------------User balance withdraw function---------#
    def WithdrawAmount(self,username,password,accountNumber):
          amount_withdraw = float(input('Enter amount deposit: '))
          file = open('userdata.txt','r')
          content = file.read()
          file.close
          user_balance_update = None
          user_dict_data = None
          user_balance = content.split('-')
          for i in user_balance:
               if i != '':
                    user_dict_balance = json.loads(i)
          if username == user_dict_balance.get('username') and password == user_dict_balance.get('password'):
                    if   (user_dict_balance['balance']) >= amount_withdraw:
                         user_balance_update = (user_dict_balance['balance']) - amount_withdraw
                         user_dict_data = {'username': username, 'email': user_dict_balance.get('email'),'password': password,\
                                       'accountNumber': user_dict_balance.get('accountNumber'), 'balance': user_balance_update}
                    else:
                         print('Not enough balance')
          user_dict_balance_json = json.dumps(user_dict_data)
          file = open('userdata.txt','w')
          file.write(user_dict_balance_json + '-')
          file.close
          print(f'Your amount Nrs: {amount_withdraw} successfully withdraw')
          print(f'Avaible balance is Nrs: {user_balance_update}')


abcCompany = Accounting()
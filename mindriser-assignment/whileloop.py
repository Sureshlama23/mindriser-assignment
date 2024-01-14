while True:
    user_choice  = (input('''
    Do you want use calculator
        Choose between Yes or No?                 
''')).lower()
    if user_choice == 'yes':
        num1=float(input("Enter the value1:- "))
        num2=float(input("Enter the value2:- "))
        opr=input("Enter The Operator:- ")
        if opr=="+":
            print(num1+num2)
        elif opr=="-":
            print(num1 - num2)
        elif opr=="*":
            print(num1*num2)
        elif opr=="/":
            print(num1/num2)
        else:
            print("Invalid opr...")
    elif user_choice == 'no':
        break
    else:
        print('Invalid choice')
    
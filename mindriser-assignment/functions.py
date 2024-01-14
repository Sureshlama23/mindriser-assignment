
# Recursion
# Task requirements (Factorial)
# func(4) -> 4 * 3 * 2 * 1 -> return value

# Decorator
# Task requirements
# Make a list of usernames
# Make a add function , and use login decorator on that function
# The decorator should ask the user for his/her username, if the username is in list print welcome , {username} , else print nothing

# Lambda function
# Task requirments
# Make a lambda function which return multiplication of parameters

#  Recursion method of factorial
def fact(a):
    if a==0:
     return 1
    else:
       return((a)*fact(a-1))
number=int(input("enter here number:- "))
result=fact(number)
print(f'The given number factorial is {result}')


# derorator function

username = ['hari','sonim', 'sita', 'ram']

def login(func):
    def wrapper():
        name = input('Enter name here: ')
        if name in username:
            print(f'Welcome {name}')
            func()  
        else:
            print('Your name not found')
    return wrapper
@login
def add():
    num = float(input('Enter a number: '))
    num1 = float(input('Enter a number: '))
    result = num + num1
    print(f'The num{num} + num1 {num1} = {result}')
add()
    
# Lambda function

num = float(input('Enter a number: '))
num1 = float(input('Enter a number: '))

addNumber = lambda a, b : a * b
result = addNumber(num,num1)
print(f'The result is: {result}')



    



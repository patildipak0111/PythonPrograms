# This is a simple calculator

menuOption = input('+ for addtion, - for Subtraction, * for multiplication, / for Division : ')
a = int(input('Please input first number: '))
b = int(input('Please input second number: '))


     if(menuOption == '+'):
        res = a + b
     elif(menuOption == '-'):    
        res = a - b
     elif(menuOption == '*'):
        res = a * b
     elif(menuOption == '/'):
        res = a / b
     else:
        print('Please type something meaningful')
print('The result is:', res)


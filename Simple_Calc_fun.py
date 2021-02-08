
def simple_calc(menuOption, a = 0, b = 0):
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
     print("The result is ",res) 
     return res

##function with sigle parameter
##function with multiple parameter
##function with default parameter
##function with multiple length parameter

#----------------------------##function with multiple parameter--------------------------

def addition(number1, number2):
    print(f"addition of {number1} + {number2} is", number1+number2)




##positional argument are used to pass multiple values

def addition_loop(*num):
    add = 0
    for i in num:
        add = add +i
    print(add)

addition(3,4);
print(addition_loop(3,4,3,505050))

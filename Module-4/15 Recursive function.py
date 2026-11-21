#function calling same function untill we are reaching base conditon
#factorial of 8 = 8*7*6*5*4*3*2*1
#factorial of 98= 98*97*......*3*2*1


def factorial(number):
    if number==0 or number==1:
        print(f"faction of {number} is 1")
        factorial=1
    else:
        factorial =1
        for i in range(1,number+1):
            factorial = factorial*i;
        print(f"factor of {number} is {factorial}");

def factorial_recursive(numner):
    if numner ==0 or numner ==1 :
        return 1
    else :
        return numner* factorial_recursive(numner-1)

print(factorial_recursive(4))
    
###Lambda functions are use 1 liner functions defined by lamdda keyword and no name is required
#syntax for lambda expression
#lambda argument : expression

#they can have any number of argument but can have 1 logic
#they are used for short operations or as argument to higher order functions
#it can be trearted with function without name and no return statement required

#function which calculated the square of the number

def square(x):
    return x**2;

print(square(2));

k = int(input("enter the number x :"))
var1 =lambda x:x**2;
print(var1(k));

#calucate the sum of 2 number using lamda function
x1 = int(input("enter number 1 :"))
x2 = int(input("enter number 2 :"))
sum1 = lambda num1,num2: num1+num2
print(sum1(x1,x2))
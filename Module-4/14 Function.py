#Function are reusable means you can use again and again, it will help to organizing code
#no need use same code again and again.

def greetings(candidate_name):
    """function for greeting the candidate, this function take input as candidate name and greets the candidate"""
    print(f"Hello {candidate_name}, How are you ? we are liked your previous experience and your skillset now we are planning to move forward with you.");

print(greetings("Mithun"));

#why functions
#it increase readablity of the code, reusability and for organizing the code as well!!!

##creation of function which is going to take input number for user side and figure out that whether if the number is even or odd

def check_number_is_even_or_odd(number):
    if number%2==0:
        print(f"{number} is even");
    else:
        print(f"{number} in odd");
    

number = int(input("Enter the number :"));
check_number_is_even_or_odd(number)

def even_or_odd_instance(number):
    if isinstance(number,int):
        if number % 2 ==0 :
            print("Even number")
        else:
            print("Odd number")
    else:
        print("Invalid input not an integer input")

print(even_or_odd_instance('s'))

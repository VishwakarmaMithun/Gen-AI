
#Nested loop is used to iterate over series of number for the proper combination of numbers
#f string  will be helping us our i printing number with variable value present inside teh colons.
for i in range(5):
    for j in range(5):
        print(f"({i},{j})");

#printing the sum of n natural number

number = int(input("enter the number til which you wanted to sum:"))
sum = 0;

for i in range(0,number+1):
    sum = sum + i;

print(f"Sum of number ={sum}");
#while loop
#by making using of while loop you made 

i =0 
while (i<=59):
    print(i)
    i=i+1;

#print the number from 0 to 50 using while loop
print("-----------------------")
i = 0;

while (i<=50):
    if i%2==0:
        print(i);
    i=i+1;

print("-----------------------")
for i in range(0,51):
    if i%2==0:
        print(i);

#------------------------------------------

for i in range(51):
    if i%2==0:
        print(i)
    else :
        break;

#divison of number where denominator is 0
number_1 = int(input("Enter the numnerator value :"))
number_2 = int(input("Enter the denominator :"))
if number_2 ==0 :
    print("Enter denominator >0 :")
    pass
else:
    print(number_1/number_2)

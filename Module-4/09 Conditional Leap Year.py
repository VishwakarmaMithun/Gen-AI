#check the year is leap year or not
year = int(input("Enter the value"))
if year%4==0:
    if year%100==0: #not relevent check 
        if year%400==0: #not relevent check 
            print("Current Year is Leap Year");
        else:
            print("Current Year is not Leap Year");
    print("Year is leap Year")
else:
    print("Year is not Leap Year");

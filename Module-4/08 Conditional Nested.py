#In the nested conditional statment, if condition exists another if condition 
#compare the heights of three friends
first_person = int(input("Enter the age in cc:"))
second_person = int(input("Enter the age in cc:"))
third_person = int(input("Enter the age in cc:"))

if first_person > second_person:
    if first_person > third_person :
        print("First Person is the tallest")
    else :
        print("third person is the tallest")
else:
    if second_person > third_person:
        print ("second person is the tallest")
    else:
        print("third person is the tallest")

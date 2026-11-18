#Used for storing different data types in a single variable. It is a collection of items that are ordered and changeable. Allows duplicate members.
a =  list()
print(type(a))
b=  set()
print(type(b))
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5,"Abc",True,1.2]
print(list1)
print(list2)  

#list mutability and slicing
list3= ['apple', 'banana', 'cherry','mango','kiwi','orange','pear','grapes','papaya','guava ']
print(list3[2:5]) #slicing
print(list3[2]) #slicing
print(list3[-1])
print(list3[1:4])
print(list3[0:len(list3)]) #slicing with step
print(list3[0:-1]) #slicing with step
#example for list from -negative index to first index
print(list3[-1:-5:-1]) #slicing with step

list3[3] = 'watermelon' #mutability
print(list3)
# using lopping statement to iterate through the list
for x in list3:
    print(x)

list_items = [1,2,3,4,5,6,7,8,9,'Abc',True,1.2]
for x in list_items:
    print(str(x)) #this will give error because list_items[x] is not valid as x is the value not index. It should be print(x) instead of print(list_items[x])    

for x in list_items[0:list_items.index("Abc")]:
    print(x) #this will give error because list_items.index("Abc") returns the index of the first occurrence of "Abc" in the list, which is 9. It should be print(list_items.index("Abc")) instead of print(x)

print("-------------------------------")
print(list_items.index(9))

a =[1,2,3,5,65]
print(sum(a))
print(max(a))

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
#list methods
my_list = [1, 2, 3, 4, 5]
my_list.append(6) #adds an element to the end of the list
print(my_list)
my_list.insert(2, 2.5) #inserts an element at a specific index
print(my_list)
my_list.insert(0, 0) #inserts an element at the beginning of the list
print(my_list)
my_list.remove(2.5) #removes the first occurrence of an element from the list
print(my_list)
my_list.append(2) #adds an element to the end of the list
print(my_list)
my_list.remove(2) #removes the first occurrence of an element from the list
print(my_list)
my_list.remove(2) #removes the first occurrence of an element from the list
print(my_list)  
my_list.insert(2, 2) #inserts an element at a specific index
print(my_list)
my_list.pop() #removes and returns the last element of the list
print(my_list)
my_list.pop(2) #removes and returns the element at a specific index
print(my_list)
my_list.insert(2, 2) #inserts an element at a specific index
print(my_list)
print(len(my_list)) #returns the number of elements in the list
my_list.index(3) #returns the index of the first occurrence of an element in the list
print(my_list.index(3))
my_list.insert(3,"Rajesh") #inserts an element at a specific index
print(my_list)
my_list.pop(3) #returns the element at a specific index
print(my_list)
list_items = [1,2,3,4,5,6,7,8,9,'Abc',True,1.2]
print(list_items)   
list_items.append("New Item") #adds an element to the end of the list
print(list_items)
list_items.clear() #removes all elements from the list
print(list_items)

#append method insterts an element at the end of the list
#remove method removes the first occurrence of an element from the list
#insert method inserts an element at a specific index
#clear method removes all elements from the list
#pop method removes and returns the last element of the list or the element at a specific index
#sort method sorts the elements of the list in ascending order, for same data types
#index method returns the index of the first occurrence of an element in the list

numbers = [11, 2, 33, 4, 5, 6, 7, 8, 9,24,54,12,13,14,15,16,17,18,19,20]
#enumerate method returns an enumerate object, which contains pairs of index and value for each element in the list
for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")

lyst = [1, 2, 3, 4, 5]
#list comprehension is a concise way to create lists in Python
for i,v in enumerate(lyst):
    print(f"Index: {i}, Value: {v}")

#len function returns the number of elements in the list
print(len(lyst))

#list comprehension

list_item2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#using list comprehension to create a new list with squares of the elements in the original list    
#in the list comprehension conditional statement are allowed

#[expression for item in iterable if condition]

#expresion is the value to be added to the new list, item is the current element in the iterable, and condition is an optional filter that determines whether the item should be included in the new list.
#for is a keyword that indicates the start of the loop, and in is a keyword that specifies the iterable to loop over.
#I need to store values from 1 to 50

list_item3 = [i for i in range(1, 51)]
print(list_item3)

list_squared = [i**2 for i in range(1, 51)]
print(list_squared)

list_even = [i for i in range(1, 51) if i % 2 == 0]
print(list_even)

#if you looking for square value of even numbers from 1 to 50, you can use the following list comprehension:
list_even_squared = [i**2 for i in range(1, 51) if i**2 % 2 == 0]
print(list_even_squared)

list_item4 = ["apple", "banana", "cherry", "date", "elderberry"]
list_items_lenght  = [len(i) for i in list_item4]
print(list_items_lenght)

list_item_upper = [i.upper() for i in list_item4]
print(list_item_upper)

#nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#flatten the matrix using nested list comprehension
flat_matrix = [num for row in matrix for num in row]
print(flat_matrix)

for i, value in enumerate(matrix):
    print(f"Index: {i}, Value: {value}")    

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

#paired list is a list of tuples, where each tuple contains one element from lst1 and one element from lst2. The list comprehension iterates over each element in lst1 and lst2, creating a tuple for each combination of elements.
paired_list = [(x, y) for x in lst1 for y in lst2]
print(paired_list)



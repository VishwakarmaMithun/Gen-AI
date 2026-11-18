#tuples are second type of data structure in python after lists. Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.
#tuples are non mutable, ordered collection of elements. They are defined using parentheses () and can contain elements of different data types.

tuples1 = ()
print("Empty tuple:", tuples1)

a = ()
print("Empty tuple:", a)

tuple_values = (1, 2, 3, 4, 5)
print("Tuple with values:", tuple_values)

for i, value in enumerate(tuple_values):
    print(f"Index: {i}, Value: {value}")

#tuples are also capable of storing different data types, including strings, integers, floats, and even other tuples.   

tuple_mixed = (1, "Hello", 3.14, (2, 4))
print("Tuple with mixed data types:", tuple_mixed)

print( tuple_mixed[1:3])

print(tuple_mixed[-1])  # Accessing the last element of the tuple   

print(tuple_mixed[:-1])  # Accessing all elements except the last one


#tuple methods: Tuples have a limited set of methods compared to lists. The two most commonly used methods are count() and index(). The count() method returns the number of occurrences of a specified element in the tuple, while the index() method returns the index of the first occurrence of a specified element.

tuple_method = (1, 2, 3, 2, 4, 2,5,6, 2)
tuple_method.count(2)  # Count the occurrences of 2 in the tuple
print(tuple_method.index(4))  # Get the index of the first occurrence of 4 in the tuple
print(tuple_method.count(2))  # Count the occurrences of 2 in the tuple
print(tuple_method.index(1))  # Get the index of the first occurrence of 2 in the tuple

print(tuple_method);

a = 1,4,5,"Hello",2.5
print(a)
b = (1,2,3,4,5)
print(b)
x,y,z,p,q = 1,2,3,4,5
print(q)

#unpacking of tuples
first_value,*e,last_value = (1,2,4,5,6,9,10,10)
print(first_value)
print(e)
print(last_value)

#NestedList
NestedList = [1,2,3]

#tuple insider list list

num_1= 45
num_2 = 6
print(num_1+num_2)

#tuple + operation is concating 2 tuple.

num_3 = (1,3,4)
num_4 = (4,5,6)
print(num_3+num_4)

print(num_3*3)
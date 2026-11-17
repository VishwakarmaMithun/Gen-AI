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



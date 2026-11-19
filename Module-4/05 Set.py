### sets are data structure which consist of value within the curly bracket
## used to store the value which are non duplicate

set_1 = {1,2,3,4,5,5}
print(set_1)
for i in set_1:
    print(i)

print(type(set_1))

set_1.add("Raj")
print(set_1)
print(len(set_1))
set_1.add(1)
print(set_1)

set_empty = set()
print(type(set_empty))

list_1 = [1,1,2,3,4,5,5]
set_list = set(list_1)
print(set_list)
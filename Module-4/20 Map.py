##map functions applieds a given function operation to all item in a iterable or a list and returns a Map Object.
##map function is particulary usefull for tranformaing the data
#syntax  map(function,iterable)
#list(map(function,iterable))

#simple way
def square(list_items):
    squared_items =[];
    for item in list_items:
        squared_items.append(item**2);
    return squared_items;

print(square([1,3,4,5,6,9]));

#logic using map function....square

print(list(map(lambda x:x**2,[1,2,3,4,5,6])));

##Map function with basic function in it

def squared_numner(numn):
    return numn*2;

print(list(map(squared_numner,[1,2,3,4,5,6])))

##L
number_1 = [1,2,3,4]
number_2 = [4,5,6,6]

print(list(map(lambda x,y:x+y, number_1, number_2)))

## convert all string value to integer
print(list(map(int,['1','2','4','5'])))

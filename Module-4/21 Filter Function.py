#Filter function is going to retrieve only those items which are meeting a certain condition in an iterable
#for the condition becomes true
#syntax for filter function
#filter(function,iterable)

#list(filter(func,iterable))


print(list(filter(lambda x:x%2==0,[1,2,3,4,5,5,6,6,9,20])))

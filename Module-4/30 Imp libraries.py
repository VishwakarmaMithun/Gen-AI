#python standard library comes with was collection of packages
from calendar import month
from datetime import datetime
from math import *
import random
import csv
import datetime
'''
int_number =int(input("Enter the number whose square root you want to calculate :"))
print(sqrt(int_number))

#random library is used for generating random numbers

l = random.randint(1,10)
k = random.randint(1, 100)
print(l);

print(random.choice(['Head','Tail']));

# csv library for laoding csv file
# create csv file
# write the content 
# read the content

with open('example.txt',mode='w',newline='') as file:
    writer =csv.writer(file)
    writer.writerow(['name','age']);
    writer.writerow(['Amit','23']);

with open('example.txt',mode='r') as file:
    reader = csv.reader(file);
    for r in reader :
        print(r)
'''
#Date Time library

from datetime import datetime, timedelta
print(datetime.now())
print(datetime.now()-timedelta(days=1))
print(datetime.now()-timedelta(minutes=24))



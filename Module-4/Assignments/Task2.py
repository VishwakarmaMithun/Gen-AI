#Author: Mithun Vishwakarma
#Date :25/11/2026
#create a list name products containing atleast 6 products

product_list = ['Soap','Shampoo','Brush','Scissors','Blade','Luffa','Soap','Brush']
category_set = set(product_list)
print('Initial product list',product_list)
print('Category Set :', category_set)

#adding new value to category_set
category_set.add('Brush_1')
print(category_set)

#try adding existing category to category set
category_set.add('Soap')
print(f"Category :{category_set}")

cat1 = 'Soap'
cat2 = 'Soap_not_exists'

if cat1 in category_set:
    print('Exists')
else:
    print('Not exists')


if cat2 in category_set:
    print('Exists')
else:
    print('Not exists')


print("Length of category set:",len(category_set))
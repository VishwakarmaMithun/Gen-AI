#Author: Mithun Vishwakarma
#Date :25/11/2026
#create a list name products containing atleast 6 products

product_list = ['Soap','Shampoo','Brush','Scissors','Blade','Luffa']
print(f"Product list : {product_list}");

#Tuple storing product_name,price,category
sample_product = ('Soap',40,'Beauty')
print(sample_product)

#accessing 1st product and last product
print(f"Fist product:{product_list[0]}")
print(f"Last Product:{product_list[-1]}")

#adding 2 new products

product_list.append('Brush_1')
product_list.append('Brush_2')

print(product_list)

#updating price to tuple

temp_list = list(sample_product)
temp_list[1]=50
sample_product = tuple(temp_list)
print(sample_product)
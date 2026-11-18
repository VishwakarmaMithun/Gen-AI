#dictionary in python are data structure are storing value in simalar way link how you store value
#in key value format

#syntax
#{key:value}

#column and rows format
#name email   phone
#Mithun mitunv@live.com 959922
#{"name":['Mithun','Vishwakarm'], "email":["a@b.com","c@y.com"],"phone":[900900,900902]}

dictionary1 = {"name":['Mithun','Vishwakarm'], "email":["a@b.com","c@y.com"],"phone":[900900,900902]}

print(dictionary1["name"])
print(dictionary1["name"][0])
print(dictionary1["email"][1])

dictionary1["email"][1] ='k@y.com'
print(dictionary1)

del dictionary1["email"][1];
print(dictionary1)

#dictionary methods 
#keys()
#values()
#items()
#get()

dictionary ={"name":"Mithun", "fruit":"Apple","vegetable":"potatoes","lst1":[1,2,4,5],"Numbers":34 , "a":3}
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.get("name"))

del dictionary["name"];

#shallow copy is used to copy of the original dictionary in a way such that


dict_1 = {"name":"Mithun"}
dict_2 = dict_1
print(dict_2)
dict_2 = {"name1":'Mithun', "b":"xyx"}
print(dict_2)
print(dict_1)
dict_3 = dict_2.copy()
print(dict_3)

#wanted to store 
Nested_dict = {"student1":{"Name":"Mithun","Marks":89},
                                                "student2":{"Name":"Raj","Marks":90}
}

print(Nested_dict["student1"]["Marks"])

for outer_key, outer_value in Nested_dict.items():
    for key1 ,value1 in outer_value.items():
        print({key1});
        print({value1})


dict_a = {"name":"Mithun","a":23,"b":24}
dict_b = dict_a
print(dict_a)
print(dict_b)
dict_a["a"] = 44;
print(dict_a)
print(dict_b)
dict_c = dict_a.copy()
print(dict_c)
dict_a["a"]=55;
print(dict_a)
print(dict_b)
print(dict_c)
student_1={"name":"Mithun","mark":34}
student_2={"name":"Raj","mark":45}
student_3={"name":"Kiran","mark":60}
dict_nested = [student_1,student_2,student_3]
print(dict_nested)

for value in dict_nested:
    for item, value1 in value.items():
        print(f" {item}: {value1}")

dictionary_1 = {"a":5,"b":2}
dictionary_2     = {"a":4,"c":4}
dictionary_3 ={"a":6}

merged_dictionary = {**dictionary_1,**dictionary_2,**dictionary_3}
print(merged_dictionary)
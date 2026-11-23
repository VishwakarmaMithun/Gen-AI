#trying to write content of the field line by line
list_lines = ['First_line\n','Second_line\n','Third_line\n']

with open('example.txt','w') as data:
    data.writelines(list_lines)

##mode---> write the content into the binary file rb
##mode--->Read teh content  from the binary file. wb

data=b'\x00\x01\x02\x03\x04'
with open('example.txt','wb') as binarydata:
    binarydata.write(data);


with open('example.txt') as binarycontent:
    binarycontent_var = binarycontent.read()
    print(binarycontent_var)

#read the content from 1 file and write the content in another file.binarycontent_var

with open('source.txt','r') as read_data:
    content = read_data.read();

with open('destination.txt','w') as destination_data:
    destination_data.write(content);
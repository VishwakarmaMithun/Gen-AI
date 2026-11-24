#OS Library is able to interact with operating system and can let us work with mutliple directories and files
## getcwd() --- it is capable of idea of current working directory.
from os import mkdir, listdir
import os
current_path = os.getcwd();
print(current_path);
#mkdir() ---- it is capable of doing making new directory. it is helping to create new directory
variable_path = os.getcwd()+"\\new_folder\\"
os.chdir(r'C:\Users\MITUN\OneDrive\Documents\Learning\Restart\Gen-AI\Module-4')

print(os.getcwd())
print(listdir())
print(variable_path)
if os.path.isdir(variable_path)==False:
    os.mkdir(variable_path)


##mkdir, chdri,getwd, 

full_path =os.path.join(variable_path,'/','new_flder')
print(full_path)
directory_name='Folder1'
file_name = 'a.txt'
current_complete_path = os.path.join(os.getcwd(),directory_name,file_name)
print(current_complete_path)

if os.path.isdir(r'C:\Users\MITUN\OneDrive\Documents\Learning\Restart\Gen-AI\Module-4'):
    print('path exists')
else:
    print('path does not exists')


if os.path.isfile(r"C:\Users\MITUN\OneDrive\Documents\Learning\Restart\Gen-AI\Module-4\01 List.py"):
    print('is file');
else :
    print('not a file');

print(os.path.abspath(r"01 List.py"));
print(os.path.realpath(r"C:\Users\MITUN\OneDrive\Documents\Learning\Restart\Gen-AI\Module-4\01 List.py"))

print(13//2);
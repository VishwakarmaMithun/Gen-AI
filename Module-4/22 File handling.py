#File handling
#infomation can be there in ram or in file
#Ram    ->information will be stored in temporary
#file   -> information will be sored permanently
#images ->will be stored in binary format.
#NLP - > information will be stored in text format
#Deep Learning model -> binary format file
# Format of file (.txt, .docx, csv)
# binary files, .mp4, mp3, mov)

#-----Read the content from the dairy/book
# 1. Open the dairy
# 2. Read the content from dairy
# 3. Close the dairy

# writing the conten of the dairy
# 1. Open the dairy
# 2. Write the content into the dairy
# 3. Close the content 

# Reading and Writing content of the file
# 1.Open the dairy
# 2.Read the content of the file
# 3.write the content of the file
# 4.close the content of the File

#open() ---> Opening the file
#First parament - > file_namer
#Second Parameter-> 
# Mode (r-read, 
# w write, 
# r+ read the content and writing contert,
# w+ writing the content and reading )

print("----------------------")
f= open("example.txt",'r')
content =  f.read()
print(content)
f.close()


print("----------writing-----------")
f=open("example.txt",'w+')
f.write('we are writing the content into the file')
f.close()
f = open("example.txt",'r');
content_2= f.read()
print(content_2)
f.close();

f = open("example.txt",'a')
f.write("genai")
f.close();
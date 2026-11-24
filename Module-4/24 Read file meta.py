#Reading the total lines, total words, total characters from files--readlines();

def count_line(file):
    with open(file,'r') as docreader:
        content= docreader.readline()
        total_lines = len(content);
        total_words = sum(len(line.split()) for line in content);

#readliness() ----> Reads the line in a way where it values are stored in the list
#['First_line','Second_line','Third_line']

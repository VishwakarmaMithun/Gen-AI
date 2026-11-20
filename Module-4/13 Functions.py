#function definitions
##function is the block of code that performs specific task
##function is helping orgainizing code and resuing for improving read ability

#systax of function

def question_answering():
    """This is sample comment , this is call Docstring"""
    #function body
    return 'x';

def translator(english_text):
    """function for language translation"""
    if english_text =='hello':
        print(f"then the translation if for {english_text} is Namaste");

print(question_answering())

#we are creating a function for language transalation

text = input("Enter the value for translation")
print(translator(text.lower()))

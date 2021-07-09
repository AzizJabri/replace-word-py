import os
from sys import platform

def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')


def writing(txt):
    with open('output.txt', 'w') as outfile:
        outfile.write(txt)
    print('DONE !, check output.txt')

 
# keyword to stop reading words to replace
keyword = ' '
clear()

print('Type the text to replace words in :')
txt = str(input())
answer = ''
words = []
# reading words to replace
while answer != keyword:
    os.system('cls')
    print('Words To Replace (insert empty space to continue) :', ', '.join(words))
    answer = str(input())
    if answer != keyword:
        words.append(answer)
clear()
# reading word to repalce with
print('Write the word to replace with :')
replace = str(input())
# replacing words
for i in words :
    text = txt.replace(i, replace)
    txt = text
    
txt = " ".join(txt.split())


# uncomment this if you want the output printed to console :
print(txt)

# writing the text to output.txt (uncomment this if you want the text as a file 'output.txt')
#writing(txt)
# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from cgitb import text


def read_file_content(filename):
    # [assignment] Add your code here 
 with open("story.txt", "r") as bread:
   print(bread.read())
read_file_content("story,txt")

def count_words():
 text = read_file_content("story.txt")
    # [assignment] Add your code here
counts = 0
for line in text:
 counts += 1
print (text |": {counts}")

count_words ()



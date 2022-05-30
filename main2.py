# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from posixpath import split


def read_file_content(filename):
    # [assignment] Add your code here 
    with open ("story.txt") as f:
        contents = f.read()
        contents=contents.split(" ")
        return contents

def count_words(path):
    text = read_file_content("story.txt")
    pack = {}
    for word in text:
        if (len(word)) != 0:
            word = word.strip()
            word = word.strip ("?/n.,")
            if word in pack.keys():
                pack[word] != 1
            else:
                pack[word] = 1
    return (pack)
print(count_words("story.txt"))

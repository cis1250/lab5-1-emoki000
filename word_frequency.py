#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

def get_sentence():
   text= input("enter a sentence:" )
   return text

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

frequency=[]
words=[]

def calculate_frequencies(text):
    text=text.lower()
    sent=text.split()
    for word in sent:
        sen=word.strip(".,?!")
        if sen in words:
            index=words.index(sen)
            frequency[index]+=1
        else:
            words.append(word)
            frequency.append(1)
    return words, frequency

def print_frequencies(words, frequency):
    for i in range(len(words)):
     print(f"{words[i]}: {frequency[i]}")


def main():
 while True:
    sent = get_sentence()
    if is_sentence(sent):
     break 
 word,freq=calculate_frequencies(sent)
 print_frequencies(word,freq)

main()






   








   

'''
https://www.codewars.com/kata/520b9d2ad5c005041100000f
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

from string import punctuation

def pig_it(text):
    temp = []
    for word in text.split():
        if word not in punctuation:
            temp.append("".join(word[1:] + word[0] + "ay"))
        else:
            temp.append(word)
    return " ".join(temp)

"""
https://www.codewars.com/kata/57a5015d72292ddeb8000b31/python
Palindrome strings
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward or forward. This includes capital letters, punctuation, and word dividers.

Implement a function that checks if something is a palindrome. If the input is a number, convert it to string first.

Examples(Input ==> Output)
"anna"   ==> true
"walter" ==> false
12321    ==> true
123456   ==> false

"""
def is_palindrome(string):
    sequence_as_string = str(string).lower()
    reversed_input = str(sequence_as_string[::-1]).lower()
    if sequence_as_string == reversed_input:
        return True
    return False
'''
Use max, min, and sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions 

Modify your code to use lambda expressions instead of separately defined key functions.

'''

# Write your code here:
def max_by_key(items, key):
    biggest = int()
    for item in items:
        if key(item) > key(biggest):
            biggest = item
    return biggest

def get_spaces_count(input_str):
    space_count = sum((str(c)).isspace() for c in input_str)
    return space_count

def most_spaces(spaces_str):
    max_space = max(spaces_str, key=get_spaces_count)
    return max_space

def vowel_ct(sentance):
    vowels = ("a","e","i","o","u")
    vowel_count = int(0)
    for char in sentance:
        if char in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

def fewest_vowels(*args):
    min_vowel = min(args, key=vowel_ct)
    return min_vowel


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2016 Aaron Maxwell. All rights reserved.

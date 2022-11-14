'''
Regular Expressions
- sequence of characters that forms a search pattern.
- RegEx checks if a string contains the specified search pattern.

RegEx Module
- re package in python can be used to work with regular expressions
 import re

RegEx Functions  - python methods i use to work with regular expressions like search string.
Metacharacters - characters has meaning.
    example:
            * means 0 or more occurrences.
            [] set of chars
            ^ starts with
            \ special sequence
Special Sequences  - a sequence is slash followed by character and it forms a meaning.
    example: 
            \s - returns match when there is a space
            \S - returns match when there is no space.
            \d - returns match when there is a number.
            \D - returns match when there is no number
            \w - returns match when there is character
            \W - returns match when there is no character.
Sets - set of characers have a special meaning like numbers set or characeters set
    example:
            [abc] - returns match when one of characters is found
            [0-9] - returns match when number from 0 to 9 found
            [a-zA-z] - returns a match when character found regarding of Upper or lower
'''
import re

string = "today weath is very cold"

'''
search  - result is match object
    - re.search('pattern', my string)
    - result is object:
         span property: span( index_found, characters_count of the match)
         match property: the match found
'''
is_match = re.search('^t.*d$', string)

print(is_match)
print(len(string))

'''
findall - returns a list of all matches the given pattern
    - re.findall('pattern', my_string)
    - result: ['match 1', 'match 2, etc....]
            - when no match found: empty list []

'''
find_all_result = re.findall('e', string)
print(find_all_result)

'''
split - Returns a list where the string has been split at each match
    re.slpit('match_string', my_string)
    - result:
            a list contains the string sliced when pattern match and add each slice into list
        maxsplit=2 will given me two list items then adds the rest of string to list as item
'''
split_result = re.split('\s', string)  # \s = ' '
print(split_result)

'''
sub - replace match with new value
    re.sub(pattern, new_value, string)
    result:
        input : re.sub(' ', '.', "today weath is very cold")
        output: "today.weath.is.very.cold"
'''

sub_result = re.sub(' ', '.', string)
print(sub_result)
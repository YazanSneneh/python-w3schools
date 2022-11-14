#'================== String Methods ===================
y = '''
this is
a 
multi line
variable
'''

a = "  Hello, World!  "
print(len(a)) # length of list
print("World" in a) # check if sub-string in string
print("world" not in a) # check if word is not in string
print(a.upper()) # format to upper case
print(a.lower()) # format to lower case
print(a.strip().split(","))# split string into list with spereator
print(a.replace("Hello", "kill")) # find word and replace it
print(a.strip()) ## remove space before and after string
print(a.index("H")) # return position of item in list.
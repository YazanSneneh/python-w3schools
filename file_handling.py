'''
File Handling in python
    - is a way to working with files in programming.
    - i use it to store data permentantly on device.
    - i can perform various operations like writing to file and reading file.

File Handling
- Python has several functions for creating, reading, updating, and deleting files.

- open() function:
    parameters: it takes two parameters, file path and mode.
    example : open(file.txt, 'r')

modes are:
    'r' - read - open file for reading, it will raise an error if no file with provided name.
    'w' - write - open file for writing, create file if does not exist.
    'a' - append - open file for appending at the end of file, create a file if does not exist.
    'x' - create - create a file, raise an error when if file exists.

i can handle file as binary or text mode.
- i add the handle mode in the operation mode like this 'rt' (read mode and text are default)
 't' - to handle file as text mode.
 'b' - to handle file as binary mode like image or sound because it's stream input.

Close Files
- when I am done with file, i should always close it.
'''

my_main = open('./text_file.txt')
print(my_main)   # returns an object with name, mode and encoding properties.
# print(my_main.name)
# print(my_main.mode)
# print(my_main.encoding)

'''
Reading file
- open function has a method .read() to read the whole file.
- i can read specific number of characters - .read(10)
'''
# print(my_main.read())
# print(my_main.read(10))


'''
readline()
I can read file line by line by calling .readline()
- observation: when python read n number of characters, it will be ignored in the next read
'''
# print(my_main.readline())
# print(my_main.readline())
# print(my_main.readline())

'''
I can loop over lines inside file and read them one by one.
'''

lines = my_main.readlines()
for line in lines:
    print(line)
    # print(my_main.readlines())


'''
Writing to file
'''
file = open('text_file.txt', 'a')
# file = open('text_file.txt', 'w')
file.write("\na new line in the text file has been added from python")
file.close()

try:
    file = open('text_file.txt', 'x')
except FileExistsError:
    print(f"{FileExistsError}\n File exist")


'''
Delete a File
- to delete a file i need to work with os module.
    - os.remove(path)    - remove file
    - os.path.exist(path) - return true
- to delete a folder also i need to work with os
    - os.rmdir(path)
'''
import os

path = "./something.txt"

if not os.path.exists(path):
    print("the file in path does not exist")
else:
    os.remove(path)
'''
Python Try Except

Exception Handling
- try and except is bascially two faces to the same coin, what does that mean?
    - normally when user send invalid input like a field accepts integer but string was given.
        the program will crash and stop executing.
    - also sometimes i try to use variables are not declared can also raise errors.
        - a good example working with external files like dbs and files.
    - to prevent this I use try, except block.
    try block: lets me execute a block of code.
    except block: when errors occurs instead of crashing the program, it will catch error
                then gives me freedom to act upon it, like printing it or send information
                to user.

the puzzle pieces:
    try - execute a block of code and check for errors, if error found execpt block will work
    except - executes a block of code, when error occurs, the block will handle the error.
    else - executes a block of code when there is no error (try and els will work together)
    finally - executes a block of code always.
        note about finally: This can be useful to close objects and clean up resources.
        like database connection and closing file.

Raise an exception:
when python interpreter can't execute a line of code, i can raise an error.
    - in this way i am telling python to handle the regular events and exceptional events.
'''

# i should cast the value before adding, but trying to demonstrate.
try:
    user_input = input("enter valid number: ")
    print(user_input+2)
except:
    print("Please Enter a number")

'''
    Many Exceptions
    - the general form is one try and one except for the code.
    - if I want to raise special type of error i can add except block with error type
            I want to handle.
'''

try:
    print(x)
except TypeError:
    print("Please Enter a number")
except:
    print("variable x is not define.")

'''
else get executed, when try executed.
finally get executed when in any cases, try, except, except 2, etc...

'''

try:
    print("demonstrate the else block and finally")
except:
    print("Please check for errors")
else:
    print('the else block will be executed because no error')
finally:
    print("the block gets executed if error raised or not")
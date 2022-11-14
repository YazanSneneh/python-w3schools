# import random
# x= random.randrange(1,7)
# print(float(x))
 
#  =================================== importing modules ==========================
from classes_objects import Human as Person
    # from classes_objects import Human
    # import classes_objects
#  =================================== importing modules ==========================

person = Person('Ahmad', 30, True, True)
print(person.name)


ahmad = Person('Ahmad', 30, mouth=True, talk=True)
print(ahmad.name)
ahmad.speak()
print(f"number of legs: {ahmad.number_of_legs}")
Person.update_number_of_legs(44)
print(f"number of legs after updating using @classmethod: {ahmad.number_of_legs}")

# ==================================== Built-in Modules ================================
# Import and use the platform module
import platform
print(platform.machine())
print(platform.system())

# Using the dir() Function - built-in function to list all the function names (or variable names) in a module.
human_class_methods = dir(Person)
print(human_class_methods)

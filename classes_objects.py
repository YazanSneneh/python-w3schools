'''
Python OOP:

The __init__() Function (class Constructor)
classes have a function called __init__(),
    - which is always executed when the class is being initiated

this keyword in python is self
note: self is not reserved keyword like this, meaning i can call it whatever i want.
    but it have to be first argument.
    should be passed to all methods in class
'''
# =================== Parent class ============================
class Mammal():
    def __init__(self, name, age, mouth = True):
        self.name = name
        self.age = age
        self.mouth = mouth

# ===================== Child class ========================
class Human(Mammal):
    # class variable
    number_of_legs = 2
    def __init__(self, name, age, mouth=True, talk=True):
        super().__init__(name, age, mouth)
        self.talk = talk

    def speak(self):
        if self.mouth == True and self.talk == True:
            print("Hello my name is " + self.name)
        else:
            print("noise")

# toString() method
    def __str__(self) -> str:
        return f"name: {self.name}"

    @classmethod
    def update_number_of_legs(cls, value):
        cls.number_of_legs = value


'''
to prevent the interpreter from executing below code i can comment it out.
but i don't want to since it was written here for a purpose.
''' 
yazan = Human('Yazan', 30, mouth=True, talk=True)
print(yazan.name)
yazan.speak()
print(f"number of legs: {yazan.number_of_legs}")
Human.update_number_of_legs(44)
print(f"number of legs after updating using @classmethod: {yazan.number_of_legs}")
# # Modify Object Properties
# my_object.name = 'New Name'

# del my_object.age   # Delete Object Properties
# del my_object   # Delete Object Properties
# print(my_object)
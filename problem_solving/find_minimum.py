'''
Minimum of two numbers in Python

Given two numbers, write a Python code to find the Minimum of these two numbers.

Examples: 
    Input: a = 2, b = 4
    Output: 2

    Input: a = -1, b = -4
    Output: -4

'''
def min_naive(num1, num2):
    if num1 < num2:
        return num1
    return num2

def min_ternary(num1, num2):
    return num1 if num1 < num2 else num2

def min_lambda(num1, num2):
    minimum = lambda a,b: a if a<b else b
    return minimum(num1, num2)

def min_built_in(num1, num2):
    return min(num1, num2)

print(f"maximum number naive method: { min_naive(1,3)}")
print(f"maximum number ternary method: { min_ternary(14,3)}")
print(f"maximum number lambda method: { min_lambda(10,3)}")
print(f"maximum number built in method: { min_built_in(2,5)}")
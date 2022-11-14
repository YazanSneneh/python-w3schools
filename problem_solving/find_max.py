'''
Maximum of two numbers in Python

Given two numbers, write a Python code to find the Maximum of these two numbers.

Examples: 
    Input: a = 2, b = 4
    Output: 4

    Input: a = -1, b = -4
    Output: -1

'''
def max_naive(num1, num2):
    if num1 > num2:
        return num1
    return num2

def max_ternary(num1, num2):
    return num1 if num1 > num2 else num2

def max_lambda(num1, num2):
    maximum = lambda a,b: a if a>b else b
    return maximum(num1, num2)

def max_built_in(num1, num2):
    return max(num1, num2)

print(f"maximum number naive method: { max_naive(1,3)}")
print(f"maximum number ternary method: { max_ternary(14,3)}")
print(f"maximum number lambda method: { max_lambda(10,3)}")
print(f"maximum number built in method: { max_built_in(2,5)}")
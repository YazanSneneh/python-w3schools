# declare function
def fun():
    pass
# call function
fun()

# Number of Arguments
def fun2(v, v2):
    pass
# calling the fun2 with more than or less the number of args will get me error.

# ======================== Arbitrary Arguments, *args ==========================

# - to solve previous problem: I add asterisk before my argument on function decleration.
    # this way i can pass as many values as i want since the function now receive a tuple.
    # then i can access values by index or loop over the tuple
# it works because of the packing and unpacking concept
def calc(*vals):
    sum =0
    for v in vals:
        sum = sum+v
    return sum

vals = [1,2,3,4,5,22, 50]
sum = calc(*vals)
print(f" the sum value is: {sum}")

# I can pass to function keyword arguments: the problem with previous arguments usage:
    #  is that the argument order matters when i call the function.
#  keyword arguments don't care for order.
def keywords_fun(key1, key2):
    print(f" key 1: {key1}")
    print(f" key 2: {key2}")

keywords_fun(2,1)    # ordered invokation
keywords_fun(key2 = 2, key1=1)  # keyword invocation

# ======================== Arbitrary Keyword Arguments, **kwargs ====================
# I can pass keyword arguments by adding two asterisks before variable.
# this way my function will receive dictionary.
# to access values i use the keyword was passed as key to argument name, see example below:
def kwargs_fun(**dic):
    print(dic)
    print(dic.get('age'))

dic = {
    "age":30,
    "fname": 'Yazan',
    "lname": 'Sneneh'
}
kwargs_fun(**dic)
kwargs_fun(age=30, fname="Yazan", lname= "Sneneh")

# note if i want to pass ordered and keyword arguments, i must pass ordered first then keywords.

# =================== Default Parameter Value =====================
# i can add a default value on function declration so that my app dont crash.
def fun(number = 0):
  print(f"number value of passed or default value: {number}")

fun()   # will not crash if i pass arguments less than function declration.
fun(2)

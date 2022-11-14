""" CHALLENGE 2
Write a function named `add_exclamation` that takes an array of strings, 
and returns a new array of the same strings with an "!" added to the end.
Use `forEach` to loop over the input array.
Modify each string, and add the updated value into a local array.
Return the local array
"""

words = ["Love", "Peace", "Freedom", "Illusions"]
def add_exclamation_list_compre(words):
    return [word + "!" for word in words]

print("add_exclamation_list_compre method", add_exclamation_list_compre(words))
def add_exclamation_built_in(words):
    # return [ word.join(["!"]) for word in words]
    return words.join("!")
print("add_exclamation_built_in .join() method", add_exclamation_built_in(words))
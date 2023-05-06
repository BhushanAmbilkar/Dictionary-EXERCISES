# Exercise 5: Create a dictionary by extracting the keys from a given dictionary

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.


# Given dictionary:
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]

# Show Hint
# Iterate the mentioned keys using a loop
# Next, check if the current key is present in the dictionary, if it is present, add it to the new dictionary

# Solution 1: Dictionary Comprehension

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }

keys = ["name", "salary"]

newDict = {k: sampleDict[k] for k in keys}
print(newDict)


# Solution 2: Using the update() method and loop

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)

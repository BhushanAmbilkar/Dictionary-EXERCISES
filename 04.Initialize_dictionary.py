# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Show Hint
# Use the fromkeys() method of dict.

# The fromkeys() method returns a dictionary with the specified keys and the specified value.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])



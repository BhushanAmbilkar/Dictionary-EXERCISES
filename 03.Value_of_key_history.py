# Exercise 3: Print the value of key ‘history’ from the below

# Show Hint
# It is a nested dict. Use the correct chaining of keys to locate the specified key-value pair.

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])

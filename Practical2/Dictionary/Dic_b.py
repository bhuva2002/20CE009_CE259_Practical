# AIM: Write a Python script to merge two Python dictionaries.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

def Merge(dict1, dict2):
    return(dict1.update(dict2))
     

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
 
Merge(dict1, dict2)
 
print(dict1)

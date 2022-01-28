# AIM: Write a Python program to remove an item from a set if it is present in the set.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

def isRemove(element):
    if element in a:
        a.discard(element)
        return a
    else:
        return 'This element does not exist in set'


a = set([1, 2, 3, 4])
print(isRemove(200))

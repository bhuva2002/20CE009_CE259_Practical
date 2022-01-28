# AIM: Write a Python program to sum all the items in a dictionary.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

def returnSum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


dict = {'a': 100, 'b': 200, 'c': 300, 'd': 500}
print("Sum :", returnSum(dict))

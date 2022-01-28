# AIM: Write a Python script to check whether a given key already exists in a dictionary.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x not in d :
        print('Key is not present in the dictionary')
    else:
        print('Key is present in the dictionary')


is_key_present(2)
is_key_present(9)

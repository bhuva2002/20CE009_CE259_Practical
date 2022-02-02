# AIM: You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

a = input()
str='' 

for i in a:
    if i.isalpha(): #check character is alphabetic or not
        if i.isupper(): #check uppercase character 
            str+=i.lower() #convert lowercase and concate in string
        elif i.islower():
            str+=i.upper()
    else:
        str+=i    

print(str)

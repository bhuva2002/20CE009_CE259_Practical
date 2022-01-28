# AIM: Find runner-up from given list
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

n = input() #score of each player
lst = []

lst = [int(score) for score in input().split()]

if len(lst)==int(n): #check given input is correct or not
    lst.sort() #list sorting
    lst.reverse() #reverse list

    i=0
    while lst[i]==lst[i+1]: #find runner-up score
        i=i+1

    print(lst[i+1]) #print runner-up score
else:
    print("Please enter valid input")

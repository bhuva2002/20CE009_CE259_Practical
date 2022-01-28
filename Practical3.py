# AIM: Find Captain Room Number
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

n = input() #total room
lst = []

lst = [int(RoomNo) for RoomNo in input().split()] #room no for each player

length = len(lst)
for i in range(length): #traverse in list
    if lst.count(lst[i])==1: 
        print(lst[i])
        exit
        

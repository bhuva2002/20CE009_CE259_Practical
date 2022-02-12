# AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If thereare odd number of characters in the string, we ignore the middle character and check for lapindrome.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

n=int(input())
lst=[]

for i in range(n):
    b = input()
    lst.append(b)

for i in lst:
    l=len(i)
    
    if l%2==0:
        a=i[:int(l/2)]
        b=i[int((l/2)):]
    else:
        a=i[:int(l/2)]
        b=i[int((l/2)+1):]

    
    a=sorted(a)
    b=sorted(b)
    if a==b:
        print("YES")
    else:
        print("NO")

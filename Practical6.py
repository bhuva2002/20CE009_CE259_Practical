# AIM: You are given n words. Some words may repeat. For each word, output its number of occurences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

a = int(input())
arr = []
for i in range(a):
    b = input()
    arr.append(b)
set1 = set(arr)
print(len(set1))

arr2 = []
arr3 = []
for i in arr:
    if i in arr2:
        pass
    else:
        arr2.append(i)
        arr3.append(arr.count(i))

for j in arr3:
    print(j, end=' ')

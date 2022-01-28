# AIM: Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Name: Yash Bhuva 
# Id: 20CE009 
# Github Repository Link: https://github.com/bhuva2002/20CE009_CE259_Practical

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dict4 = {}
for i in (dic1, dic2, dic3):
    # print('i', i)
    dict4.update(i)
print(dict4)

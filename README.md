# 20CE009_CE259_Practical

1) Introduction to Python Programming. Installation & Configuration of Python.Along with its all major editors, IDLE, Pycharm, Anaconda, Jupyter, Interpreter etc.

2) Dictionary
    a. Write a Python script to check whether a given key already exists in a dictionary.
    b. Write a Python script to merge two Python dictionaries.
    c. Write a Python program to sum all the items in a dictionary.
    d. Write a Python script to add a key to a dictionary.
    Sample Dictionary : {0: 10, 1: 20}
    Expected Result : {0: 10, 1: 20, 2: 30}
    e. Write a Python script to concatenate following dictionaries to create a new one.
    Sample Dictionary :
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
   Tuple
    a. Write a Python program to create a tuple with different data types.
    b. Write a Python program to create a tuple with numbers and print one item.
    c. Write a Python program to add an item in a tuple.
    d. Write a Python program to convert a tuple to a string.
    e. Write a Python program to find the length of a tuple.
   Set
    a. Write a Python program to add member(s) in a set and clear a set
    b. Write a Python program to remove an item from a set if it is present in the set.
    c. Write a Python program to create an intersection, Union, difference of sets.
    d. Write a Python program to find maximum and the minimum value in a set.
    e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

3) Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms. One fine day, a finite number of tourists come to stay at the      hotel.
   The tourists consist of:
   → A Captain.
   → An unknown group of families consisting K of members per group where K ≠ 1.
   The Captain was given a separate room, and the rest were given one room per group. Mr. Anant has an unordered list of randomly arranged room entries. The list          consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room. Mr. Anant needs you to help him    find the Captain's room number. The total number of tourists or the total number of groups of families is not known to you. You only know the value of K and the        room number list.
   Input Format:
    The first line consists of an integer, K , the size of each group.
    The second line contains the unordered elements of the room number list.
   Constraints: 1< K<1000
   Output Format: Output the Captain's room number.
   Sample Input
   5
   1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
   Sample Output
   8
   Explanation: The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families. In the given list, all of the numbers repeat 5 times      except for room number 8.Hence, 8 is the Captain's room number.

4) Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and      find the score of the runner-up.
   Input Format: The first line contains. The second line contains an array A[] ofn integers each separated by a space.
   Constraints:
      𝟐 ≤ 𝒏 ≤ 𝟏𝟎
      −𝟏𝟎𝟎 ≤ 𝑨[𝒊] ≤ 𝟏𝟎𝟎
   Output Format: Print the runner-up score.
   Sample Input
   5
   2 3 6 6 5
   Sample Output 
   5
   Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
  
5) You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
   For Example:
   Www.HackerRank.com → wWW.hACKERrANK.COM
   Pythonist 2 → pYTHONIST 2 
   Function Description
     Complete the swap_case function in the editor below.swap_case has the following parameters:
       string s: the string to modify
     Returns
       string: the modified string
   Input Format: A single line containing a string s.
   Constraints: 0 < 𝑙𝑒𝑛(𝑠) ≤ 1000
   Sample Input: HackerRank.com presents "Pythonist 2".
   Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

6) You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance    of the word. See the sample input/output for clarification.
   Note: Each input line ends with a "\n" character.
   Constraints:1 ≤ 𝑛 ≤ 105
   The sum of the lengths of all the words do not exceed 106
   All the words are composed of lowercase English letters only.
   Input Format
     The first line contains the integer n.
     The next n lines each contain a word.
   Output Format
     Output 2 lines.
     On the first line, output the number of distinct words from the input.
     On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
   Sample Input
   4
   bcdef
   abcdefg
   bcde
   bcdef
   Sample Output
   3
   2 1 1
   Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of      the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

7) Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd    number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves gaand ga have      the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves          contain  the same characters but their frequencies do not match.Your task is simple. Given a string, you need to tell if it is a lapindrome.
   Input:
     First line of input contains a single integer T, the number of test cases.
     Each test is a single line containing a string S composed of only lowercase English alphabet.
   Output:
     For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.
   Constraints:
     1 ≤ T ≤ 100
     2 ≤ |S| ≤ 1000, where |S| denotes the length of S
   Example:
    Input:
    6
    gaga
    abcde
    rotor
    xyzxy
    abbaab
    ababc
    Output:
    YES
    NO
    YES
    YES
    NO
    NO

8) Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

9) Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those     representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

10) Generate PDF file of your 3rd Semester Mark-sheet

'''
Rahul is learning about letters and their frequencies in words. He wants to know how many times each letter appears in a given word. Write a Python program to help Rahul find the frequency of each letter in the word.
The first line contains a single string word (the word to analyze).
The word will contain only lowercase English letters.
1≤length of word≤1000.
Print the frequency of each letter in the word in alphabetical order. Each line should contain the letter followed by its frequency.
hello


e 1
h 1
l 2
o 1
'''

word = input().strip()
words_list = []
dict = {}

for i in word:
    # print(i)
    words_list.append(i)

if 1 <= len(words_list) <= 100:
    words_list.sort()
    for i in range(0, len(words_list)):
        freq = words_list.count(words_list[i])
        dict[words_list[i]] = freq

    for i, j in dict.items():
        print(i,j)
else:
    print("Invalid Input")




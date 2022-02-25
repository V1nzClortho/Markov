# Python program to generate Markov Quote using quotes from TV Sitcom "The Office"
# Scott Cornman 2022


import pandas as pd
import math
import re
import random
import json

# import numpy as np

# def isFloat(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False
schrute = pd.read_csv("schrute.csv")

#filter for only michael, dwight quotes
michael = schrute.loc[schrute.character == "Michael"]
# dwigt = schrute.loc[schrute.character == "Dwight"]
#print(michael.head())
#print(dwigt.head())


numRows = len(michael.index)

#michael_words = [""]
michael_words = michael['text'].tolist()
#print(michael_words[0:2])

#start data manipulation of Michael Scott quotes
word_index = []
sentences = [""]


wordIndex = [] 

# #create list of every word [0:n words]
# for i in range(0, len(word_index)):
#     for j in range(0, len(word_index[i])):
#         if word_index[i][j] and word_index[i][j] != " " and word_index[i][j] != '.':
#             wordIndex.append(word_index[i][j])



startWords = []
endWords = []


#check for NaN in michael_words
# for quote in michael_words:
#     if isFloat(quote):
#         print("Error, NaN: ", quote)
#     else:
#         continue

#create list of end words
for quote in michael_words:
    for word in str(quote).split():
        if word.endswith(".") and not "..." in word:
            endWords.append(word)
        elif word.endswith("?"):
            endWords.append(word)
        elif word.endswith("!"):
            endWords.append(word)
        
    
#Create lists for Start words
index = 0
for quote in michael_words:
    if str(quote).split()[index]:
        if str(quote).split()[index] != '.' and not "..." in str(quote).split()[index]:
            startWords.append(str(quote).split()[index])
            #print(str(quote).split()[index])
        
# Create dict of all words
dictWords = {}
word_index= []
for quote in michael_words:
    for word in str(quote).split():
        word_index.append(word)



for n, word in enumerate(word_index):
    #print(dictWords)
    if word in dictWords.keys():
        dictWords[word].append(word_index[n + 1])
    #print(word)
    # if not word in endWords:
    #     dictWords.setdefault(word, []).append(word_index[word_index.index(word) + 1])
        #dictWords[word].append(word_index[word_index.index(word) + 1])
    elif not word in endWords:
        dictWords[word] = [word_index[n + 1]]

for word in dictWords.keys():
    if len(dictWords[word]) < 3:
        dictWords[word].append("...")


        





def markovScotch():
    runNum = 0
    start1 = random.choice(startWords)
    while start1 in endWords:
        start1 = random.choice(startWords)
    # if start1 == " ":
    #     print("Error, blank space")
    # else:
    #     print(start1)

    my_quote = ""
    my_quote += start1
    i_word = start1
    tempWord = start1

    while (i_word not in endWords) or (runNum < 6):
        
        #print(runNum)
       
        

        i_word = random.choice(dictWords[i_word])
        # while len(dictWords[i_word]) < 3:
        #     i_word = random.choice(dictWords[tempWord])
        #     print(i_word)         
            

        if runNum < 6:
            while (i_word in endWords):
                # print(i_word)
                # print(tempWord)
                i_word = random.choice(dictWords[tempWord])
                
        my_quote += " "
        my_quote += i_word
        runNum += 1
        tempWord = str(i_word)

    print(my_quote)

    

for i in range(10):
    markovScotch()







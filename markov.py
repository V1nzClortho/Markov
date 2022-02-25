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

#filter for only michael, quotes
michael = schrute.loc[schrute.character == "Michael"]



numRows = len(michael.index)
michael_words = michael['text'].tolist()


#start data manipulation of Michael Scott quotes
word_index = []
sentences = [""]
wordIndex = [] 
startWords = []
endWords = []

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
        
        
# Create list of all words
dictWords = {}
word_index= []
for quote in michael_words:
    for word in str(quote).split():
        word_index.append(word)


#build dictionary of all words with their succeeding words
for n, word in enumerate(word_index):
    if word in dictWords.keys():
        dictWords[word].append(word_index[n + 1])
    elif not word in endWords:
        dictWords[word] = [word_index[n + 1]]

for word in dictWords.keys():
    if len(dictWords[word]) < 3:
        dictWords[word].append("...")

#build Markov quote
def markovScotch():
    runNum = 0
    start1 = random.choice(startWords)
    while start1 in endWords:
        start1 = random.choice(startWords)
    
    my_quote = ""
    my_quote += start1
    i_word = start1
    tempWord = start1

    while (i_word not in endWords) or (runNum < 6):
        
        i_word = random.choice(dictWords[i_word])
        
        if runNum < 6:
            while (i_word in endWords):
                i_word = random.choice(dictWords[tempWord])
                
        my_quote += " "
        my_quote += i_word
        runNum += 1
        tempWord = str(i_word)

    print(my_quote)

    
#run quote generator n times
for i in range(10):
    markovScotch()







#THIS FILE WILL NOT EXECUTE, THIS IS SIMPLY AN ARCHIVE FOR WRITTEN BUT NO LONGER NEEDED BLOCKS OF CODE FOR MARKOV.PY

## This was a function that was to scan input text character by character and separate it into a list called sentences. Obsolete due to discovery of capability of .split() function in python
## function had unsolved logic error that wouldn't append ? or ! to end of words
#index = 0
# for i in range(0, len(michael_words)):
#     for j in range(0, len(str(michael_words[i]))-1):
#         if(isFloat(michael_words[i])):
#             print()
#             #index += 1
#             #sentences += [""]
#             continue
#         else:
#             if michael_words[i][j] == '.' and michael_words[i][j+1] != '.': 
#                 if michael_words[i][j] == '?' or michael_words[i][j] == "!" or michael_words[i][j] == '.':
#                     sentences[index] = sentences[index] + michael_words[i][j]
#                     index += 1
#                     sentences += [""]
#                     continue
#             try:
#                 if michael_words[i][j] == '.' and michael_words[i][j+1] == '.' and michael_words[i][j+2] == '.':
#                     sentences[index] = sentences[index] + "..."
#                     #j += 1
#                     continue
#             except IndexError:
#                 continue
#             else:
#                 #print(index, i, j)
#                 sentences[index] = sentences[index] + michael_words[i][j]
#                 #print(sentences[i])
#     index += 1
#     sentences += [""]
#############################################################################################
# #create list with one sentence per index value
# for i in range(0, len(sentences)):
#     if(not isFloat(sentences[i]) and sentences[i]):
#         word_index.append(sentences[i].split())

################################################################################################
# for i in range(0, len(word_index)):
#     if word_index[i]:
#         if word_index[i][0] != '.':
#             startWords.append(word_index[i][0])
#         if word_index[i][-1] != '.':
#             endWords.append(word_index[i][-1])
#         #print(endWords[i])

#build dictionary of words
for i in range(0, len(word_index)):
    for j in range(0, len(word_index[i])-1):
        if word_index[i][j] in midWords.keys():
            midWords[word_index[i][j]].append(word_index[i][j+1])
        else:
            midWords[word_index[i][j]] = [word_index[i][j+1]]

            #Create dict of all words
for i in range(0, len(word_index)):
    for j in range(0, len(word_index[i])-1):
        if word_index[i][j] in midWords.keys():
            midWords[word_index[i][j]].append(word_index[i][j+1])
        else:
            midWords[word_index[i][j]] = [word_index[i][j+1]]
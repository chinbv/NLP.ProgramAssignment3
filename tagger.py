# -*- coding: utf-8 -*-
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
#####
##### Brandon Chin
##### Tuesday, February 19th, 2019
##### CMSC 416 - Natural Language Processing
##### Programming Assignment 2 - Ngram Modeling
#####
##### 1. The Problem
##### Design and implement a Python3 program called ngram.py, that will learn an N-gram language model from an arbitrary number of plain text files.
##### The program should generate a given number of sentences based on that N-gram model.
#####
##### 2. Example Input/Output
#####
##### [Input] python ngram.py 3 10 theMenofBoru.Jack.A.Nelson.txt theOsbornes.E.F.Benson.txt blackIvory.R.M.Ballantyne.txt
##### [Output] Command line settings: ngram.py n = 3 m = 10
##### [Output] Sentence number #1:
##### [Output] bradley has another map.
##### [Output] Sentence number #2:
##### [Output] harold agreed with you about things of far greater import , had got some nice thick pieces of raw flesh , so plausible through its naturalness , that he's in the slavemarket of zanzibar.
##### [Output] Sentence number #3:
##### [Output] white ivory do come from the source of american power and the rich tropical foliage of that distressing species.
##### [Output] Sentence number #4:
##### [Output] 'twere better to enjoy a picture , i don't mind if i am over things like that.
##### [Output] Sentence number #5:
##### [Output] today she could see that , whenever he had acted on no secret and mysterious tips from the bush and poured a small antelope , which soon reduced them to go through.
##### [Output] Sentence number #6:
##### [Output] down in a style that has been out : savages have no money , and campequipage into bundles of a carter's horse , and mopped his streaming forehead with a band of manganja men and the awful cruelties that goes the pace of thatlor’ ,
#####          my dear sir , don't be a woman short at dinner and giving a little to doan' sole hisself to him had come down , ” claude turned to harold and his flesh was deeply lacerated by the slavers.
##### [Output] Sentence number #7:
##### [Output] d'ye think it right to a thing in a day on the chiefnot very heavily , and reptiles , all that in this one defeat to get in return is this consistent.
##### [Output] Sentence number #8:
##### [Output] providence , however , turned the corrugated building into a coil which hung down their backs and limbs.
##### [Output] Sentence number #9:
##### [Output] contrast them with an appetite that was biondinetti all over , ” it required no gifts of perception whatever to their satisfaction , as they pleased.
##### [Output] Sentence number #10:
##### [Output] “but claude , and wherever you put on.
#####
##### 3. Algorithm
#####
##### #1. Read the arguments from the command line to determine number of sentences (m) using the specified size ngram (n) and the text files to build your corpus
#####
##### #2. Break each word/punctuation into a token, removing certain punctuations and record the frequency of each token, also inserting <start> at the
#####     beginning of the sentence, and <end> at the end of a sentence (ending punctuation)
#####
##### #3. With frequency recorded, generate probabilities for the words that appear after the word that you are currently on
#####
##### #4. Build the sentences based on the probabilities and a random generated number to help you choose the following word, thereby building the sentence
#####
##### #5. Continue until reaching an ending punctuation, which should end the sentence, and then begin building a new sentence
#####
##### #6. Do this for the specified number of sentences (m) using the specified size ngram (n) which is determined in the command line argument
#####
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


import re
import sys
from decimal import Decimal
from random import *
import operator

wordDict = {}

def main():##main method

    # print("This program tags words with POS.")
    # print("Created by Brandon Chin")

    numberOfArgs = len(sys.argv)
    # print "there are " + str(numberOfArgs) + " arguments"
    # if numberOfArgs < 3:
    #     # print "Usage: " + sys.argv[0] + " n m <filenames> where n = number of grams, m = number of sentences"
    #     exit(1)

    # trainingData = sys.argv[1]
    # testData = sys.argv[2]
    numberOfArgs -= 1 # adjust
    argsIndex = 1

    while argsIndex <= numberOfArgs:
        loadFileName = sys.argv[argsIndex]
        # print "opening file " + loadFileName
        f = open(loadFileName,"r")
        contents = f.read()
        f.close()
        # print contents + "\n"
        if argsIndex == 1:
            # print "I got here [1]"
            generate_tokens(contents)
        if argsIndex == 2:
            # print "I got here [2]"
            generate_testTokens(contents)
        # print "argsIndex: " + argsIndex
        argsIndex += 1

    # loadFileName = trainingData
    # print "opening file " + loadFileName
    # f = open(loadFileName,"r")
    # contents = f.read()
    # f.close()
    # # print contents + "\n"
    # generate_tokens(contents)

    # loadFileName = testData
    # print "opening file " + loadFileName
    # f = open(loadFileName,"r")
    # contents = f.read()
    # f.close()
    # print contents + "\n"
    # generate_testTokens(contents)

    # print (generate_sentences(ngramDict))



    # counts = dict()

#Dealing with the test file tokens
def generate_testTokens(s):
    # s = s.replace('[', '',)
    # s = s.replace(' [ ', '',)
    # s = s.replace(']', '',)
    # s = s.replace(' ] ', '',)

    # Replace new lines with spaces
    s = re.sub(r'\s+', ' ', s)

    # Break sentence into the tokens, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    for i in range(len(tokens)):
        #print "Tokens {}: {}".format(i+1, tokens[i])
        currToken = tokens[i]

        punct = ['!',',','.','?']

        # print "CurrToken: " + currToken + "\n"

        # wordDictCheck = wordDict.get(currToken, None)

        # print "wordDictCheck: " + str(wordDictCheck)

        # if wordDictCheck == "None":
        #     print "Did not exist in wordDict"
        #     generate_frequencies(currToken, "NN", wordDict)
        #     print "should have inserted it"


        def openBracket():
            print "[",

        def closeBracket():
            print "]"

        def default():
            #print "default:"
            resultingPOS = wordDict.get(currToken,None)
            # print "resultingPOS: " + str(resultingPOS)
            theMaxPOS = findMostFrequent(resultingPOS)
            # print "theMaxPOS: " + str(theMaxPOS)
            # for i in punct:
            #     # print i
            #     if theMaxPOS == i:
            #         print currToken + "/" + theMaxPOS
            #     else:
            #         print currToken + "/" + theMaxPOS,
            print currToken + "/" + str(theMaxPOS)

        switcher = {
            '[': openBracket,
            ']': closeBracket,
        }

        def switch(currToken):
            #print "I got here [1] " + currToken
            return switcher.get(currToken, default)()

        switch(currToken)

        # if currToken == "]" or currToken == "[":
        #     print "Token was a ]: " + currToken
        #     print "]"
        # if currToken == "[":
        #     print "Token was a [: " + currToken
        #     print "["
        # else:
        #     print "in else statement, currToken " + currToken

            # print "Word: " + currToken + " POS: " + theMaxPOS


    # stringToken = str(tokens)
    # create_tokens(tokens, wordDict)

    # print "stringToken are " + stringToken + "\n"
    # print "firstWord is " + str(firstWord) + "\n"


    # print "Tokens are " + str(tokens) + "\n"

#Find most frequent occurence in posDict
def findMostFrequent(resultingPOS):

    maxPOS = None
    maxFreq = 0

    # print "resultingPOS: " + str(resultingPOS)

    if resultingPOS == None:
        # print "Did not exist in wordDict"
        maxPOS = "NN"
        # print "should have inserted it"

    else:
        for pos,frequency in resultingPOS.items():
            if maxFreq < frequency:
                maxFreq = frequency
                maxPOS = pos
        # print "(inside for loop) maxPOS: " + maxPOS
    # print "(outside for loop) maxPOS: " + maxPOS
    # print "maxPOS: " + maxPOS

    return maxPOS

#Dealing with the training file tokens
def generate_tokens(s):
    # print "loading in contents"
    # Convert to lowercases
    # s = s.lower()

    # Replace all brackets with empty
    s = re.sub("[\[\]]", '', s)

    # Replace new lines with spaces
    s = re.sub(r'\s+', ' ', s)

    # Break sentence into the tokens, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    # stringToken = str(tokens)
    create_tokens(tokens, wordDict)

    # for key,val in wordDict.items():
    #     print key, "=>", val

    # print "stringToken are " + stringToken + "\n"
    # print "firstWord is " + str(firstWord) + "\n"

    # print "Tokens are " + str(tokens) + "\n"



#split the 3 part token into 3 individual parts
def create_tokens(tokens, wordDict):

    # wordToken = [stringToken for stringToken in stringToken.split('/') if stringToken !=""]
    # posToken = [stringToken for stringToken in stringToken.split('/') if stringToken !=""]
    # print tokens

    for i in range(len(tokens)):
        # print "Tokens {}: {}".format(i+1, tokens[i])
        currToken = tokens[i]
        # print "currToken: " + currToken
        splitTokens = currToken.split('/')
        # if currToken == '[':
        #     print "token is " + currToken
        # if currToken == ']':
        #     print "token is " + currToken
        # else:
        # print "splitTokens are " + str(splitTokens) + "\n"

        wordToken = splitTokens[0]

        posToken = splitTokens[1]


        generate_frequencies(wordToken, posToken, wordDict)

        # for word in wordDict:
        #     print "wordDict contains " + word + "\n"

        # print "wordToken is " + str(wordToken) + "\n"
        # print "posToken is " + str(posToken) + "\n"

    # tokenDict.append(wordToken)

    # print "PosToken are " + posToken + "\n"

def generate_frequencies(wordToken, posToken, wordDict):

    if wordToken in wordDict:
                # print "incrementing posDict " + wordToken + " count"
                posDict = wordDict[wordToken]
                if posDict is not None:
                    if posToken in posDict:
                        posDict[posToken] += 1
                    else:
                        posDict[posToken] = 1
                else:
                    posDict = { posToken : 1 }
                    wordDict[wordToken] = posDict
    else:
        # print "adding wordToken " + "|" + wordToken + "|" + " to wordDict"
        posDict = { posToken : 1 }
        wordDict[wordToken] = posDict
        # print ("Buffer after newNgram is added to ngramDict " + " len(lookBackBuffer): " + str(len(lookBackBuffer))
        #     + " ngramSize: " + str(ngramSize))
    # for key,val in wordDict.items():
    #     print key, "=>", val
    # for key,val in posDict.items():
    #     print key, "=>", val
    # findMostFrequent(posDict)


if __name__ == "__main__":
    main()

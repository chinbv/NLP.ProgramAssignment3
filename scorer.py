# -*- coding: utf-8 -*-

## 1. With no additional rules except for most frequent pos
# 84.4396733774% CORRECT
# 15.5603266226% INCORRECT
## 2. Any capital letter means a POS with NNP, and then most frequent pos
# 81.5042939603% CORRECT
# 18.4957060397% INCORRECT
## 3. Any number that is read in is classified as CD, and then most frequent pos
# 85.1981557089% CORRECT
# 14.8018442911% INCORRECT
## 4. Any word that ends in -ly is classified as RB, and then most frequent pos
# 82.8646346614% CORRECT
# 17.1353653386% INCORRECT
## 5. Any word that begins with un- or Un- is classified as JJ, and then most frequent pos
# 83.3327467267% CORRECT
# 16.6672532733% INCORRECT

import re
import sys
from decimal import Decimal
from random import *
import operator
from fractions import Fraction

keyTokenDict = {}

def main():##main method

    # print("This program tags words with POS.")
    # print("Created by Brandon Chin")

    numberOfArgs = len(sys.argv)
    numberOfArgs -= 1 # adjust
    argsIndex = 1
    fTestFile = None
    fKeyFile = None

    # while argsIndex <= numberOfArgs:
    #     loadFileName = sys.argv[argsIndex]
    #     # print "opening file " + loadFileName
    #     # f = open(loadFileName,"r")
    #     # contents = f.read()
    #     # f.close()
    #     # print contents + "\n"
    #     fTestFile = sys.argv[1]
    #     fKeyFile = sys.argv[2]
    #     print "fTestFile: " + str(fTestFile)
    #     print "fKeyFile: " + str(fKeyFile)
    #     argsIndex += 1

    fTestFile = sys.argv[1]
    fKeyFile = sys.argv[2]
    # print "fTestFile: " + str(fTestFile)
    # print "fKeyFile: " + str(fKeyFile)

    with open(fTestFile) as fT1:
        with open(fKeyFile) as fK1:
            contestTest = fT1.read()
            contentsKey = fK1.read()
            testTokens = generate_tokens(contestTest)
            keyTokens = generate_tokens(contentsKey)
        fT1.close()
        fK1.close()

    # for i in testTokens:
    #     for j in keyTokens:
    #         if i == j:
    #             print "Matched: " + str(i) + " " + str(j)
    #         else:
    #             print "Did not match: " + str(i) + " " + str(j)

    correctCount = 0
    incorrectCount = 0
    totalCount = 0

    for i in range(len(testTokens)):
        keyTokensValue = keyTokens[i]
        keyTokensValue = keyTokensValue.replace("\/", "")
        testTokensValue = testTokens[i]
        testTokensValue = testTokensValue.replace("\/", "")
        if testTokensValue == keyTokensValue:
            # print "It matched " + str(testTokensValue) + " " + str(keyTokensValue)
            testSplitTokens = testTokensValue.split('/')
            testPosToken = testSplitTokens[1]
            # print "testPosToken: " + testPosToken

            # if keyTokensValue[1] == '/':
            #     testingToken0 = keyTokensValue[0]
            #     testingToken2 = keyTokensValue[2]
            #
            #     print "testingToken0: " + testingToken0 + " testingToken2: " + testingToken2

            keySplitTokens = keyTokensValue.split('/')
            keyPosToken = keySplitTokens[1]

            # print "keyPosToken: " + keyPosToken

            correctCount += 1

            generate_confusion_matrix(keyTokenDict,testPosToken,keyPosToken)

        else:
            # print "Did not match " + str(testTokens[i]) + " " + str(keyTokensValue)
            testSplitTokens = testTokensValue.split('/')
            testPosToken = testSplitTokens[1]

            # print "testPosToken: " + testPosToken


            keySplitTokens = keyTokensValue.split('/')
            keyPosToken = keySplitTokens[1]

            # print "keyPosToken: " + keyPosToken

            incorrectCount += 1

            generate_confusion_matrix(keyTokenDict,testPosToken,keyPosToken)

    totalCount = correctCount + incorrectCount

    fractionCorrect = Fraction(correctCount,totalCount)
    fractionIncorrect = Fraction(incorrectCount,totalCount)

    # print "Correct: " + str(fractionCorrect)
    # print "Incorrect: " + str(fractionIncorrect)

    print str(float(fractionCorrect)*100) + "% CORRECT"
    print str(float(fractionIncorrect)*100) + "% INCORRECT"

    for keyToken in keyTokenDict:
        #for testToken in testTokenDict:
        for testToken in keyTokenDict.get(keyToken):
            print str(keyToken) + " " + str(testToken) + " " + str(keyTokenDict.get(keyToken).get(testToken))
        # print len(keyTokenDict.get(keyToken))
    # print len(keyTokenDict)

    # for key,val in keyTokenDict.items():
    #     print key, "=>", val

    # fileKey = open(fKeyFile)
#Dealing with the removing excess from key

def generate_confusion_matrix(keyTokenDict,testPosToken,keyPosToken):
    if keyPosToken in keyTokenDict:
                testTokenDict = keyTokenDict[keyPosToken]
                if testTokenDict is not None:
                    if testPosToken in testTokenDict:
                        testTokenDict[testPosToken] += 1
                    else:
                        testTokenDict[testPosToken] = 1
                else:
                    testTokenDict = { testPosToken : 1 }
                    keyTokenDict[keyPosToken] = testTokenDict
    else:
        testTokenDict = { testPosToken : 1 }
        keyTokenDict[keyPosToken] = testTokenDict


def generate_tokens(s):
    # print "loading in contents"
    # Convert to lowercases
    # s = s.lower()
    s = re.sub("[\[\]]", '', s)

    # Replace new lines with spaces
    s = re.sub(r'\s+', ' ', s)

    # Break sentence into the tokens, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    stringToken = str(tokens)
    # print "tokens are: " + stringToken + "\n"

    return tokens

if __name__ == "__main__":
    main()

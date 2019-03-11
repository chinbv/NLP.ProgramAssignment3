# -*- coding: utf-8 -*-

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
            print "It matched " + str(testTokensValue) + " " + str(keyTokensValue)
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
            print "Did not match " + str(testTokens[i]) + " " + str(keyTokensValue)
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

    for keyToken in keyTokenDict:
        for testToken in testTokenDict:
            print keyTokenDict.get(keyToken,testToken)


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

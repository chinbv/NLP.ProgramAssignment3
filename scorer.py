# -*- coding: utf-8 -*-

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
    print "fTestFile: " + str(fTestFile)
    print "fKeyFile: " + str(fKeyFile)

    with open(fTestFile) as fT1:
        with open(fKeyFile) as fK1:
            generate_tokens(fT1)

    # fileTest = open(fTestFile)
    # fileKey = open(fKeyFile)
#Dealing with the removing excess from key

def generate_tokens(s):
    # print "loading in contents"
    # Convert to lowercases
    # s = s.lower()
    s = s.replace('[', '',)
    s = s.replace(' [ ', '',)
    s = s.replace(']', '',)
    s = s.replace(' ] ', '',)

    # Replace new lines with spaces
    s = re.sub(r'\s+', ' ', s)

    # Break sentence into the tokens, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    stringToken = str(tokens)
    print "tokens are: " + stringToken + "\n"

    return tokens

if __name__ == "__main__":
    main()

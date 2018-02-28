#!/usr/bin/python3

# Modules
import os
import sys
#-------------------------------

def main(argv):
    collected = []  # all sub strings
    word = input()
    print(word)
    prev = 0       # index of last split
    for i in range(len(word)):
        if word[i] == '.':
            subword = word[prev:i]
            prev = i
            collected.append(subword)
    for i in collected:
        print(i)
#-------------------------------

if __name__ == '__main__':
    main(sys.argv)

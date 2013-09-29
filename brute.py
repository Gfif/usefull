#!/usr/bin/python
import string

class wordIt:
    def __init__(self, letters, length):
        self.letters = letters
        self.word = ""
        self.length = length

    def next(self):
        if self.word == "":
            self.word = self.letters[0] * self.length
            return self.word
        k = -1
        for i in range(len(self.word)):
            if self.word[i] != self.letters[-1]:
                k = i
        if k == -1:
            raise StopIteration
        else:
            self.word = self.word[ : k]+ self.letters[self.letters.find(self.word[k]) + 1]
            self.word += self.letters[0] * (self.length - len(self.word))
            return self.word
        

    def __iter__(self):
        return self

for i in range(8):
    for s in wordIt(string.letters, i + 1):
        print(s)
    

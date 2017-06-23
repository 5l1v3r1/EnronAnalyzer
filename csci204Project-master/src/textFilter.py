"""
This class will filter the information inside a Document
and return a filtered (SAME) Document.
"""

from document import *
from sentence import *


class TextFilter:
    """
    Applies a list of filter to a document and returns same filtered Document
    """

    def __init__(self, filterList=None, doc=None):
        self.__filterList = filterList
        self.__doc = doc

    def setFilterList(self, filterList):
        self.__filterList = filterList

    def setDoc(self, doc):
        self.__doc = doc

    def apply(self, doc=None):
        """
        doc is the Document we are applying each filter in the filterlist to
        Calls each filter in filterList in order
        """
        for filt in self.__filterList:
            filt(self)

    def normalizeWhiteSpace(self):
        """
        Makes it so there is only one space in between words
        """
        
        # Create a list of the words with split
        # Add each to a new string with a space at the end
        # Remove the last space and create new sentence to replace original
        for i in range (self.__doc.getSCount()):
            string = self.__doc[i].getSString()
            wordList = string.split()
            newString = ''
            for word in wordList:
                newString += word + ' '
            newSent = Sentence(newString[0:len(newString)-1])
            self.__doc[i] = newSent
            

    def normalizeCase(self):
        """
        Chances all words to lowercase
        """
        for i in range (self.__doc.getSCount()):
            self.__doc[i] = Sentence(self.__doc[i].getSString().lower())
    
    def stripNull(self):
        """
        Removes all characters that are not alphanumeric or a digit
        """
        index = 0
        for i in range (self.__doc.getSCount()):
            string = self.__doc[i].getSString()
            wordList = string.split()
            newString = ''
            for word in wordList:
                newWord = word
                # Goes through each letter in word backwards, adds to new word
                # if alpha or digit
                for i in range(len(word)-1, -1, -1):
                    if not (word[i].isalpha() or word[i].isdigit()):
                        newWord = word[0 : i] + word[i + 1 : len(word)]
                newString += newWord + ' '
            self.__doc[index] = Sentence(newString[0:len(newString)-1])
            index += 1

    def stripNumbers(self):
        """
        Removes all numbers from a document
        """
        index = 0
        for i in range (self.__doc.getSCount()):
            string = self.__doc[i].getSString()
            wordList = string.split()
            newString = ''
            for word in wordList:
                newWord = word
                # Goes through each letter in word backwards, creates new word
                # excluding any indices that represent numbers
                for i in range(len(word)-1, -1, -1):
                    if word[i].isdigit():
                        newWord = newWord[0 : i] + newWord[i + 1 : len(newWord)]
                newString += newWord + ' '
            newSent = Sentence(newString[0:len(newString)-1])
            self.__doc[index] = newSent
            index += 1

    def stripFiles(self):
        """
        Removes all words that are in a file from a document
        Precondition: wordfile folder is in the root folder
        """
        stripFile = open('wordfile/README.md', 'r')
        stripList =[]
        lines = stripFile.readlines()
        # Creates a list of words from each line in file
        for line in lines:
            stripList.extend(line.split())
        stripFile.close()
        
        # If a word in a sentence is in the list, the word gets removed
        for i in range (self.__doc.getSCount()):
            string = self.__doc[i].getSString()
            wordList = string.split()
            for word in stripList:
                while word in wordList:
                    wordList.remove(word)
            newString = ''
            for word in wordList:
                newString += word + ' '
            newSent = Sentence(newString[0:len(newString)-1])
            self.__doc[i] = newSent



def testTestFilter():
    """
    Put your test for the filter class here
    """
    filterList = [TextFilter.normalizeWhiteSpace, TextFilter.normalizeCase, TextFilter.stripNull,
                  TextFilter.stripNumbers]
    sent1 = Sentence("This    IS a bad.sentence")
    sent2 = Sentence("YEs-    It really  is")
    sent3 = Sentence("Has any1 used nu3mb3rs yet?")
    testDoc = Document([sent1, sent2, sent3])
    testFilter = TextFilter(filterList, testDoc)
    testFilter.apply()
    for sent in testDoc:
        print(sent.getSString())


if __name__ == "__main__":
    testTestFilter()






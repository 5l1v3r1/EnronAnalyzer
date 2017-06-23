"""
Class that will contain a document (Basic unit -- "Primary Data-Structure)
"""

from util import *
from sentence import *
import datetime
from stats import *


class Document:
    
    def __init__(self, sentences = [None], toInfo = None, fromInfo = None, date=None):
        self.__sentences = sentences
        self.__sCount = len(sentences) #Number of sentences
        self.__toInfo = toInfo #Who was the document to
        self.__fromInfo = fromInfo #Who was the document from
        self.__date = date
        self.__fwd = False
        self.__reply = False


    def __getitem__(self, index):
        return self.__sentences[index]

    def __setitem__(self, index, value):
        self.__sentences[index] = value

    def getSCount(self):
        #fill me (we should not have to ever set sCount)
        return self.__sCount

    def setToInfo(self, value):
        #fill me
        self.set__toInfo = value

    def getToInfo(self):
        #fill me
        return self.__toInfo

    def setFromInfo(self, value):
        #fill me
        self.__toInfo = value

    def getFromInfo(self):
        #fill me
        return self.__fromInfo
    
    def setDate(self, year, month, day):
        #should use date object in python datetime package
        # mydate = datetime.date(year,month, day)
        #fill me
        self.__date = datetime.date(year, month, day)
        
    def getDate(self):
        # converts datetime to string
        # returns year,month,day
        date = str(self.__date)
        return int(date[0:4]), int(date[5:7]), int(date[8:10])


    def setFwd(self, value):
        #fill me 
        self.__fwd = value

    def getFwd(self):
        #fill me
        return self.__fwd

    def setReply(self,value):
        #fill me
        self.__reply = value
    
    def getReply(self):
        #fill me 
        return self.__reply
        
    def topBottomExist(self):
        # Checks to make sure there are 10 words in the document
        # Called in skTree.py
        wordList = []
        for sentence in self.__sentences:
            wordList.extend(sentence.getSString().split())
        if len(wordList) < 10:
            return False
        else:
            return True
  
    """
    Used to test your Document Class
    """

if __name__ == "__main__":
    testDocument()





    

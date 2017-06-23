"""
Will be used to make a decision tree using sklearn
More details will be added to this later
"""

import math
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from document import *

def buildLists(documentList):
    """
    buildLists is outside of the SKTree class, and takes in a list of documents.
    From the list, it creates a 2d List of lists of length 7 which store the
    data that will be compared. It also creates a 1d length that stores the sender
    of each document such that we can train based on this data. Finally, it stores
    names in a dictionary so the program can compare names as numbers.
    """
    twoDList = [None]*len(documentList)
    fromList = [None] * len(documentList)
    nameIndex = 0
    nameDic = {}
    docIndex = 0
    
    for document in documentList:
        dataList = [None] * 7
        
        # Calculate Julian Date
        year, month, day = document.getDate()
        dataList[0] = int(367*year - (7*(year+((month+9)/12))/4) - (3*(((year+(month-9)/7)/100)+1)/4) + (275*month/9) + day + 1721028.5)
        
        # Get to info, store to map
        if document.getToInfo() not in nameDic.keys():  
            nameDic[document.getToInfo()] = nameIndex
            dataList[1] = nameIndex
            nameIndex += 1
        else:
            dataList[1] = nameDic[document.getToInfo()] 
           
        # Get from info, store to yData
        if document.getFromInfo() not in nameDic.keys():
            nameDic[document.getFromInfo()] = nameIndex
            fromList[docIndex] = nameIndex
            nameIndex += 1
        else:
            fromList[docIndex] = nameDic[document.getFromInfo()]
        
        # Check if email was a forward or reply
        if document.getFwd():
            dataList[2] = 1
        else:
            dataList[2] = 0          
        if document.getReply():
            dataList[3] = 1
        else:
            dataList[3] = 0 
            
        # Get wordcount of document
        numWords = 0
        for sent in document:
            numWords += sent.getWCount()
        dataList[4] = numWords
        
        # Check to see if there are 10 words in the document
        # If so, top/bottom exits
        if document.topBottomExist():
            dataList[5] = 1
            dataList[6] = 1
        else:
            dataList[5] = 0
            dataList[6] = 0
            
        twoDList[docIndex] = dataList
        docIndex += 1 
        
    return twoDList, fromList, nameDic, 

class SKTree:
    
    def __init__(self, documentList):
        """
        Initiates instance variables by calling buildLists
        """
        self.twoDList, self.fromList, self.nameDic = buildLists(documentList)
        self.tree = None

        
    def train(self, maxDepth = 5000):
        """
        Building the tree based on initial training docs
        """
        self.tree = DecisionTreeClassifier(criterion="entropy", max_depth = maxDepth, random_state=0)
        self.tree = self.tree.fit(self.twoDList, self.fromList)

    
    def evaluate(self, evalDocs):
        """
        Evaluating the unknown documents based on the tree built in train.
        Also inverts our dictionary that we got in the constructor to
        get a list of names instead of a list of numbers.
        """
        twoD, oneD, unknownDic = buildLists(evalDocs)
        oneD = [0] * len(evalDocs)
        oneD = self.tree.predict(twoD, oneD)
        fromPredictions = [None] * len(oneD)
        
        # Create new dic with inverted keys
        invDic = {num: name for name, num in self.nameDic.items()}
        # Convert numbers to names
        for i in range(len(oneD)):
            fromPredictions[i] = invDic[oneD[i]]
        return fromPredictions

def testSKTree():
    """
    Used to test my SKTree
    """
    pass

if __name__ == "__main__":
    testSKTree()

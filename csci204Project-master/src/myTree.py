"""
This is the file that contains your dicision tree
"""

import math
import random

class DTreeNode:
    """
    Your Node Class for your dicision tree
    """
    
    def __init__(self, key, data = None, edges = []):
        """
        I am allowing these to be public to manipulate them easy
        """
        self.key = key
        self.data = data
        self.edges = edges
        



class MyDecisionTree:
    """
    Will contain your decision tree algorithm
    """
    
    def __init__(self):
        self.__myRoot = None
        self.__maxHeight = -1
        self.__minHeight = -1


    def train(self, xData, yData, maxDepth):
        """
        External interface for building the tree
        Calls recursive build method
        """
        self.__myRoot = __recursiveBuild(self, xData, yData, 0, maxDepth)


    def evaluate(self, xData):
        """
        External interface for evaluating the tree (Predicting)
        
        I asked for advice on this but still have no idea how to implement,
        I feel like we never really went over how to implement the walk
        or use the tree we built. I understand that we have to continuously keep
        splitting to get lists that match up with the tree, but I am still
        unsure of how to actually write this.
        
        """

    def __recursiveBuild(self, xData, yData, currentDepth, maxDepth):
        """
        Recursively build tree for based on training files
        Algorithm given to us in checkpoint was slightly modified
        """
        if len(xData[0]) == 1:
            dataList = [None] * len(xData)
            for i in range(len(xData)):
                dataList[i] = xData[i][0]
            return DTreeNode(0, dataList)
        elif currentDepth == maxDepth:
            return DTreeNode(None)
        else:
            entropyList = [None] * len(xData[0])
            for i in range(len(xData[0])):
                entropyList[i] = self.calculateEntropy(xData, i)[1]
            
            # Find min in list
            min = entropyList[0]
            mini = 0
            for i in range(len(entropyList)):
                if entropyList[i] < min:
                    mini = i
            # Create list from min entropy column
            minData = [None] * len(xData)
            for i in range(len(xData)):
                minData[i] = xData[i][mini] 
                
            nodeRef = DTreeNode(i, minData)
            twoDLists = self.split2DList(xData, mini)
            for twoD in twoDLists:
                for i in range(len(twoD)):
                    returnedRef = self.__recursiveBuild(twoD, yData, currentDepth + 1, maxDepth)
                    nodeRef.edges.append(returnedRef)
            return nodeRef
            
    def calculateEntropy(self, twoDList, column):
        """
        Calculates the entropy of a given column in a two dimensional list.
        First gets all values in column, then finds num occurences of any given
        value. Finally, uses entropy equation to calculate entropy.
        """
        entropyList = [None]*len(twoDList)
        occurences = [None]*len(twoDList)
        
        #Create list from column
        for i in range(len(twoDList)):
            entropyList[i] = twoDList[i][column]
            occurences[i] = -1
        
        # Count occurences of each number
        i = 0
        while i < len(entropyList):
            occurences[i] = entropyList.count(entropyList[i])
            # Delete other occurences
            n = i + 1
            while n < len(entropyList):
                if entropyList[n] == entropyList[i]:
                    del entropyList[n]
                else:
                    n += 1
            i += 1
                
        # Remove extra values
        while -1 in occurences:
            occurences.remove(-1)
        
        # Calculate Entropy
        entropy = 0
        for num in occurences:
            p = num/len(twoDList)
            entropy -= p*math.log(p, 2)
            
        return entropyList, entropy
    

    def split2DList(self, twoDList, column):
        """
        split2dList ssplits a twoDList into n twoDLists, where n is the number
        of unique values in the given column. Returns a 3d list of 2d lists.
        """
        # Create list from column
        columnList = [None]*len(twoDList)
        for i in range(len(twoDList)):
            columnList[i] = twoDList[i][column]
            
        # Find unique values in column 
        uniqueValuesList = []     
        for i in columnList:
            if i not in uniqueValuesList:
                uniqueValuesList.append(i)
                
        # Create 3d List of 2d Lists, one for each unique value in column           
        numVals = len(uniqueValuesList)
        listOf2dLists = [None]*numVals
        for index in range(len(listOf2dLists)):
            listOf2dLists[index] = [None] * len(twoDList)
        
        # Fill 3d List 
        for twoList in range(len(uniqueValuesList)):
            rowNumber = 0
            newRow = []
            for row in twoDList:
                if row[column] == uniqueValuesList[twoList]:
                    listOf2dLists[twoList][rowNumber] = newRow
                    for n in range(column):
                        listOf2dLists[twoList][rowNumber].append(row[n])
                    for q in range(column + 1, len(twoDList[0])):
                        listOf2dLists[twoList][rowNumber].append(row[q])
                    newRow = []
                    rowNumber += 1   
        
        # Remove empty rows in each 2d List
        for three in range(len(listOf2dLists)):
            while None in listOf2dLists[three]:
                listOf2dLists[three].remove(None)
       
        return listOf2dLists

def testMyDecisionTree():
    """
    Used for your testing
    """
    twodList = [None] * 5
    
    for i in range(5):
        twodList[i] = [None] * 5
        for n in range(5):
            twodList[i][n] = random.randint(0, 2)
    tree = MyDecisionTree()
    print(tree.calculateEntropy(twodList, 2))
    print(tree.split2DList(twodList, 2))

if __name__ == "__main__":
    testMyDecisionTree()

"""
This class will perform simple stats calcuations on our data
Most of these will be static methods
"""

from sort import *
from heap import *

class Stats:


    def __init__(self):
        pass

    @staticmethod
    def findFreqDic(aList):
        """
        Takes in a list of words, returns a dictionary of words/freq
        """
        freqDic = dict()
        # Adds to dic if not in dic
        # Adds to freq if key in dic
        for i in range (len(aList)):
            if aList[i] not in freqDic:
                freqDic[aList[i]] = 1
            else:
                freqDic[aList[i]] += 1
        return freqDic

    @staticmethod
    def topNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        topDic = dict()
        
        # Finds the maximum occurence in the frequency dic
        # Removes max from freq, adds to top
        # Loops n times
        
        for n in range (n):
            maxFreq = aDic[list(dict.keys(aDic))[0]]
            maxIndex = list(dict.keys(aDic))[0]
            for key in aDic:
                if aDic[key] > maxFreq:
                    maxFreq = aDic[key]
                    maxIndex = key
            topDic[maxIndex] = maxFreq
            del aDic[maxIndex]
            
        return topDic

    @staticmethod
    def bottomNSort(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        minDic = dict()
        
        # Finds the minimum occurence in the frequency dic
        # Removes min from freq, adds to top
        # Loops n times
        
        for n in range (n):
            minFreq = aDic[list(dict.keys(aDic))[0]]
            minIndex = list(dict.keys(aDic))[0]
            for key in aDic:
                if aDic[key] < minFreq:
                    minFreq = aDic[key]
                    minIndex = key
            minDic[minIndex] = minFreq
            del aDic[minIndex]
            
        return minDic


    @staticmethod
    def topNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the highest freq
        """
        pass

    
    @staticmethod
    def bottomNHeap(aDic, n):
        """
        Takes in a dictionary of words/freq (sort the list based on freq)
        Return a dictionary of n  word/freq with the lowest freq
        """
        pass



def testStats():
    """
    Can be used to test methods in the Stats Class
    """
    wordlist = ['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 
                'hello', 'hello', 'word', 'compsci', 'compsci',
                'three', 'three', 'three', 'hello', 'hello',
                'binary']
    tester = Stats()
    freq = tester.findFreqDic(wordlist)
    print(freq)
    print(tester.bottomNSort(freq, 3))
    print(tester.topNSort(freq, 2))


if __name__ == "__main__":
    testStats()

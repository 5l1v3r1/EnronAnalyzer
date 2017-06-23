"""
A primary data-structure.
Document will keep a list of these.
A Sentence is NOT a line.
"""

class Sentence:

    def __init__(self, sString = ""):
        self.__sString = sString[0:len(sString)- 1]
        self.__wCount = -1
        if sString != "":
            self.__endP = sString[len(sString) - 1]
        
    def getWCount(self):
        """
        If found return/else calcuate and return
        """
        if self.__wCount != -1:
            return self.__wCount
        else:
            temp = self.__sString.split()
            self.__wCount = len(temp)
            return self.__wCount

    def getSString(self):
        """
        """
        return self.__sString


    def setSString(self, value):
        """
        """
        self.sString = value

def testSentence():
    """
    Used to test your Sentence class
    """
    pass


if __name__ == "__main__":
    testSentence()

    

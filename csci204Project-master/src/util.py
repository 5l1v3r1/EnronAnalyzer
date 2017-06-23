"""
This file will contain utility classes and functions
"""


class UserInput:
    """
    Class that will keep a record of user inputs
    """
    def __init__(self):
        self.tPath = ""
        self.ePath = ""
        self.__tDocument = [] #A List of training documents
        self.__eDocument = [] #A List of evaluation documents
        self.__textFilter = [] #A List of text filters

    def setTDocument(self, docList):
        self.__tDocument = docList

    def addTDocument(self, doc):
        """
        Add a training document
        """
        pass

    def getTDocument(self):
        """
        Returns the training document list
        """
        return self.__tDocument

    def setEDocument(self, docList):
        self.__eDocument = docList


    def addEDocument(self, doc):
        """
        Add an eval document
        """
        pass
    
    def getEDocument(self):
        """
        Returns the training document list
        """
        return self.__eDocument

    def setTextFilter(self, filt):
        pass
    
    def addTextFilter(self, filt):
        self.__textFilter.append(filt)
    
    def getTextFilter(self):
        return self.__textFilter
        


class TimerStats:
    """
    This class may be used to keep information on performance of your code
    """
    
    def __init__(self):
        pass

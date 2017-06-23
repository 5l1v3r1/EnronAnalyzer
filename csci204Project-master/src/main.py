"""
Main Interface 
Requirements:  matplotlib, numpy, scipy, sci-kit
Recommended to use with anaconda (will have all packages)
"""

import util
import os
from os import *
from os.path import *
from documentReader import *
from stats import *
from plot import *
from textFilter import *
from skTree import *

def main():
    """
    Will call main loop of interface
    """
    user_interface()
    
def user_interface():
    """
    Will be used to interact with user
    """

    info = UserInput() #my main structure that holds my execution information

    print("----Welcome to Enron Data Analysis----")
    print("Goals: (1) Who wrote an email (2) Communication Network -- Who talked to who")
    
    # Compile list of training docs
    info.tpath = input("Please enter the filepath for the training data: ")
    emptyList = []
    validFile = False
    while not validFile:
        try:
            print("Loading Training Documents")
            info.setTDocument(listDocuments(info.tpath, emptyList))
        except:
            print("Not a Valid File Path")
            info.tpath = input("Please enter the filepath for the training data: ")
        else:
            validFile = True  
            print('Success!')
    
    # Compile list of eval docs
    info.epath = input("Please enter the filepath for the unknown data: " ) 
    emptyList = []      
    validFile = False
    while not validFile:
        try:
            print("Loading Eval Documents")
            info.setEDocument(listDocuments(info.epath, emptyList))
        except:
            print("Not a Valid File Path")
            info.epath = input("Please enter the filepath for the unknown data: " ) 
        else:
            validFile = True
            print('Success!')
    
    topMenu(info)
      

def listDocuments(path, carrylist):
    """
    listDocuments is adapted from a CSCI204 lab. It recursively checks the path,
    analyzes if it is a file or a folder, and operates accordingly. Prints any
    exception that it comes across.
    """
    dirName = os.path.basename(path)
    for f in os.listdir( path ):
        if f[len(f) - 1] == '/':
            f = f[0:len(f)-1]
        if f[0] == '.':
            continue
        v = os.path.join( path, f )
        if os.path.isfile( v ):
            try:
                reader = DocumentReader(v)
                carrylist.append( reader.readFile() )
            except Exception as e: 
                print(e)
                print(v + " could not be read.")
        elif os.path.isdir( v ):
            listDocuments( v, carrylist )
    return carrylist
   
        
def topMenu(info):
    """
    topMenu is the main interface the user has with the program. It allows us to
    call any of the functions we have written, and will continue to come back to
    the menu until the user quits.
    """
    
    print("Enter Selection")
    print("1. Add Text Filter")
    print("2. Apply Text Filter")
    print("3. Topic Analyis of Train")
    print("4. Topic Analyis of Eval")
    print("5. Find Unknown From")
    print("6. Restart program")
    print("-1 to exit")
    t = int(input("Enter: "))
    if t == 1:
        addTextFilter(info)
    elif t == 2:
        applyTextFilter(info)
    elif t == 3:
        topicAnalysisTrain(info)
    elif t == 4:
        topicAnalysisEval(info)
    
    # Allows user to choose between custom or Scikit tree
    elif t == 5:
        print("1. Scikit-Learn")
        print("2. Custom Tree")
        a = int(input("Enter: "))
        if a == 1:
            findUnKnownFromSK(info)
        elif a == 2:
            print('Warning - Method Unfinished)')
            findUnKnownFromMY(info)
    elif t == 6:
        user_interface()
        t = -1
    elif t != -1:
        print("Invalid Selection")
    
    # Ends program if t == -1
    if t != -1:
        topMenu(info)
    
    
def addTextFilter(info):
    """
    Add information about which text filters to use, see TextFilter class for details
    """
    print("Choose from the following filters by typing the numbers of your choices, \
          separated by commas.")
    print("1: normalizeWhiteSpace")
    print("2: normalizeCase")
    print("3: stripNull")
    print("4: stripNumbers")
    print("5: stripFile")
    uinput = input("Choices: ")
    filterDic = {"1": TextFilter.normalizeWhiteSpace, "2": TextFilter.normalizeCase, "3": TextFilter.stripNull,
                  "4": TextFilter.stripNumbers, "5": TextFilter.stripFiles}
    for i in uinput:
        if i.isdigit() and int(i) <= 5:
            info.addTextFilter(filterDic[i])

def applyTextFilter(info):
    """
    Apply the text filter to both the training and eval Document Lists
    """
    tDoc = info.getTDocument()
    eDoc = info.getEDocument()
    for doc in tDoc:
        trainFilter = TextFilter(info.getTextFilter(), doc)
        trainFilter.apply()
    info.setTDocument(tDoc)
    for doc in eDoc:
        evalFilter = TextFilter(info.getTextFilter(), doc)
        evalFilter.apply()
    info.setEDocument(eDoc)
        

def topicAnalysisTrain(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    # Create objects for stats and plot classes
    counter = Stats()
    plotter = MyPlot()
    
    # Requests top number of words from user
    num = input("How many words are you looking for? " )
    while not num.isdigit():
        num = input("Please input a valid number: " )
    number = int(num)
    
    # Gets list of words of all documents in training docs
    wordList = []
    for doc in info.getTDocument():
        for sentence in doc:
            wordList.extend( sentence.getSString().split() )
            
    # Creates frequency dic and then dic of the top n words in that fdic
    fdic = counter.findFreqDic( wordList )
    try:
        tdic = counter.topNSort(fdic, number)
    except:
        print("Too few words to generate list")
    else:
        xLabels = [None] * number
        xList = [None] * number
        yList = [None] * number
        i = 0
        for x in tdic:
            xLabels[i] = x
            xList[i] = i
            yList[i] = tdic[x]
            i += 1
        plotter.twoDBar(xList, yList, xLabels, num)
        

def topicAnalysisEval(info):
    """
    We will analyze topics based on words in the email
    We will prompt the user for how many topics "words" they are looking for
    After we will find this information and plot it using our Plot class
    """
    # Create objects for stats and plot classes
    counter = Stats()
    plotter = MyPlot()
    
    # Requests top number of words from user
    num = input("How many words are you looking for? " )
    while not num.isdigit():
        num = input("Please input a valid number: " )
    number = int(num)
    
    # Gets list of words of all documents in eval docs
    wordList = []
    for doc in info.getEDocument():
        for sentence in doc:
            wordList.extend( sentence.getSString().split() )
            
    # Creates frequency dic and then dic of the top n words in that fdic
    fdic = counter.findFreqDic( wordList )
    try:
        tdic = counter.topNSort(fdic, number)
    except:
        print("Too few words to generate list")
    else:
        xLabels = [None] * number
        xList = [None] * number
        yList = [None] * number
        i = 0
        for x in tdic:
            xLabels[i] = x
            xList[i] = i
            yList[i] = tdic[x]
            i += 1
        plotter.twoDBar(xList, yList, xLabels, num)

def findUnKnownFromSK(info):
    """
    This implements SKTree from skTree.py
    """
    tDocs = info.getTDocument()
    tree = SKTree(tDocs)
    tree.train()
    eDocs = info.getEDocument()
    # Prints list of names of which document was sent by whom
    # List aligns with order of eDocs
    print(tree.evaluate(eDocs))

def findUnKnownFromMY(info):
    """
    This implements our custom tree from myTree.py
    Since our tree is not finished, we simply tell the user it is not ready
    and implement our working tree.
    """
    print('Our custom tree is not ready- we will use SKTree instead')
    findUnKnownFromSK(info)

def findUnKnownTo(info):
    """
    Had we implemented this, we simply would just rewrite our SKTree
    to have the yData be To information, and run the same algorithm.
    """
    pass


def buildNetwork(info):
    """
    To be added (may or maynot get)
    """
    print("To be added")
    return None


if __name__ == "__main__":
    main()

"""
Class used to read a document.
Each document will be product by one instance of a DocumentReader

IF DATA IS MISSING, will be noted at ??? in the file 
"""

#Will be used when we find an exceptions
from userExceptions import *
#All documents contain multiple sentences
from sentence import *
#Will produce a document
from document import *
import datetime
import os.path


class DocumentReader:
    """
    Used to read in a document
    """
    
    def __init__(self, fname = ""):
        self.__fname = fname
        self.__fileRef = None #Will store the reference to file when open

    
    def getFName(self):
        return self.__fname

    
    def __openFile(self):
        """
        Private function used to open the file and test if it exists
        """

        if os.path.isfile( self.getFName() ):
            fd = os.open( self.getFName(), os.O_RDWR|os.O_CREAT )
            self.__fileRef = os.fdopen(fd, "w+")
            return True
        else:
            return False
    
    def readFile(self):
        """
        Will open (if not already open)/read the file
        Make a Document and return
        If any Error, throws error
        Format of file is MIME EMAIL
        """
        escapeList = ["Message-ID:", "Date:", "From:", "To:", "Subject:", "Mime-Version:",
                      "Content-Type:", "Content-Transfer-Encoding:", "X-From:", "X-To:",
                      "X-cc:", "X-bcc:", "X-Folder:", "X-Origin:", "X-FileName:"]
        
        result = self.__openFile()
        if result:
            
            lineList = self.__fileRef.read().splitlines()
            text = ""
            beginIrrelevant = False
            hasPassedFilename = False
            toEmail = ""
            for i in lineList:
                
                # Get name of sender
                if i[0:9] == "X-Folder:":
                    
                    letterCounter = 11
                    firstName = ""
                    lastName = ""
                    
                    while i[letterCounter] != '_':
                        firstName += i[letterCounter]
                        letterCounter += 1
                        
                    letterCounter += 1
                    while i[letterCounter] != '_':
                        lastName += i[letterCounter]
                        letterCounter += 1
                        
                    fromEmail = firstName + " " + lastName    
                
                # Get name of recipient
                elif i[0:3] == "To:":
                    try:
                        endIndex = i.index(",")
                    except:
                        endIndex = len(i)
                    toEmail = i[4:endIndex]
                   
                # Get date sent
                elif i[0:5] == "Date:" and not hasPassedFilename:
                    day = i[11:13]
                    if day[1] == " ":
                        monthIndex = 13
                    else:
                        monthIndex = 14
                    month = i[monthIndex:monthIndex + 3]
                    year = i[monthIndex + 4: monthIndex + 9]
                
                # Checks to see if we have reached message body
                elif i[0:11] == "X-FileName:":
                    hasPassedFilename = True
                
                # Skips past forwarded/replied message
                else:
                    
                    count = 0
                    if beginIrrelevant:
                        break
                    
                    for word in escapeList:
                        if word in i[0:len(word)]:
                            count += 1
                        if "----------------------" in i \
                            or "-----Original Message-----" in i:
                            beginIrrelevant = True
                            break
                        
                    if count == 0 and hasPassedFilename:
                        text += i
            
            # Creates list of sentence objects
            sentences = []
            punctuation = [".", "?", "!"]
            startIndex = 0
            for i in range (len(text)):
                if text[i] in punctuation:
                    sentences.append(Sentence(text[startIndex : i + 1]))
                    startIndex = i + 1 
            if len(sentences) == 0:
                sentences.append(Sentence(text))
                
            # if no toEmail was found, we list it as UNKNOWN
            if toEmail == "":
                toEmail = 'UNKNOWN'
                
            # Translates month to number
            mts = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                   'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
            month = mts[month]
            
            # Converts date to datetime
            date = datetime.date(int(year), month, int(day))
            
            newDocument = Document(sentences, toEmail, fromEmail, date)
            return newDocument
        else:
            print("Invalid file")
                        
    def checkFileFormat(self):
        """
        Will open the file (if not already open)
        Will test if it is a correctly formatted MIME EMAIL
        """
        
        formatList = ["Message-ID:", "Date:", "From:", "To:", "Subject:", "Mime-Version:",
                      "Content-Type:", "Content-Transfer-Encoding:", "X-From:", "X-To:",
                      "X-cc:", "X-bcc:", "X-Folder:", "X-Origin:", "X-FileName:"]
        
        # Checks to make sure file includes all data headings
        result = self.__openFile()
        if result:
            lineList = self.__fileRef.read().splitlines()
            
            for line in lineList:
                for starter in formatList:
                    if starter in line:
                        formatList.remove(starter)
                        break
            if len(formatList) == 0:
                return True
            else:
                return False
        else:
            return False


def testDocumentReader():
    """
    Used to test your DocumentReader class
    """

    dRead = DocumentReader("train/tana.jones@enron.com/12")

    
    print(dRead.checkFileFormat())
    doc = dRead.readFile()
    print("From: " + doc.getFromInfo())
    print("To: " + doc.getToInfo())
    for i in range (doc.getSCount()):
        print("Sentence: " + doc[i].getSString())
        print("")
        
    
    


if __name__ == "__main__":
    testDocumentReader()

"""
Will you will place your code for a linked-list
"""


class LinkNode:
    
    def __init__(self, key, next=None, prev=None, data=None):
        """
        I will allow the attributes of this class to be public for easy access
        """
        self.key = key
        self.next = next
        self.data = data


class SLinkedList:
    """
    Where you will place your code for a singly linked list
    """
    
    def __init__(self):
        self.__head = None

    
    def add(self, key, sorted = True, data=None):
        pass

    def remove(self, key):
        pass

    def __addSorted(self,key,data=None):
        pass

    def __addUnSorted(self,key,data=None):
        pass

class DLinkLsit:
    """
    Where you will place your code for a doubly linked list
    """

    def __init__(self):
        self.__head = None
        
        
    def add(self, key, sorted = True, data = None):
        pass
    
    def remove(self, key):
        pass

    def __addSorted(self,key,data=None):
        pass
    
    def __addUnSorted(self,key,data=None):
        pass

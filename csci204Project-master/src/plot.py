"""
This file contains objects related to our plotting
"""


import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt



class MyPlot:
    """
    This class will be used for all plotting.
    In most cases, the functions will just be static
    However, this allows for on nice interface
    """

    def __init__(self):
        """
        constructor
        """
        pass


    @staticmethod
    def twoDScatter(xList, yList, xLabels=None, yLabels=None):

        area = len(xList)*len(yList)
        plt.scatter(xList, yList)
        plt.xticks(range(len(xList)), xLabels, size='small')
        plt.show()


    @staticmethod
    def twoDBar(xList, yList, xLabels=None, number = '?', yLabels=None ):
        """
        Creates bar graph with a label of how many words are listed
        and what word each bar represents
        """
        
        fig, ax = plt.subplots()
        width = .8

        # Adds top label if applicable
        if number != '?':
            ax.set_title('Top ' + number + ' Words')
            
        # Creates bar graph with labels
        ax.bar(xList, yList, width)
        ax.set_xticks(np.arange(len(xList)) + width/2)
        ax.set_xticklabels(xLabels)
        ax.set_ylabel('Occurences')
        plt.show()
        




def testMyPlot():
    """
    Used to test MyPlot class
    """
    xList = [0,3,4,5]
    xLabels = ["one", "two", "three", "four", "five"]
    yList = [1, 2, 3, 4]
    plotter = MyPlot()
    plotter.twoDBar(xList, yList, xLabels)


if __name__ == "__main__":
    testMyPlot()



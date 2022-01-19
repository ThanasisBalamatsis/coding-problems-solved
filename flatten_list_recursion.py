# The following problem was solved in the context of
# MIT's online course "6.00.1x Introduction to Computer Science and
# Programming Using Python"

# THE PROBLEM
# Write a function to flatten a list. 
# The list contains other lists, strings, or ints.
# For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened 
# into [1,'a','cat',2,3,'dog',4,5] (order matters).

# SOLUTION'S DESCRIPTION
# The problem was solved recursively. The "if" statement makes use of
# "isFlattened" function which checks whether a list is flattened at
# first degree. If the condition is true, then it is the base case and the fully 
# flattened list is returned. Otherwise, the function returns itself taking
# as parameter a list that is flattened at first degree by the "makeItFlattened" function.
# This process is running repeatedly until the initial list is fully flattened.    

def flatten(theList):
    # define function that checks whether the list is flattened at first degree
    def isFlattened(listToBeChecked):
        for i in listToBeChecked:
            
            if type(i) == list:
                return False
            
        return True
    
    # define function that flattens a list at first degree
    def makeItFlattened(listToBeFlattened):
        # A "for" loop checks every element of the list.
        # Elements that are not lists are appended to the newly created flattenedList.
        # If an element is a list, then its elements are appended in linear order to the flattenedList
        # through another "for" loop.
        flattenedList = []
        for i in range(len(listToBeFlattened)):
            
            if type(listToBeFlattened[i]) == list:
                for k in listToBeFlattened[i]:
                    flattenedList.append(k)
            elif type(listToBeFlattened[i]) != list:
                flattenedList.append(listToBeFlattened[i])
                
        return flattenedList
    
    #business logic
    if isFlattened(theList) == True:
        return theList
    else:
        return flatten(makeItFlattened(theList))
    
        


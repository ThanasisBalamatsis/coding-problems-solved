# The following problem was solved on Codewars

# THE PROBLEM
# For a given string s find the character c (or C) with longest consecutive repetition and return:

# Tuple<char?, int>(c, l)where l (or L) is the length of the repetition. 
# If there are two or more characters with the same l return the first in order of appearance.

# For empty string return:

# Tuple<char?, int>(null, 0)

# SOLUTION'S DESCRIPTION
# Assume the first character is the longest consecutive part
# Iterate over the chars string and compare tempLength to the maxLength. 
# If tempLength is greater than maxLength then assign tempLength to maxLength 

def longest_repetition(chars):
    
    if len(chars) == 0:
        return ('', 0)
    
    tempLength = 1
    maxLength = 1
    longestPart = chars[0]
    
    for i in range(1,len(chars)):
        
        if chars[i] == chars[i-1]:
            tempLength += 1
        else:
            if tempLength > maxLength:
                longestPart = chars[i-1]
                maxLength = tempLength
                tempLength = 1
            tempLength = 1
            
        if i + 1 == len(chars):
            
            if tempLength > maxLength:
                longestPart = chars[i-1]
                maxLength = tempLength
                
    return (longestPart, maxLength)
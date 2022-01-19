# The following problem was solved on Codewars

# THE PROBLEM
# What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list. 
# You will be given two inputs a word and an array with words. 
# You should return an array of all the anagrams or an empty array if there are none. 
# For example:

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

# SOLUTION'S DESCRIPTION
# Create nested isAnagram function that checks whether an examined word is an anagram of a word
# Iterate over the list of words and call isAnagram for each word
# Append it to the result if true


def anagrams(word, words):
    result = []
    
    def isAnagram(word, examinedWord):
        if len(word) == len(examinedWord):
            charsListOne = list(word)
            charsListTwo = list(examinedWord)
            if sorted(charsListOne) == sorted(charsListTwo):
                return True
            else:
                return False
        else:
            return False
        
    for examinedWord in words:
        if isAnagram(word, examinedWord):
            result.append(examinedWord)
            
    return result

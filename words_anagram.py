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
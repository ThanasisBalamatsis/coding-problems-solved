# The following problem was solved on Codewars

# THE PROBLEM
# The drawing below gives an idea of how to cut a given "true" rectangle into squares 
#("true" rectangle meaning that the two dimensions are different).

# My note: Assume each cell is a square. Each exploded part is a square as well. 

#        
#     ____ ____ ____ ____ ____
#    |    |    |    |    |    |
#    |    |    |    |    |    |  
#     ____ ____ ____ ____ ____
#    |    |    |    |    |    |
#    |    |    |    |    |    |  
#     ____ ____ ____ ____ ____
#    |    |    |    |    |    |
#    |    |    |    |    |    |  
#     ____ ____ ____ ____ ____
#                          

#        
#     ____ ____ ____          ____ ____
#    |    |    |    |        |    |    |
#    |    |    |    |        |    |    |  
#     ____ ____ ____          ____ ____
#    |    |    |    |        |    |    |
#    |    |    |    |        |    |    |  
#     ____ ____ ____          ____ ____
#    |    |    |    |        
#    |    |    |    |          
#     ____ ____ ____ 
#                             ____      ____
#                            |    |    |    |
#                            |    |    |    |
#                             ____      ____



# Can you translate this drawing into an algorithm?

# You will be given two dimensions

# 1. a positive integer length
# 2. a positive integer width

# You will return a collection or a string with the size of each of the squares.

# Examples in general form:

#  sqInRect(5, 3) should return [3, 2, 1, 1]
#  sqInRect(3, 5) should return [3, 2, 1, 1]

# SOLUTION'S DESCRIPTION
# The solution is based on the concept of Euclidean Algorithm. 
# The smallest possible square in this rectangle is actually the Greatest Common Divisor
# of positive integer length and positive integer width.
# A floor-division, within the recursive algorithm for gcd, gives 
# the dimension of the largest possible square contained within the rectangle.
# A for loop is needed in order to add all 
# the potential squares with minimum possible dimensions contained.

def sqInRect(dimensionOne, dimensionTwo):
    
    def gcdRecur(bigDim, smallDim, result):        
        
        if smallDim == 0:
            return(bigDim)
        else:
            for i in range(bigDim // smallDim):
                result.append(smallDim)
            return(gcdRecur(smallDim, bigDim % smallDim, result))
        
        
    if dimensionOne == dimensionTwo:
           return None
    else:
        bigDim = max(dimensionOne, dimensionTwo)
        smallDim = min(dimensionOne, dimensionTwo)
        result = []
        gcdRecur(bigDim, smallDim, result)
        return result 

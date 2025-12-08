

myListOne = [1,2,4]
myListTwo = myListOne
myListOne = 'chai'    
# >>> myListTwo            
# [1, 2, 4]
myListOne = [1,2,4]   
# >>> myListTwo             
# [1, 2, 4]

myListOne[0] = 44
# >>> myListOne          
# [44, 2, 4]
# >>> myListTwo         
# [1, 2, 4]

h1 = [1,2,4]
h2 = h1[:]   
# >>> h1
# [1, 2, 4]
# >>> h2   
# [1, 2, 4]
h1[0] = 55  
# >>> h1
# [55, 2, 4]
# >>> h2    
# [1, 2, 4]

import copy  
h2 = copy.copy(h1)
h2 = copy.deepcopy(h1) 

m = [1,2,4]
n = m
# m == n
# True
# >>> m is n
# True
m = [1,2,4]
# >>> m == n
# True
# >>> m is n 
# False


# -*- coding:utf8 -*-
'''
Created on 4 de Jun de 2012

@author: Miguel
'''

class Knot(object):
    X_D = 1      #X dimension
    Y_D = 2      #Y dimension
    Z_D = 3      #Z dimension
    T_D = 4      #T "Time" dimension (representative of 4th dimension)
    NIL = Knot() #Empty Knot
    
    '''
    classdocs
    '''
    def __init__():
        '''
        Constructor
        '''
        self.key = []
        self.value = "None"
        self.parent     = None
        self.left       = None 
        self.right      = None
        self.dimension  = 0
        pass
    
    def __init__(key, parent, left, right, dimension):
        '''
        Constructor
        '''
        self.key = key
        self.parent     = parent
        self.left       = left 
        self.right      = right
        self.dimension  = dimension
        pass
    
    def __str__(self):
        return str(self.key) + " <" + str(self.dimension) + "D>: ( " + str(self.parent.key) + \
            ", " + str(self.left.key) + ", " + str(self.left.key) + ")"
    pass #Class
        
# -*- coding:utf-8 -*-
'''
Created on June 4th, 2012

@author: Miguel Rodrigues, 5959
'''

class Node():
    '''
    classdocs
    '''

    #Constants    
    IND_D = -1      # Indeterminate dimension or depth
    X_D   =  1      # X dimension
    Y_D   =  2      # Y dimension
    Z_D   =  3      # Z dimension
    T_D   =  4      # T "Time" dimension (representative of 4th dimension)
    
    def __init__(self, key = [0], value = "", parent = None, left = None, \
                 right = None, k = IND_D, depth = IND_D):
        '''
        Constructor
        '''
        self.key        = key       # Key List
        self.value      = value     # Node Value
        self.parent     = parent    # Parent Node
        self.left       = left      # Left Node
        self.right      = right     # Right Node
        self.k          = k         # 'K' dimension
        self.depth      = depth     # Node depth
        pass
    
    def __str__(self):
        return str(self.key) + " <" + str(self.k) + "D>: '" + self.value + "' ( " + str(self.parent.key) + \
            ", " + str(self.left.key) + ", " + str(self.right.key) + ")"


    def compareKeys(self, keyToCompare):
        if self.k > 1:
            selectedKey = (self.depth + 1)  % self.k
        else:
            selectedKey = 0
        if self.key[selectedKey] < keyToCompare[selectedKey]:    # smaller
            return -1
        elif self.key[selectedKey] > keyToCompare[selectedKey]:  # bigger
            return 1
        else:                                                 # same key
            return 0
        pass
    pass #Class
NIL = Node([0], "NIL") # Empty "NIL" Node

class Tree(object):
    '''
    classdocs
    '''

    def __init__(self, root, k):
        '''
        Constructor
        '''
        if root == None:
            self.root = NIL
        else:
            self.root = root
            self.root.depth = 1
            self.root.k = k
            self.root.parent = NIL
            self.root.left = NIL
            self.root.right = NIL
            
            pass
        pass
    
    def insert(self, z):
        z.left = NIL
        z.parent = NIL
        z.right = NIL
        
        y = NIL
        x = self.root
        while x != NIL: #Explores the tree until it reach the bottom.
            y = x
            if x.compareKeys(z.key) > 0: 
                x = x.left
            else:
                x = x.right
                pass
            pass
        z.parent = y
        if y == NIL:
            self.root = z # Tree was Empty
        elif y.compareKeys(z.key) > 0:
            y.left = z
        else:
            y.right = z
            pass
        z.depth = y.depth + 1
        z.k = y.k
        pass
    
    def sort(self):
        
        pass
    
    def search(self, x, k): #TEST
        if x == self.nil or x.compareKeys(k) == 0:
            return x
        if x.compareKeys(k) > 0:
            return self.search(x.left, k)
        else:
            return self.search(x.right, k)

    def minimum(self, x): #RAW
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x): #RAW
        while x.right != self.nil:
            x = x.right
        return x

    def sucessor(self, x): #RAW
        if x.right != self.nil:
            return self.minimum(x.right)
        y = x.parent
        while y != self.nil and x == y.right:
            x = y
            y = y.parent
        return y

    def transplant(self, u, v): #RAW
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != self.nil:
            v.parent = u.parent

    def delete(self, z): #RAW
        if z.left == self.nil:
            self.transplant(z, z.right)
        elif z.right == self.nil:
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def inorder_walk(self, x, lista): #RAW
        if x != self.nil:
            self.inorder_walk(x.left, lista)
            lista.append( x )
            self.inorder_walk(x.right, lista)
    
    pass #class
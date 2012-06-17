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
    X_D = 1      # X dimension
    Y_D = 2      # Y dimension
    Z_D = 3      # Z dimension
    T_D = 4      # T "Time" dimension (representative of 4th dimension)
    
    def __init__(self, key=[0], value="", parent=None, left=None, \
                 right=None, k=IND_D, depth=IND_D):
        '''
        Constructor
        '''
        self.key = key       # Key List
        self.value = value     # Node Value
        self.parent = parent    # Parent Node
        self.left = left      # Left Node
        self.right = right     # Right Node
        self.k = k         # 'K' dimension
        self.depth = depth     # Node depth
        pass
    
    def __str__(self):
        if self.left == None:
            left = "None"
        elif self.left == NIL:
            left = "NIL"
        else:
            left = self.left.key
        if self.right == None:
            right = "None"
        elif self.right == NIL:
            right = "NIL"
        else:
            right = self.right.key
        if self.parent == None:
            parent = "None"
        elif self.parent == NIL:
            parent = "NIL"
        else:
            parent = self.parent.key
            
        return str(self.key) + " <" + str(self.k) + "D>: '" + self.value + "' ( " + str(parent) + \
            ", " + str(left) + ", " + str(right) + ")"


    def compareKeys(self, keyToCompare):
        if self.k > 1:
            selectedKey = (self.depth + 1) % self.k
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
    
    def search(self, k, x=None):
        if k == NIL: #If k is NIL then doesn't worth to search it 
            return k
        elif x == None: #Set Root as default search
            x = self.root
        if x == NIL or x.key == k.key:
            return x
        if x.compareKeys(k.key) > 0:
            return self.search(k, x.left)
        else:
            return self.search(k, x.right)

    def minimum(self, x = None):
        if x == None:
            x = self
        while x.left != NIL:
            x = x.left
        return x

    def maximum(self, x):
        if x == None:
            x = self
        while x.right != NIL:
            x = x.right
        return x

    def sucessor(self, x):
        if x == NIL:
            return NIL
        if x.right != NIL:
            return self.minimum(x.right)
        y = x.parent
        while y != NIL and x == y.right:
            x = y
            y = y.parent
        return y
    
    def inorder_walk(self, x=None, nodeList = []): #TEST
        if x == None:
            x = self
        if x != NIL:
            self.inorder_walk(x.left, nodeList)
            nodeList.append(x)
            self.inorder_walk(x.right, nodeList)
    

    def transplant(self, u, v):
        if u.parent == NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != NIL:
            x = v.parent
            v.parent = u.parent
            u.parent = x
            if v == x.left:
                x.left = u
            else:
                x.right = u

    def delete(self, z): #RAW
        if z.left == NIL:
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

    def sort(self):
        
        pass
    
    pass #class

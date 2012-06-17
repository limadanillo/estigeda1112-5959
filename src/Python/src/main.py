# -*- coding:utf-8 -*-
'''
Escola Superior de Tecnologias e Gestão de Beja - ESTIG
Licenciatura em Engenharia Informática - 9119
Estrura de Dados e Algoritmos - EDA
-----------------------------------
Created on June 13th, 2012
@author: Miguel de Campos Rodrigues - 5959
'''

from kDTree import Tree
from kDTree import Node
import kDTree

UNSUP = "Unsupported / Unimplemented yet"

def main():
    
    #Build nodes
    node1 = Node([3, 1], "a")
    node2 = Node([2, 7], "b")
    node3 = Node([6, 9], "c")
    node4 = Node([2, 2], "d")
    node5 = Node([9, 9], "e")
    node6 = Node([3, 2], "f")
    node7 = Node([8, 4], "g")
    node8 = Node([5, 7], "h")
    node9 = Node([7, 1], "i")
    node10 = Node([1, 3], "j")
    node11 = Node([0, 8], "k")
    node12 = Node([4, 5], "l")
    node13 = Node([7, 9], "m")
    
    #Build Tree
    tree = Tree(node1, 2)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node5)
    tree.insert(node6)
    tree.insert(node7)
    tree.insert(node8)
    tree.insert(node9)
    tree.insert(node10)
    tree.insert(node11)
    tree.insert(node12)
    tree.insert(node13)
    
    #Print Structure 
    print "- Tree Structure ----------"
    print str(tree.root)
    print str(node2)
    print str(node3)
    print str(node4)
    print str(node5)
    print str(node6)
    print str(node7)
    print str(node8)
    print str(node9)
    print str(node10)
    print str(node11)
    print str(node12)
    print str(node13)
    
    
    #Search Node by Key
    print "\n - Search 4 different nodes ----------"
    print "Node11\nS#" + str(node11)
    print "R#" + str(tree.search(node11))
    print "Node12\nS#" + str(node12)
    print "R#" + str(tree.search(node12))
    print "Node9\nS#" + str(node9)
    print "R#" + str(tree.search(node9))
    print "NIL Node\nS#" + str(kDTree.NIL)
    print "R#" + str(tree.search(kDTree.NIL))
    
    #Get Minimum Node
    print "\nMinimum Node:" + str(tree.minimum(tree.root))
    
    #Get Maximum Node
    print "Maximum Node:" + str(tree.maximum(tree.root))
    
    #Get Sucessor Node
    print "Successor Node from Root Node:" + str(tree.sucessor(tree.root))
    print "Successor Node form the Maximum Node: " + str(tree.sucessor(tree.maximum(tree.root)))
    print "Successor Node form the Minimum Node: " + str(tree.sucessor(tree.minimum(tree.root)))
    
    #Get Predecessor Node
    print "Predecessor Node from Node6: " + UNSUP
    print "Predecessor Node from Maximum Node: " + UNSUP
    print "Predecessor Node from Minimum Node: " + UNSUP
    
    #Get In order Walk from Root Node
    print "In order walk from root Node: " + UNSUP
    
    #Transplant Node
    print "Transplant Node3 to Node 6:" + UNSUP
    
    #Remove Node
    print "Remove Node7: " + UNSUP
    
    #Balance Tree (Sort)
    print "Sort / Balance Tree: " + UNSUP
    
    pass

if __name__ == '__main__':
    main()
    pass

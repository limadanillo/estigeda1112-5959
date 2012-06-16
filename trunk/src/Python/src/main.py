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

def main():
    
    node1 = Node([3, 7], "a")
    node2 = Node([8, 1], "b")
    node3 = Node([6 ,6], "c")
    node4 = Node([2, 6], "d")
    node5 = Node([1, 7], "f")
    node6 = Node([8, 6], "g")
    node7 = Node([5, 9], "h")
    
    tree = Tree(node1, 2)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node5)
    tree.insert(node6)
    tree.insert(node7)
    
    print str(tree.root)
    print str(node2)
    print str(node3)
    print str(node4)
    print str(node5)
    print str(node6)
    print str(node7)
    
    pass

if __name__ == '__main__':
    main()
    pass
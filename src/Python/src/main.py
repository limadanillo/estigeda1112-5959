# -*- coding:utf-8 -*-
'''
Escola Superior de Tecnologias e Gestão de Beja - ESTIG
Licenciatura em Engenharia Informática - 9119
Estrura de Dados e Algoritmos - EDA
-----------------------------------
Criado no dia 13 de Junho de 2012
@author: Miguel de Campos Rodrigues - 5959
'''

from kDTree import Tree
from kDTree import Node
import kDTree
import time

UNSUP = "Unsupported / Unimplemented yet"


def main():
    #Inicializa o temporizador
    global startTimer
    startTimer = time.clock()
    global stepTimer
    stepTimer = 0
    
    #Construir nós
    nodes = []
    nodes.append(Node([3, 1], "a"))
    nodes.append(Node([2, 7], "b"))
    nodes.append(Node([6, 9], "c"))
    nodes.append(Node([2, 2], "d"))
    nodes.append(Node([9, 9], "e"))
    nodes.append(Node([3, 2], "f"))
    nodes.append(Node([8, 4], "g"))
    nodes.append(Node([5, 7], "h"))
    nodes.append(Node([7, 1], "i"))
    nodes.append(Node([1, 3], "j"))
    nodes.append(Node([0, 8], "k"))
    nodes.append(Node([4, 5], "l"))
    nodes.append(Node([7, 9], "m"))
    
    #Construir Árvore
    tree = Tree(nodes[0], 2)
    for i in range(1, 13):
        tree.insert(nodes[i])
        
    #Mostrar estrutura 
    print "- Tree Structure ----------"
    for i in range(0, 13):
        print str(i) + ": " + str(nodes[i])
    checkTimer()
    
    #Procurar Nó pela sua chave.
    print "\n - Search 4 different nodes ----------"
    print "Node11\nS#" + str(nodes[11])
    print "R#" + str(tree.search(nodes[11]))
    print "Node12\nS#" + str(nodes[12])
    print "R#" + str(tree.search(nodes[12]))
    print "Node9\nS#" + str(nodes[9])
    print "R#" + str(tree.search(nodes[9]))
    print "NIL Node\nS#" + str(kDTree.NIL)
    print "R#" + str(tree.search(kDTree.NIL))
    checkTimer()
    
    #Nó menor (mais à esquerda)
    print "\nMinimum Node:" + str(tree.minimum(tree.root))
    
    #Nó maior (mais à direita)
    print "Maximum Node:" + str(tree.maximum(tree.root))
    checkTimer()
    
    #Nó sucessor
    print "Successor Node from Root Node:" + str(tree.sucessor(tree.root))
    print "Successor Node form the Maximum Node: " + str(tree.sucessor(tree.maximum(tree.root)))
    print "Successor Node form the Minimum Node: " + str(tree.sucessor(tree.minimum(tree.root)))
    checkTimer()
    
    #Nó predecedor Não implementado
    #print "Predecessor Node from Node6: " + UNSUP
    #print "Predecessor Node from Maximum Node: " + UNSUP
    #print "Predecessor Node from Minimum Node: " + UNSUP
    
    #Listagem de nós ordenada a partir da raiz
    nodelist = list()
    tree.inorder_walk(tree.root, nodelist)
    print "\nIn order walk from root Node:"
    for value in map(lambda value: str(value), nodelist):
        print value
    checkTimer()
    
    #Transplantar Nó
    tree.transplant(nodes[3], nodes[6])
    print "\nTransplant Node3 to Node 6:"
    for i in range(0, 13):
        print str(i) + ": " + str(nodes[i])
    checkTimer()
    
    #Remover nó
    tree.delete(nodes[2])
    print "\nRemove Node2: "
    for i in range(0, 13):
        print str(i) + ": " + str(nodes[i])
    checkTimer()
    
    #Balancear Árvore (Sort)
    print "\nSort / Balance Tree: "
    tree.sort(tree.root, kDTree.NIL, 1)
    for i in range(0, 13):
        print str(i) + ": " + str(nodes[i])
    pass
    checkTimer()
    
    #Procura por Nó mais próximo
    print "\nSearch for Nearest-neighbor of [4, 8]:"
    print str(tree.nearestSearch([4, 8], tree.root))
    checkTimer()
    
def checkTimer():
    global startTimer
    stepTimer = time.clock()
    print "time spent:" + str(stepTimer - startTimer)
    startTimer = time.clock()

#Módulo de main
if __name__ == '__main__':
    main()
    pass
# -*- coding:utf-8 -*-
'''
Created on June 4th, 2012

@author: Miguel Rodrigues, 5959
'''

class Node():
    '''
    Representa um nó de uma Árvore Binária do tipo k-D Tree. 
    Uma k-D Tree serve para organizar dados dentro de um espaço multi-dimensional.
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
        Inicializa uma nova instância de um nó de uma k-D Tree.
        @param key=[0]: A chave o nó. Esta chave tem de ser composta por 'k' números,
                    em que 'k' é o número de dimensões da árvore.
        @param value="": O valor que o nó armazena (opcional).
        @param parent=None: O nó pai (opcional).
        @param left=None: O nó adjacente à esquerda (com chave menor - opcional);
        @param left=None: O nó adjacente à direita (com chave maior ou igual - opcional);
        @param k=IND_D: O número de dimensões da árvore ao qual o nó assenta (opcional);
        @param depth=IND_D: A profundidade do nó na árvore (opcional);
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
        """
        Converte o nó para uma representação em texto.
        @return: Devolve um texto com a seguinte estrutura:
                 ['key'] <'k'D - d:'depth'>: 'value' ('parent.key', 'left.key', 'right.key')
        """
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
            
        return str(self.key) + " <" + str(self.k) + "D - d:" + str(self.depth) + ">: '" + \
            self.value + "' (" + str(parent) + ", " + str(left) + ", " + str(right) + ")"


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
    Representa uma Árvore Binária do tipo k-D Tree. 
    Uma k-D Tree serve para organizar dados dentro de um espaço multi-dimensional.
    '''

    def __init__(self, root, k):
        '''
        Inicializa uma nova instancia de uma árvore binária tipo k-D Tree.
        @param root: o nó que fica como raiz.
        @param k: a dimensão ao qual a árvore trabalha.
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
        """
        Insere um nó na árvore. A sua posição é aplicada automáticamente, dependendo do peso da sua chave.
        @param z: o nó a inserir. É preciso que o nó tenha a mesma dimensão que a árvore.
        """
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
        """
        Procura pelo nó a indicado
        @param x: O nó pelo qual começa a procurar;
        @param k: Um nó com a chave a procutar;
        @return: Um nó da árvore com a chave igual ou 'NIL' se nada encontrar.
        Se x for 'None' então procura a partir da raiz da árvore.
        Se k for 'NIL' então devolve 'NIL'
        
        """
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

    def minimum(self, x=None):
        """
        Devolve o nó mais à esquerda (menor) na árvore.
        @param x: O nó pelo qual começa a procurar;
        @return: Devolve o nó mais à esquerda.
        Se x for 'None' então procura a partir da raiz da árvore.
        """
        if x == None:
            x = self.root
        while x.left != NIL:
            x = x.left
        return x

    def maximum(self, x=None):
        """
        Devolve o nó mais à direita (maior) na árvore.
        @param x: O nó pelo qual começa a procurar;
        @return: Devolve o nó mais à direita.
        Se x for 'None' então procura a partir da raiz da árvore.
        """
        if x == None:
            x = self.root
        while x.right != NIL:
            x = x.right
        return x

    def sucessor(self, x):
        """
        Devolve o nó sucessor relativamente à sua posição.
        @param x: O nó a avaliar;
        @return: Devolve o nó sucessor. NIL se x for NIL ou None.
        """
        if x == NIL or x == None:
            return NIL
        if x.right != NIL:
            return self.minimum(x.right)
        y = x.parent
        while y != NIL and x == y.right:
            x = y
            y = y.parent
        return y
    
    def inorder_walk(self, x=None, nodeList = []): #TEST
        """
        Cria uma lista com todas os nós ordenados de forma sequêncial.
        @param x=None: o nó ao qual começa a ler. Ao manter 'None' utiliza a raiz da árvore por defeito;
        @param nodeList: a lista que recebe os nos nós sequenciados;
        
        """
        if x == None:
            x = self.root
        if x != NIL:
            self.inorder_walk(x.left, nodeList)
            nodeList.append(x)
            self.inorder_walk(x.right, nodeList)
    

    def transplant(self, u, v):
        """
        Transplanta (troca) um nó para outra posição na árvore.
        @param u: o nó que vai ser transplantado;
        @param v: o nó a transplantar;
        Se u.parent for NIL então define v como raiz da árvore.
        """
        if u.parent == NIL:
            self.root = v
            v.depth = 1
        elif u == u.parent.left:
            u.parent.left = v
            v.depth = u.parent.depth + 1
        else:
            u.parent.right = v
            v.depth = u.parent.depth + 1
        if v != NIL:
            x = v.parent
            v.parent = u.parent
            u.parent = x
            u.depth = x.depth + 1
            if v == x.left:
                x.left = u
            else:
                x.right = u

    def delete(self, z):
        '''
        Remove um nó da árvore.
        @param z: O nó a remover. 
        '''
        if z.left == NIL:
            #Se o nó z não tem nó à esquerda então transplanta o direito para cima
            self.transplant(z, z.right)
        elif z.right == NIL:
            #Se o nó z não tem nó à direita então transplanta o esquerdo para cima
            self.transplant(z, z.left)
        else:
            #Se possuir ambos os nós adjacentes então:
            #Obtém o o nó mais pequeno do nó à sua direita.
            y = self.minimum(z.right)
            if y.parent != z:
                
                #Se o nó mais pequeno não for adjacente a z, transplanta-o com nó à sua direita 
                self.transplant(y, y.right)
                
                #define ligação à direita de y 
                y.right = z.right
                y.right.parent = y
                
            #Troca z com y
            self.transplant(z, y)
            
            #Define ligação à esquerda de y
            y.left = z.left
            y.left.parent = y
        
        #Corta o nó z da árvore
        z.parent.right = NIL
        z.left = NIL
        z.right = NIL
        z.parent = NIL
        z.depth = Node.IND_D
        pass

    def sort(self, nodeToSort, parentNode = None, depth=0): #TEST
        '''
        Reordena a árvore de forma a ficar balanceada.
        @param nodeToSort: O nó ou lista a ordenar;
        @param parentNode=None: o nó pai ao qual vai ordenar; Se este nó for NIL,
               define o primeiro nó da lista ou ou como raiz;
        @param depth=0: a profundidade do Nó na arvore; 
        '''
        if nodeToSort == []: #Se não hover mais nós para ordenar então devolve NIL
            return NIL
        
        #cria uma lista e guarda o pai do nó a ordenar
        nodeList = []
        
        #Se o objecto dado for um nó então:
        if (isinstance(nodeToSort, Node)):
            #Obtém todos os nós descendentes de outro nó específico
            self.inorder_walk(nodeToSort, nodeList)
        else:
            #se não, é porque é uma lista de nós
            nodeList = nodeToSort
            
        #Ordena Lista pela dimensão
        nodeList.sort(key=lambda node: node.key[self.getDim(depth)])
        
        #Obtém o nó mediano
        medianNode = self.__getMedian(nodeList, depth)
        nodeList.remove(medianNode)
        #Define o nó mediano como raiz da árvore se o seu pai for NIL
        if parentNode == NIL:
            self.root = medianNode
        medianNode.parent = parentNode
        #Separa a lista de nós (block maior para a direita, e outro menor para a esquerda) 
        leftBlock = [x for x in nodeList if x.key[self.getDim(depth)] < \
                     medianNode.key[self.getDim(depth)]]
        rightBlock = [x for x in nodeList if x.key[self.getDim(depth)] >= \
                      medianNode.key[self.getDim(depth)]]
        
        #Define a profundidade do nó na árvore e os seus nós adjacentes.
        medianNode.depth = depth
        medianNode.left = self.sort(leftBlock, medianNode, depth + 1)
        medianNode.right = self.sort(rightBlock, medianNode, depth + 1)
        
        #Devolve o nó ordenado.
        return medianNode
    
    def __getMedian(self, nodeList, depth):
            #Obtém as chaves na correspondente dimensão em relação à sua profundidade na árvore
            keys = map(lambda value: value.key[self.getDim(depth)], nodeList)
            
            #Calcula a média
            mean = sum(keys) / len(keys)
            
            #Procura o valor mais aproximado da média (nó mediano)
            for i in range(0, len(keys)):
                if keys[i] >= mean:
                    return nodeList[i]
                pass
            pass
    
    def getDim(self, depth):
        
        #Devolve a profundidade da arvore em relação à sua raiz
        return (depth - 1) % self.root.k
    pass #class

# AVL tree implementation in Python


import sys

# Cria a classe do Nodo
class TreeNode(object):
    def __init__(self, chave):
        self.chave = chave
        self.left = None
        self.right = None
        self.height = 1 #Altura do nodo em relação a raiz(1)

#Classe da arvore, onde vao ser feitas as operacoes
class AVLTree(object):

    #Como esta implemetacao nao tem init, o nodo e referenciado na propria area de teste

    # Funcao de inserir o nodo, com parametros: nodo pai e dado(inteiro)
    def insert_node(self, raiz: None or TreeNode, chave: int):

        # Procura o local correto para adicionar o novo nodo (recursiva)

        if raiz == None: #Caso seja o primeiro nodo da arvore ou chegue ponto ideal para ser adicionado, o nodo ira ser adicionado 
            return TreeNode(chave)
        elif chave < raiz.chave: #Caso a chave do novo nodo seja menor que a do nodo raiz, é chamado a funcao novamente com o lado esquerdo do nodo pai 
            raiz.left = self.insert_node(raiz.left, chave)
        else: #Caso a chave do novo nodo seja maior que a do nodo raiz, é chamado a funcao novamente com o lado direito do nodo pai 
            raiz.right = self.insert_node(raiz.right, chave)

        #define a altura do novo nodo
        raiz.height = 1 + max(self.getHeight(raiz.left),
                              self.getHeight(raiz.right))


        # Apos o novo nodo ser adicionado, faz o balanceamento necessario na arvore
        # Nota que como o metodo e recursivo, o balanceamento ira se aplicar em cascata da ultima folha(menos o novo nodo, pois ela para no return) ate a raiz

        balanceFactor = self.getBalance(raiz)
        if balanceFactor > 1: # Caso o fator de balanceamento for maior que 1 e a chave do novo nodo for menor que a esquerda do nodo pai, realiza uma rotacao para direita, chamando o metodo especifico
            if chave < raiz.left.chave:
                return self.rightRotate(raiz)
            else:  
                raiz.left = self.leftRotate(raiz.left)
                return self.rightRotate(raiz)

        # Caso o fator de balanceamento for menor que -1 e a chave do novo nodo for maior que a direita do nodo pai, realiza uma rotacao para esquerda, chamando o metodo especifico
        if balanceFactor < -1:
            if chave > raiz.right.chave:
                return self.leftRotate(raiz)
            else:
                raiz.right = self.rightRotate(raiz.right)
                return self.leftRotate(raiz)

        return raiz

    # Function to delete a node
    def delete_node(self, raiz, chave):

        # Find the node to be deleted and remove it
        if not raiz:
            return raiz
        elif chave < raiz.chave:
            raiz.left = self.delete_node(raiz.left, chave)
        elif chave > raiz.chave:
            raiz.right = self.delete_node(raiz.right, chave)
        else:
            if raiz.left is None:
                temp = raiz.right
                raiz = None
                return temp
            elif raiz.right is None:
                temp = raiz.left
                raiz = None
                return temp
            temp = self.getMinValueNode(raiz.right)
            raiz.chave = temp.chave
            raiz.right = self.delete_node(raiz.right,
                                          temp.chave)
        if raiz is None:
            return raiz

        # Update the balance factor of nodes
        raiz.height = 1 + max(self.getHeight(raiz.left),
                              self.getHeight(raiz.right))

        balanceFactor = self.getBalance(raiz)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(raiz.left) >= 0:
                return self.rightRotate(raiz)
            else:
                raiz.left = self.leftRotate(raiz.left)
                return self.rightRotate(raiz)
        if balanceFactor < -1:
            if self.getBalance(raiz.right) <= 0:
                return self.leftRotate(raiz)
            else:
                raiz.right = self.rightRotate(raiz.right)
                return self.leftRotate(raiz)
        return raiz

    # Function to perform left rotation
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Get the height of the node
    def getHeight(self, raiz):
        if not raiz:
            return 0
        return raiz.height

    # Get balance factore of the node
    def getBalance(self, raiz):
        if not raiz:
            return 0
        return self.getHeight(raiz.left) - self.getHeight(raiz.right)

    def getMinValueNode(self, raiz):
        if raiz is None or raiz.left is None:
            return raiz
        return self.getMinValueNode(raiz.left)

    def preOrder(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.chave), end="")
        self.preOrder(raiz.left)
        self.preOrder(raiz.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.chave)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVLTree()
raiz = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    raiz = myTree.insert_node(raiz, num)
myTree.printHelper(raiz, "", True)
chave = 13
raiz = myTree.delete_node(raiz, chave)
print("After Deletion: ")
myTree.printHelper(raiz, "", True)
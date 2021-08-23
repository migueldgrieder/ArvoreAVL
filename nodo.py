import sys
# Cria a classe do Nodo
class TreeNode(object):
    def __init__(self, chave):
        self.chave = chave
        self.left = None
        self.right = None
        self.height = 1 #Altura do nodo em relação a raiz(1)

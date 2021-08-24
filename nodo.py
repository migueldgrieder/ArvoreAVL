import sys
# Cria a classe do Nodo
class TreeNode(object):
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1 #Altura do nodo em relação a raiz(1)

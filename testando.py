from nodo import Nodo
from arvore_avl import ArvoreAVL

arvore = ArvoreAVL()
arvore.adicionar(5)
print(arvore.raiz.valor)

arvore.adicionar(4)
print(arvore.raiz.esquerda.valor)

arvore.adicionar(6)
print(arvore.raiz.direita.valor)



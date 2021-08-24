
from nodo import Nodo
from arvore_avl import ArvoreAVL

arvore = ArvoreAVL()
arvore.adicionar(5)
print(arvore.raiz.valor)

arvore.adicionar(3)
print(arvore.raiz.esquerda.valor)

arvore.adicionar(6)
print(arvore.raiz.direita.valor)

arvore.adicionar(4)
print(arvore.raiz.esquerda.direita.valor)

print(arvore.buscaPonta(-1).valor) 
print(arvore.busca(7))
print(arvore.busca(4))

arvore.deletar(6)  # Ocorrerá rotação simples, alocando um novo nodo para ser a raiz
print(arvore.raiz.valor)
print(arvore.raiz.esquerda.valor)
print(arvore.raiz.direita.valor)
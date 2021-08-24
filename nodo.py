class Nodo(object): # Sera as folhas e raiz da arvore, objeto unidade da arvore
    def __init__(self,valor):
        self.valor = valor    # Representa o elemento do nodo
        self.esquerda = None  # Representa o galho esquerdo do nodo, inicialmente nenhum, abrigara novos nodos, caso requisitado
        self.direita = None   # Representa o galho direito do nodo, inicialmente nenhum, abrigara novos nodos, caso requisitado
        self.tamanho = 0      # Representa o tamanho atual
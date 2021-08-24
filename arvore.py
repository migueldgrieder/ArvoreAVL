from nodo import TreeNode
import sys
#Classe da arvore, onde vao ser feitas as operacoes
class AVLTree(object):

    #Como esta implemetacao nao tem init, o nodo e referenciado na propria area de teste

    # Funcao de inserir o nodo, com parametros: nodo pai e dado(inteiro)
    def inserir_node(self, raiz: None or TreeNode, chave: int):

        # Procura o local correto para adicionar o novo nodo (recursiva)

        if raiz == None: #Caso seja o primeiro nodo da arvore ou chegue ponto ideal para ser adicionado, o nodo ira ser adicionado 
            return TreeNode(chave)
        elif chave < raiz.chave: #Caso a chave do novo nodo seja menor que a do nodo raiz, é chamado a funcao novamente com o lado esquerdo do nodo pai 
            raiz.esquerda = self.inserir_node(raiz.esquerda, chave)
        else: #Caso a chave do novo nodo seja maior que a do nodo raiz, é chamado a funcao novamente com o lado direito do nodo pai 
            raiz.direita = self.inserir_node(raiz.direita, chave)

        #define a altura do novo nodo
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda),
                              self.getAltura(raiz.direita))


        # Apos o novo nodo ser adicionado, faz o balanceamento necessario na arvore
        # Nota que como o metodo e recursivo, o balanceamento ira se aplicar em cascata da ultima folha(menos o novo nodo, pois ela para no return) ate a raiz

        balanceFator = self.getBalanco(raiz)
        if balanceFator > 1: # Caso o fator de balanceamento for maior que 1 e a chave do novo nodo for menor que a esquerda do nodo pai, realiza uma rotacao para direita, chamando o metodo especifico
            if chave < raiz.esquerda.chave:
                return self.direitaRotacao(raiz)
            else:  
                raiz.esquerda = self.esquerdaRotacao(raiz.esquerda)
                return self.direitaRotacao(raiz)

        # Caso o fator de balanceamento for menor que -1 e a chave do novo nodo for maior que a direita do nodo pai, realiza uma rotacao para esquerda, chamando o metodo especifico
        if balanceFator < -1:
            if chave > raiz.direita.chave:
                return self.esquerdaRotacao(raiz)
            else:
                raiz.direita = self.direitaRotacao(raiz.direita)
                return self.esquerdaRotacao(raiz)

        return raiz

    # Funcao para deletar um nodo da arvore
    def deleta_node(self, raiz, chave): 

        # Realiza uma busca do nodo para deletar e remover da arvore

        if not raiz: # Caso seja o primeiro nodo da arvore
            return raiz
        elif chave < raiz.chave: # Verifica se o nodo é menor do que a raiz esquerda, e caso seja a deleta
            raiz.esquerda = self.deleta_node(raiz.esquerda, chave)
        elif chave > raiz.chave: # Verifica se o nodo é maior do que a raiz direita, e caso seja a deleta
            raiz.direita = self.deleta_node(raiz.direita, chave)
        else: 
            if raiz.esquerda is None:
                temp = raiz.direita
                raiz = None
                return temp
            elif raiz.direita is None:
                temp = raiz.esquerda
                raiz = None
                return temp
            temp = self.getMinValorNode(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.deleta_node(raiz.direita,
                                          temp.chave)
        if raiz is None: # Caso nao exista uma raiz
            return raiz

        # Determina o fator de balanceamento da arvore, verificando se esta balanceada, utilizando-se da altura para tal 
        raiz.altura = 1 + max(self.getAltura(raiz.esquerda),
                              self.getAltura(raiz.direita))

        balanceFator = self.getBalanco(raiz)

        # Apos determinado o fator de balanceamento, ira realizar o balanceamento caso necessario avaliando-se o resultado
        if balanceFator > 1: # Caso o fator de balanceamento seja maior do que 1 ira rotacionar a raiz para a direita
            if self.getBalanco(raiz.esquerda) >= 0:
                return self.direitaRotacao(raiz)
            else:
                raiz.esquerda = self.esquerdaRotacao(raiz.esquerda)
                return self.direitaRotacao(raiz)
        if balanceFator < -1: # Caso o fator de balanceamento seja menor do que 1 ira rotacionar a raiz para a esquerda
            if self.getBalanco(raiz.direita) <= 0:
                return self.esquerdaRotacao(raiz)
            else:
                raiz.direita = self.direitaRotacao(raiz.direita)
                return self.esquerdaRotacao(raiz)
        return raiz # Por fim retorna a raiz, apos o deleta e balanceamento caso necessario

    # Funcao encarregada por rotacionar pela esquerda da arvore
    def esquerdaRotacao(self, z):
        y = z.direita
        T2 = y.esquerda
        y.esquerda = z
        z.direita = T2
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    # Funcao encarregada por rotacionar pela direita da arvore
    def direitaRotacao(self, z):
        y = z.esquerda
        T3 = y.direita
        y.direita = z
        z.esquerda = T3
        z.altura = 1 + max(self.getAltura(z.esquerda),
                           self.getAltura(z.direita))
        y.altura = 1 + max(self.getAltura(y.esquerda),
                           self.getAltura(y.direita))
        return y

    # Funcao encarregada por determinar a altura na avore
    def getAltura(self, raiz):
        if not raiz:
            return 0
        return raiz.altura

    # Funcao encarragada por determinar o fator de balanceamento
    def getBalanco(self, raiz):
        if not raiz:
            return 0
        return self.getAltura(raiz.esquerda) - self.getAltura(raiz.direita)

    def getMinValorNode(self, raiz):
        if raiz is None or raiz.esquerda is None:
            return raiz
        return self.getMinValorNode(raiz.esquerda)

    def preOrdem(self, raiz):
        if not raiz:
            return
        print("{0} ".format(raiz.chave), end="")
        self.preOrdem(raiz.esquerda)
        self.preOrdem(raiz.direita)

    # Printa a arvore
    def printTree(self, raiz, indente, bol):
        if raiz != None:
            sys.stdout.write(indente)
            if bol:
                sys.stdout.write("D----")
                indente += "     "
            else:
                sys.stdout.write("E----")
                indente += "|    "
            print(raiz.chave)
            self.printTree(raiz.esquerda, indente, False)
            self.printTree(raiz.direita, indente, True)
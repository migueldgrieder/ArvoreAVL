from nodo import Nodo

class ArvoreAVL(object):

    def __init__(self):
        self.raiz = None

    def busca(self,valor): # Busca um nodo com o valor inserido
        if self.raiz is None: # Caso nao haja nenhum nodo na arvore
            return None
        else:
            return self._busca(valor,self.raiz)  # Caso exista um nodo, será realizada a busca de fato

    def _busca(self,valor,nodo): # Método responsável pela busca de um nodo
        if nodo is None:
            return None
        elif valor<nodo.valor:
            return self._busca(valor,self.esquerda)
        elif valor>nodo.valor:
            return self._busca(valor,self.direita)
        else:
            return nodo

    def buscaMin(self):
        if self.raiz is None:
            return None
        else:
            return self._buscaMin(self.raiz)

    def _buscaMin(self,nodo):
        if nodo.esquerda:
            return self._buscaMin(nodo.esquerda)
        else:
            return nodo

    def buscaMax(self):
        if self.raiz is None:
            return None
        else:
            return self._buscaMax(self.raiz)

    def _buscaMax(self,nodo):
        if nodo.direita:
            return self._buscaMax(nodo.direita)
        else:
            return nodo

    def tamanho(self,nodo):
        if nodo is None:
            return -1
        else:
            return nodo.tamanho
    
    def rotacao_esquerda_simples(self,nodo):
        k1=nodo.esquerda
        nodo.esquerda=k1.direita
        k1.direita=nodo
        nodo.tamanho=max(self.tamanho(nodo.direita),self.tamanho(nodo.esquerda))+1
        k1.tamanho=max(self.tamanho(k1.esquerda),nodo.tamanho)+1
        return k1

    def rotacao_direita_simples(self,nodo):
        k1=nodo.direita
        nodo.direita=k1.esquerda
        k1.esquerda=nodo
        nodo.tamanho=max(self.tamanho(nodo.direita),self.tamanho(nodo.esquerda))+1
        k1.tamanho=max(self.tamanho(k1.direita),nodo.tamanho)+1
        return k1

    def rotacao_esquerda_dupla(self,nodo):
        nodo.esquerda=self.rotacao_direita_simples(nodo.esquerda)
        return self.rotacao_esquerda_simples(nodo)

    def rotacao_direita_dupla(self,nodo):
        nodo.direita=self.rotacao_esquerda_simples(nodo.direita)
        return self.rotacao_direita_simples(nodo)

    def adicionar(self,valor):
        if not self.raiz:
            self.raiz= Nodo(valor)
        else:
            self.raiz=self._adicionar(valor,self.raiz)
            
    def _adicionar(self,valor,nodo):
        if nodo is None:
            nodo = Nodo(valor)
            
        elif valor<nodo.valor:
            nodo.esquerda=self._adicionar(valor,nodo.esquerda)
            if (self.tamanho(nodo.esquerda)-self.tamanho(nodo.direita))==2:
                if valor<nodo.esquerda.valor:
                    nodo=self.rotacao_esquerda_simples(nodo)
                else:
                    nodo=self.rotacao_esquerda_dupla(nodo)
            
        elif valor>nodo.valor:
            nodo.direita=self._adicionar(valor,nodo.direita)
            if (self.tamanho(nodo.direita)-self.tamanho(nodo.esquerda))==2:
                if valor<nodo.direita.valor:
                    nodo=self.rotacao_direita_dupla(nodo)
                else:
                    nodo=self.rotacao_direita_simples(nodo)
        
        
        nodo.tamanho=max(self.tamanho(nodo.direita),self.tamanho(nodo.esquerda))+1
        return nodo
        
    def deletar(self,valor):
        self.raiz=self.remover(valor,self.raiz)

    def remover(self,valor,nodo):
        if nodo is None:
            print("Erro!\nO nodo inserido nao existe na arvore!")

        elif valor<nodo.valor:
            nodo.esquerda=self.remover(valor,nodo.esquerda)
            if (self.tamanho(nodo.direita)-self.tamanho(nodo.esquerda))==2:
                if self.tamanho(nodo.direita.direita)>=self.tamanho(nodo.direita.esquerda):
                    nodo=self.rotacao_direita_simples(nodo)
                else:
                    nodo=self.rotacao_direita_dupla(nodo)
            nodo.tamanho=max(self.tamanho(nodo.esquerda),self.tamanho(nodo.direita))+1
            
                
        elif valor>nodo.valor:
            nodo.direita=self.remover(valor,nodo.direita)
            if (self.tamanho(nodo.esquerda)-self.tamanho(nodo.direita))==2:
                if self.tamanho(nodo.esquerda.esquerda)>=self.tamanho(nodo.esquerda.direita):
                    nodo=self.rotacao_esquerda_simples(nodo)
                else:
                    nodo=self.rotacao_esquerda_dupla(nodo)
            nodo.tamanho=max(self.tamanho(nodo.esquerda),self.tamanho(nodo.direita))+1
        
        elif nodo.esquerda and nodo.direita:
            if nodo.esquerda.tamanho<=nodo.direita.tamanho:
                minnodo=self._buscaMin(nodo.direita)
                nodo.valor=minnodo.valor
                nodo.direita=self.remover(nodo.valor,nodo.direita)
            else:
                maxnodo=self._buscaMax(nodo.esquerda)
                nodo.valor=maxnodo.valor
                nodo.esquerda=self.remover(nodo.valor,nodo.esquerda)
            nodo.tamanho=max(self.tamanho(nodo.esquerda),self.tamanho(nodo.direita))+1
        else:
            if nodo.direita:
                nodo=nodo.direita
            else:
                nodo=nodo.esquerda
        
        return nodo
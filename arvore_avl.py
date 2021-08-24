from nodo import Nodo

class ArvoreAVL(object):

    def __init__(self):
        self.raiz = None

    def busca(self,valor): # Busca um nodo com o valor inserido
        if self.raiz is None: # Caso nao haja nenhum nodo na arvore
            return None
        else:
            return self._busca(valor,self.raiz)  # Caso exista um nodo, será realizada a busca de fato

    def _busca(self,valor,nodo): # Método responsável pela busca de um nodo de fato
        if nodo is None:
            return None
        elif valor<nodo.valor:
            return self._busca(valor,self.esquerda)
        elif valor>nodo.valor:
            return self._busca(valor,self.direita)
        else:
            return nodo # Por fim retorna o nodo com o elemento(valor) buscado, caso exista

    def buscaMin(self): # Busca o nodo com o menor valor na arvore
        if self.raiz is None:
            return None
        else:
            return self._buscaMin(self.raiz)

    def _buscaMin(self,nodo): # Realiza de fato a busca pelo nodo com o menor valor na arvore
        if nodo.esquerda: # Funciona parecido com um  while, ira executar a busca até que nao haja um nodo menor conectado ao atual da busca
            return self._buscaMin(nodo.esquerda)
        else:
            return nodo # Por fim retorna o menor nodo

    def buscaMax(self): # Busca o nodo com maior valor na arvore
        if self.raiz is None: 
            return None
        else:
            return self._buscaMax(self.raiz)

    def _buscaMax(self,nodo): # Realiza de fato a busca pelo nodo com o maior valor na arvore
        if nodo.direita: # Funciona parecido com while, executa ate que nao haja um nodo maior conectado ao atual
            return self._buscaMax(nodo.direita)
        else:
            return nodo # Por fim retorna o maior nodo

    def tamanho(self,nodo): # Responsavel por retornar o tamanho de um nodo
        if nodo is None:
            return -1
        else:
            return nodo.tamanho
    
    def rotacao_esquerda_simples(self,nodo): # Responsavel por realizar a rotacao simples sentido horario
        k1=nodo.esquerda 
        nodo.esquerda=k1.direita
        k1.direita=nodo 
        nodo.tamanho=max(self.tamanho(nodo.direita),self.tamanho(nodo.esquerda))+1
        k1.tamanho=max(self.tamanho(k1.esquerda),nodo.tamanho)+1
        return k1

    def rotacao_direita_simples(self,nodo): # Responsavel por realizar a rotacao simples sentido anti-horario
        k1=nodo.direita
        nodo.direita=k1.esquerda
        k1.esquerda=nodo
        nodo.tamanho=max(self.tamanho(nodo.direita),self.tamanho(nodo.esquerda))+1
        k1.tamanho=max(self.tamanho(k1.direita),nodo.tamanho)+1
        return k1

    def rotacao_esquerda_dupla(self,nodo): # Responsavel por realizar a rotacao dupla sentido horario
        nodo.esquerda=self.rotacao_direita_simples(nodo.esquerda)
        return self.rotacao_esquerda_simples(nodo)

    def rotacao_direita_dupla(self,nodo): # Responsavel por realizar a rotacao dupla sentido anti-horario
        nodo.direita=self.rotacao_esquerda_simples(nodo.direita)
        return self.rotacao_direita_simples(nodo)

    def adicionar(self,valor): # Realiza a inclusao de novos nodos na arvore
        if not self.raiz: # Caso a arvore nao tenha nodos
            self.raiz= Nodo(valor)
        else:
            self.raiz=self._adicionar(valor,self.raiz)
            
    def _adicionar(self,valor,nodo): # Responsavel de fato pela inclusao, já com a raiz como parametro
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
        
    def deletar(self,valor): # Responsavel por deletar um nodo da arvore
        self.raiz=self.remover(valor,self.raiz)

    def remover(self,valor,nodo): # Responsavel de fato pela remocao de um nodo na arvore
        if nodo is None: # Caso a arvore nao tenha nodos
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
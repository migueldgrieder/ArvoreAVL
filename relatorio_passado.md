Nome: Otavio Augusto da Silva Pinheiro Castro
Matrícula: 20100863

O trabalho apresentou diversos obstáculos, os quais gostaria de dizer que resolvi de imediato, mas não foi esse o caso, nesse relátorio consta algumas explicações de como mentalizei minhas soluções para com o código.

Antes de qualquer coisa, tentei organizar a ordem pela qual iria implementar as operações que deveriam necessariamente constar no código do trabalho, o que futuramente se mostrou um erro, pois antes disso deveria entender por completo o funcionamente de um nodo duplo.

O entendimento do cursor foi outro ponto importante para a realização do trabalho, o cursor nada mais é do que o nodo atual na zona de cursor, como assim? Cada nodo tem um elemento que marca sua identidade na lista, ao mesmo tempo que o cursor é por definição 1 Nodo, também representa todos pois todos estão conectados, apesar de ele ser 1 quando representado no self.__cursor, mas como todos estão ligados, em 1 objeto pode-se conseguir vários.

Após diversas falhas decidi montar um quadro de possibilidades dos nodos, para que não voltasse a esquecer algum tipo específico:
Listas possiveis: 
Listas com 1 Nodo ou Nenhum:
    Fila sem Nodos   ->             Nada
    Fila com 1 Nodo  ->       Nada|Cursor|Nada
Listas com Mais de 1 Nodo:
    Nodo no Começo ->         Nada |Cursor| Outro Nodo
    Nodo no Final ->     Outro Nodo|Cursor| Nada
    Nodo Entre Outros -> Outro Nodo|Cursor| Nada

Com base nessas possibilidades recomeçei as implementações, realizando testes simultaneamente com o término de cada método.

Para o último ponto que resolvi registrar, a implementação de exclusão de nodos atuais na lista. 
Caso ocorra de excluir o nodo atual(representado pelo cursor) em uma lista em que esse nodo encontra-se entre outros Nodos (seu anterior é Outro Nodo e seu próximo também) o processo será representado abaixo:

    Nodo|Cursor|Nodo    O que seria excluir esse Nodo do meio(cursor)?
Digamos que: 
       1|Cursor|2  -> Lista ATUAL
    O que o cursor é nesse caso? O cursor é o anterior do proximo(2) e também o próximo do anterior(1), dito isso basta transformamos o anterior do proximo no anterior do Cursor (transformar o Cursor em 1 PARA o 2), e o proximo do anterior no proximo do Cursor (Transformar o Cursor em 2 para o 1), feito isso conseguimos fazer um nova corrente em que o cursor não mais exista, caso avance para o proximo ou retroceda para o anterior, pois os mesmos já não apontam mais para ele, funcionando como uma "exclusão".

Em resumo a exclusao entre:
  Digamos que exista uma lista: 1 | 2 | 3
  E que você está no 2, por definiçao o 2 é o numero anterior ao 3 e seguinte ao 1, para que o 2 deixe de existir basta apenas com que o anterior ao 3 e o seguinte ao 1 não seja mais o 2, assim deixando de existir para seus números em contato, e quando se avançar ou retroceder não mais será possível acessar o 2. 
Trabalho feito em DUPLA

Nome: Otavio Augusto da Silva Pinheiro Castro
Matrícula: 20100863

Nome: Miguel Duarte Grieder
Matrícula: 20100862



                                    RELATÓRIO TRABALHO 2 - ÁRVORES AVL

O primeiro passo a ser tomado pela dupla foi a organização dos métodos, a ordem em qual seriam montados e inseridos, o que demandou uma reflexão e pesquisa sobre o funcionario de uma arvore AVL antes de começarmos.

A Arvore AVL funciona, assim como cada outros tópicos estudados anteriormente na disciplina, com a conexão de objetos conectados um aos outros, logo o objeto Nodo foi o primeiro a ser implementado.

Características essenciais da Arvore AVL: Deve estar sempre balanceada, ou seja, cada sub-árvore de todo nó deve ter uma altura que difere em mais do que 1, composta essencialmente de nodos, em que cada nó pode apontar para 2 outros nodos, por isso árvore binária. Esse balanceamento e feito de forma automatica ao realizar as operações como inserir e deletar, e sao feitos através de metodos especificos como rotação para lado x e rotação para lado x dupla.

Nodo: Cada objeto nodo deve ser responsável por indicar sua própria altura, a qual chamamos de tamanho nesse código, pois é essencial para o balanceamento da arvore como um todo. Outros atributos são espaços para futuros nodos a esquerda e a direita. Essencialmente para que o nodo exista é necessário apenas um valor inicialmente. O nodo raiz tem a altura 0, e vai incrementando 1 conforme as próximas camadas

Explicações técnicas:

Nodo (Figura):
       Valor         |
      /    \         | Tamanho
Esquerda   Direita   |  

Arvore AVL(Figura):
      Nodo Raiz       Em que a árvore seguirá a lógica:  Nodo Raiz > Nodo(A) e Nodo Raiz < Nodo(B)
       /    \         A lógica será aplicada em todas as sub-árvores possivelmente existentes, ou seja,
   Nodo(A)  Nodo(B)   Num certo nodo, o nodo ligado a direita será sempre maior do que o mesmo, e o a esquerda menor.

Após implementado o nodo, começa de fato a implementação da árvore AVL.
Na árvore os primeiros métodos, sendo os mais básicos, que serviram tanto para checar a árvore como um tanto quanto para métodos principais como remoção, foram os primeiros a serem implementados.

A busca pelo menor valor e maior valor: Conhecendo-se a lógica de posicionamento da árvore, a busca caso seja pelo menor, irá percorrer pelos caminhos a esquerda da árvore até que não haja mais algum para percorrer, e por fim entregará a informação desse nodo. Caso seja pela maior valor, o percorre será realizado pela direita, até que não haja mais como percorrer por tal.

Lembrando de que o que buscamos nesse método é o menor e maior valor na árvore, e não o galho mais ao fundo da árvore
Por exemplo:
        5     
       / \
      3   6    O nodo de menor valor será o 3.
       \
        4

Também há a busca por um nodo específico, em que ocorrerá seguindo a mesma lógica dos anteriores, comparando o valor de cada nodo com o valor buscado, e caso seja menor irá para o caminho a esquerda, caso maior pelo da direita, e assim repetindo a comparação como um while, em que será parado quando o nodo for o procurado ou não haja nodo a se comparar, indicando a inexistencia do nodo buscado.

Inseridos os metodos de busca para a árvore, o próximo passo será as rotações, simples e duplas, em que balanceiam a árvore após a inserção e/ou remoção de nodos.

Sobre as Rotações Simples (No sentido horário e anti-horário): Tais métodos são o alircece da árvore, serão chamados quando necessários na adição e remoção de nodos, basicamente faz com que a árvore troque os nodos de posição, tomando como nodo foco a raiz, trocando a "raiz" para outro nodo, fazendo assim a arvore "rotacionar", e por fim atualizando as alturas dos nodos mexidos.

Sobre as rotações duplas: As rotações duplas nada mais são do que rotações simples encima de rotações simples, de maneira alternada, basicamente funciona da seguinte forma: Digamos que seja feita uma rotação dupla esquerda, entao primeiro pegamos o nodo à esquerda da raiz, e realizamos uma rotação simples para a direita (sentido anti-horario), então a sub-arvore esquerda agora está rotacionada, após isso realizamos uma rotação simples para a esquerda ( sentido horario) pela raiz, rotacionando toda a arvore como um todo, logo a junção dessas rotações forma a rotação dupla.

Por fim temos a adição e remoção de nodos na árvore AVL, com todos os métodos básicos como buscas e rotações já determinados, o que resta é apenas determinar quando cada método deverá ser usado na adição e remoção.

Sobre a adição e remoções: Funcionam como um loop, onde serão feitas comparações com o nodo no oloforte, é o nodo que está ocupando a posição "nodo" nos parametros do metodo de adição, e o nodo a ser inserido, começando pela raiz, por exemplo:
Caso o valor do novo nodo seja menor do que o valor do nodo atual, será utilizado o método de adição novamente, em que o nodo no oloforte seguinte será o que estiver ocupando a posição a esquerda do nodo oloforte anterior, e caso seja maior do que o valor do nodo atual será utilizado o método de adição novamente, porém agora com o nodo oloforte sendo o nodo na posição direita... O método ocorrerá até que chegue-se a um nodo que tenha sua posição esquerda ou direita vazia, realizando assim finalmente o final do loop, inserindo na posição vazia o novo nodo.
Importante dizer que o balanceamento ocorrerá a cada busca de nodo por nodo, em que caso a diferença dos tamanhos do nodo da esquerda com o da direita sejam 2, ou seja maiores do que 1, será então necessária ser feita uma rotação antes de continuar com o loop de adição, em que por exemplo: caso o nodo a ser adicionado tenha o valor menor do que o da esquerda, então para tentar ocupar aquela posição, a arvore será rotacionada da esquerda para direita simples, caso o valor seja maior do que o nodo da esquerda entao será realizada uma rotação dupla.

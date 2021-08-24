from arvore import AVLTree

myTree = AVLTree()
raiz = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    raiz = myTree.inserir_node(raiz, num)
myTree.printTree(raiz,"", True)

chave = 13
raiz = myTree.deleta_node(raiz, chave)
print("After Deletion: ")
myTree.printTree(raiz,"", True)
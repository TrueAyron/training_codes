# A classe Node representa um nó individual na lista, que armazena os dados e as referências para o próximo e anterior nós na lista.
class Node:
    def __init__(self, data):
        self.data = data # Armazena os dados no nó
        self.next = None # Referência para o próximo nó na lista
        self.prev = None # Referência para o nó anterior na lista

# A classe DoublyLinkedList representa a lista duplamente encadeada em si
# com métodos para adicionar elementos (append) e imprimir os elementos (print_list)
class DoublyLinkedList:
    def __init__(self):
        self.head = None # Inicializa a cabeça da lista como None
    
    #O método append adiciona um novo nó no final da lista com os dados fornecidos. Ele cria um novo objeto Node
    #  com os dados fornecidos e, se a lista estiver vazia, o novo nó será a cabeça da lista. Caso contrário, o 
    # método itera a partir da cabeça da lista até encontrar o último nó, adicionando o novo nó logo depois dele 
    # e atualizando os ponteiros prev e next.
    def append(self, data):
        new_node = Node(data) # Cria um novo nó com os dados fornecidos
        if self.head is None: # Se a lista estiver vazia
            self.head = new_node # O novo nó será a cabeça da lista
            return
        curr = self.head # Inicia a iteração a partir da cabeça da lista
        while curr.next: # Enquanto houver um próximo nó
            curr = curr.next # Vai para o próximo nó
        curr.next = new_node # Adiciona o novo nó no final da lista
        new_node.prev = curr # Atualiza o ponteiro prev do novo nó para o nó anterior

    # O método print_list itera através da lista a partir da cabeça, imprimindo os dados de cada nó e avançando para
    # o próximo nó até chegar ao final da lista.    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

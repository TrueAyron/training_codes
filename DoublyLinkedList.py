class Node:
    def __init__(self, data):
        self.data = data # Armazena os dados no nó
        self.next = None # Referência para o próximo nó na lista
        self.prev = None # Referência para o nó anterior na lista

class DoublyLinkedList:
    def __init__(self):
        self.head = None # Inicializa a cabeça da lista como None
    
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
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

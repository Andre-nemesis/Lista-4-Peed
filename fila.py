#arquivo da fila (queue)
class Item:
    def __init__(self, valor):
        self.value = valor
        self.next = None

class Fila:
    def __init__(self, size=None):
        self.head = None
        self.tail = None
        self.size = size if size is not None else float('inf')#metodo para predefinir o tamanho da fila
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            raise IndexError('A fila está cheia')
        new_item = Item(value)
        if self.is_empty():
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')
        value = self.head.value#armazenando o primeiro valor da fila
        self.head = self.head.next#trocando o primeiro valor da fila para o próximo elemento
        self.count -= 1
        if self.head is None:
            self.tail = None
        return value
    
    def is_empty(self):
        return self.head is None
    
    def is_full(self):
        return self.count >= self.size 
    
    def tamanho(self):
        return self.count
    
    def end_element(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')
        return self.tail.value
    
    def next_element(self):
        if self.is_empty():
            raise IndexError('A fila está vazia')
        return self.head.value
    
    def __str__(self):
        s= ""
        aux = self.head
        while aux is not None:
            s += str(aux.value) + " "
            aux = aux.next
        return s
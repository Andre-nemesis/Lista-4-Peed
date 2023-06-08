class Item:
    def __init__(self,value):
        self.value = value
        self.prox = None
        self.ant = None

class ListaEncadeadaDupla:
    def __init__(self,tamanho=None):
        self.inicio = None
        self.size = tamanho if tamanho is not None else float('inf')
        self.count = 0
    
    def is_empyt(self):
        return self.inicio is None
    
    def is_full(self):
        return self.count >= self.size
    
    def tamanho(self):
        return self.count

    def inserir_ini(self,elemento):
        if self.is_full():
            raise IndexError('A lista está cheia!')
        novo_item = Item(elemento)
        if self.inicio is None:
            self.inicio = novo_item
        else:
            novo_item.prox = self.inicio
            self.inicio = novo_item
            novo_item.ant = self.inicio
        self.count += 1
    
    def inserir_fin(self, elemento):
        novo_item = Item(elemento)
        if self.is_empyt():
            self.inicio = novo_item
            self.count += 1
        else:
            ultimo = self.inicio
            while ultimo.prox is not None:
                ultimo = ultimo.prox
            ultimo.prox = novo_item
            novo_item.ant = ultimo
            self.count += 1

    def remover_fin(self):
        if self.is_empyt():
            raise IndexError('A lista está vazia')
        if self.inicio.prox is None:
            valor = self.inicio.value
            self.inicio = None
            self.count -= 1
            return valor
        aux = self.inicio
        anterior = None
        while aux.prox is not None:
            anterior = aux
            aux = aux.prox
        valor = aux.value
        anterior.prox = None
        self.count -= 1
        return valor

    def remover_ini(self):
        if self.is_empyt():
            raise IndexError('A lista está vazia')
        valor = self.inicio.value
        self.inicio = self.inicio.prox
        return valor

    def buscar(self,item):
        if self.inicio is None:
            raise IndexError('A lista está vazia')
        aux = self.inicio
        while aux is not None:
            if aux.value == item:
                return True
            aux = aux.prox
        return False

    def __str__(self):
        if self.is_empyt():
            return 'A lista está vazia!'
        s= ""
        aux = self.inicio
        for i in range(self.count):
            if aux is None:
                break
            s += str(aux.value) + " "
            aux = aux.prox
        return s
    
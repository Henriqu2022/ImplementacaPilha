# TAD Pilha
class Pilha:
    def __init__(self, tam):
        self.itens = [0] * tam
        self.tam = tam
        self.topo = -1

    def insere(self, elemento):
        if self.cheia():
            print("Pilha Cheia")
            return
        self.topo += 1
        self.itens[self.topo] = elemento
        print(self.itens, self.topo, elemento)
        return None

    def remove(self):
        if not self.vazia():
            self.topo -= 1
        else:
            print("Pilha Vazia")
        print(self.itens[self.topo])
        return None

    def vazia(self):
        if self.topo == -1:
            return True
        return False

    def cheia(self):
        if self.tam == self.topo + 1:
            return True
        return False



pilha = Pilha(5)
for i in range(6):
  pilha.insere(i+1)

for i in range(6):
  pilha.remove()
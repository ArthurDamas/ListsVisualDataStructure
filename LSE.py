class No:
    def __init__(self):
        self._conteudo = 0
        self._proximo = None

    @property
    def conteudo(self):
        return self._conteudo

    @property
    def proximo(self):
        return self._proximo

    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo


class LSE:
    def __init__(self):
        self.cabeca = No()
        self.num_elem = 0

    def vazia(self):
        return self.num_elem == 0

    def tamanho(self):
        aux = self.cabeca.proximo
        qtd = 0
        while aux is not None:
            aux = aux.proximo
            qtd += 1
        return qtd

    def elemento(self, pos):
        if self.vazia():
            return -1  # exception
        if pos < 1 or pos > self.tamanho():
            return -1  # exception

        aux = self.cabeca.proximo
        for i in range(1, pos):
            aux = aux.proximo

        return aux.conteudo

    def posicao(self, dado):
        if self.vazia():
            return -1  # exception
        aux = self.cabeca.proximo
        qtd = 1
        while aux is not None:
            if aux.conteudo == dado:
                return qtd
            aux = aux.proximo
            qtd += 1

        return -1  # exception

    def insere_inicio_lista(self, valor):
        novo_no = No()

        novo_no.conteudo = valor
        novo_no.proximo = self.cabeca.proximo
        self.cabeca.proximo = novo_no

        self.num_elem += 1

        return True

    def insere_meio_lista(self, pos, valor):
        novo_no = No()
        novo_no.conteudo = valor

        aux = self.cabeca.proximo
        for i in range(1, pos - 1):
            aux = aux.proximo

        novo_no.proximo = aux.proximo
        aux.proximo = novo_no

        self.num_elem += 1

        return True

    def insere(self, pos, valor):
        if self.vazia() and pos != 1:
            return False  # posição inválida com lista vazia

        if pos <= 0 or pos > self.num_elem + 1:
            return False  # posição inválida

        if pos == 1:
            return self.insere_inicio_lista(valor)
        else:
            return self.insere_meio_lista(pos, valor)

    def remove_inicio_lista(self):
        p = self.cabeca.proximo

        valor_removido = p.conteudo
        self.cabeca.proximo = p.proximo

        self.num_elem -= 1

        return valor_removido

    def remove_na_lista(self, pos):
        antecessor = self.cabeca

        for i in range(1, pos):
            antecessor = antecessor.proximo

        atual = antecessor.proximo
        valor_removido = atual.conteudo
        antecessor.proximo = atual.proximo

        self.num_elem -= 1

        return valor_removido

    def remove(self, pos):
        if self.vazia():
            return -1  # lista vazia

        if pos <= 0 or pos > self.num_elem:
            return -1

        if pos == 1:
            return self.remove_inicio_lista()

        else:
            return self.remove_na_lista(pos)

    def exibir_lista(self):
        for i in range(1, self.tamanho() + 1):
            dado = self.elemento(i)
            print(f"#{i} -> {dado}")
        print()


ls = LSE()
qtd = 0

if ls.vazia():
    print("Lista inicialmente vazia.")
else:
    print("Lista inicialmente preenchida.")

ls.insere(1, 10)
ls.insere(2, 20)
ls.insere(3, 30)
ls.insere(4, 40)

qtd += 1

print(f"Inserção {qtd}.")
ls.exibir_lista()

ls.insere(3, 25)
ls.insere(5, 35)

qtd += 1
print(f"Inserção {qtd}.")
ls.exibir_lista()

ls.insere(2, 2000)

qtd += 1
print(f"Inserção {qtd}.")
ls.exibir_lista()

ret = ls.insere(1, 101)
print(f"Inserção do 101 na posição 1: {ret}")

qtd += 1
print(f"Inserção {qtd}.")
ls.exibir_lista()

ret = ls.insere(20, 500)
print(f"Inserção do 500 na posição 20: {ret}")

print(f"Posição do elemento 10: {ls.posicao(10)}")
print(f"Posição do elemento 30: {ls.posicao(30)}")
print(f"Posição do elemento 40: {ls.posicao(40)}")
print(f"Posição do elemento 15: {ls.posicao(15)}")

print(f"\nTamanho = {ls.tamanho()} elementos.\n")

ls.exibir_lista()
dado = ls.remove(1)

print(f"Dado removido = {dado}\n\n")

print("Lista depois da 1a remoção.")
ls.exibir_lista()

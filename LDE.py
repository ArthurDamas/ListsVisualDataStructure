class No:
    def __init__(self):
        self._conteudo = 0
        self._anterior = None
        self._proximo = None

    @property
    def conteudo(self):
        return self._conteudo

    @property
    def anterior(self):
        return self._anterior

    @property
    def proximo(self):
        return self._proximo

    @conteudo.setter
    def conteudo(self, conteudo):
        self._conteudo = conteudo

    @anterior.setter
    def anterior(self, anterior):
        self._anterior = anterior

    @proximo.setter
    def proximo(self, proximo):
        self._proximo = proximo


class LDE:
    def __init__(self):
        self.inicio = No()
        self.fim = No()
        self.num_elem = 0

    def vazia(self):
        return self.num_elem == 0

    def tamanho(self):
        return self.num_elem

    def elemento(self, pos):
        aux = self.inicio
        qtd = 1

        if self.vazia():
            return -1  # exception

        if pos < 1 or pos > self.tamanho():
            return -1  # exception

        while qtd < pos:
            aux = aux.proximo
            qtd += 1

        return aux.conteudo

    def posicao(self, dado):
        i = 1

        if self.vazia():
            return -1  # exception

        aux = self.inicio

        while aux is not None:
            if aux.conteudo == dado:
                return i
            else:
                aux = aux.proximo
                i += 1

        return -1  # exception

    def insere_inicio_lista(self, valor):
        novo_no = No()

        novo_no.conteudo = valor
        novo_no.proximo = self.inicio

        novo_no.anterior = None

        if self.vazia():
            self.fim = novo_no
        else:
            self.inicio.anterior = novo_no

        self.inicio = novo_no
        self.num_elem += 1

        return True

    def insere_meio_lista(self, pos, dado):
        qtd = 1

        novo_no = No()
        novo_no.conteudo = dado

        aux = self.inicio

        while qtd < pos - 1 and aux is not None:
            aux = aux.proximo
            qtd += 1

        if aux is None:
            return False

        novo_no.anterior = aux
        novo_no.proximo = aux.proximo

        aux.proximo.anterior = novo_no
        aux.proximo = novo_no

        self.num_elem += 1

        return True

    def insere_fim_lista(self, dado):
        novo_no = No()

        novo_no.conteudo = dado
        novo_no.proximo = None

        self.fim.proximo = novo_no

        novo_no.anterior = self.fim
        self.fim.proximo = novo_no
        self.fim = novo_no

        self.num_elem += 1

        return True

    def insere(self, pos, dado):
        if self.vazia() and pos != 1:
            return False
        if pos == 1:
            self.insere_inicio_lista(dado)
        elif pos == self.num_elem + 1:
            self.insere_fim_lista(dado)
        else:
            self.insere_meio_lista(pos, dado)

    def remove_inicio_lista_unitaria(self):
        dado = self.inicio.conteudo

        self.inicio = None
        self.fim = None

        self.num_elem -= 1

        return dado

    def remove_inicio_lista(self):
        p = self.inicio

        dado = p.conteudo

        self.inicio = p.proximo
        p.proximo.anterior = None

        self.num_elem -= 1

        return dado

    def remove_meio_lista(self, pos):
        p = self.inicio
        n = 1

        while n <= pos - 1 and p is not None:
            p = p.proximo
            n += 1

        if p is None:
            return -1  # exception

        dado = p.conteudo
        p.anterior.proximo = p.proximo
        p.proximo.anterior = p.anterior

        self.num_elem -= 1

        return dado

    def remove_fim_lista(self):
        p = self.fim
        dado = p.conteudo

        self.fim.anterior = p.conteudo
        self.fim = self.fim.anterior

        self.num_elem -= 1

        return dado

    def remove(self, pos):
        if self.vazia():
            return -1  # exception
        if pos == 1 and self.tamanho() == 1:
            return self.remove_inicio_lista_unitaria()
        elif pos == 1:
            return self.remove_inicio_lista()
        elif pos == self.tamanho():
            return self.remove_fim_lista()
        else:
            return self.remove_meio_lista(pos)

    def exibir_lista(self):
        print(f"Lista com {self.tamanho()} elementos.\n")
        for i in range(1, self.tamanho() + 1):
            dado = self.elemento(i)
            print(f"#{i} -> {dado}")
        print()


ls = LDE()

ls.insere(1, 10)
ls.insere(2, 20)
ls.insere(3, 30)
ls.insere(4, 40)

ls.exibir_lista()

ls.insere(3, 25)
ls.insere(5, 35)

ls.exibir_lista()

ls.insere(2, 2000)
ret = ls.insere(1, 101)

print(f"Inserção do 101 na posição 1: {ret}")

ls.exibir_lista()

ls.remove(8)

ls.exibir_lista()

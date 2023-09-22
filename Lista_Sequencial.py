class Lista_Seq:
    def __init__(self, tam_max):
        self.dados = []
        self.__tam_max = tam_max

    @property
    def num_elem(self):
        return len(self.dados)

    def vazia(self):
        if self.num_elem == 0:
            return True
        else:
            return False

    def cheia(self):
        if self.num_elem == self.__tam_max:
            return True
        else:
            return False

    def elemento(self, pos):
        if pos > self.num_elem or pos <= 0:
            return -1  # exception

        return self.dados[pos - 1]

    def posicao(self, valor):
        qtd = 0
        for i in range(self.num_elem):
            if valor == self.dados[i]:
                pos = [i + 1]
                qtd += 1
                while self.posicao_desloc(valor, pos[len(pos)-1]) != -1:
                    pos.append(self.posicao_desloc(valor, pos[len(pos)-1]))
                    qtd += 1
                return pos
        return False

    def posicao_desloc(self, valor, desloc):
        for i in range(desloc, self.num_elem):
            if self.dados[i] == valor:
                return i + 1

        return -1  # exception

    def insere(self, pos, valor):
        if self.cheia() or (pos - 1 > self.num_elem) or pos <= 0:
            return False

        elif self.vazia() and pos == 1:
            self.dados.append(valor)
            return True

        self.dados.append(self.dados[self.num_elem - 1])

        for i in range(self.num_elem - 1, pos - 1, -1):
            self.dados[i] = self.dados[i - 1]

        self.dados[pos - 1] = valor
        return True

    def remove(self, pos):
        if pos > self.num_elem or pos < 1:
            return -1  # exception

        aux = self.dados[pos - 1]

        for i in range(pos - 1, self.num_elem - 1):
            self.dados[i] = self.dados[i + 1]

        self.dados.pop()
        return aux

    def exibir(self):
        print(f"Tamanho da lista: {self.num_elem} elementos.\n")
        for i in range(0, self.num_elem):
            print(f"#{i + 1} -> {self.dados[i]}")
        print("\n")

    def menu(self):
        op = int(input("0 - sair\n"
                       "1 - inserir elementos na lista\n"
                       "2 - consultar se está vazia\n"
                       "3 - consultar se está cheia\n"
                       "4 - consultar elemento\n"
                       "5 - remover elemento da lista\n"
                       "6 - exibir lista\n"
                       "7 - exibir tamanho da lista\n"
                       "8 - esvaziar a lista\n"
                       "Digite aqui: "))
        print(100 * "\n")
        if op == 0:
            return False
        elif op == 1:
            num = int(input("Digite o elemento da lista: "))
            pos = -1
            while pos <= 0:
                print(f"Tamanho da lista: {self.num_elem} elementos.\n")
                pos = int(input("Digite a posição do elemento: "))
            self.insere(pos, num)
            print(100*"\n")
        elif op == 2:
            print(f"Está vazia? {self.vazia()}")
        elif op == 3:
            print(f"Está cheia? {self.cheia()}")
        elif op == 4:
            num = int(input("Digite o elemento a ser consultado: "))
            print(100*"\n")
            pos = self.posicao(num)
            if pos:
                for i in pos:
                    print(f"Posição {i}.")
            else:
                print(f"Não temos o elemento {num}.")
        elif op == 5:
            if self.vazia():
                print("Lista vazia.")
                return True
            pos = -1
            while pos <= 0 or pos > self.num_elem + 1:
                pos = int(input("Digite a posição do elemento a ser removido: "))
                print(100*"\n")
                if pos == 1 and self.num_elem == 1:
                    self.dados.pop()
                else:
                    self.remove(pos)
        elif op == 6:
            print(100*"\n")
            self.exibir()
        elif op == 7:
            print(100*"\n")
            print(f"Tamanho da lista: {self.num_elem} elementos.\n")
        elif op == 8:
            print(100*"\n")
            x = int(input("Tem certeza que quer ESVAZIAR a lista? 0 - NÃO ESVAZIE, 1 - ESVAZIE.\nDigite aqui: "))
            if x == 1:
                self.dados = []
            print(f"Está vazia? {self.vazia()}")

        return True


lista = Lista_Seq(100)

ret = True
while ret:
    ret = lista.menu()

# if lista.vazia():
#     print("Lista criada vazia!")
# else:
#     print("Lista criada não vazia!")
#
# lista.insere(1, 10)
# lista.insere(2, 20)
# lista.insere(3, 30)
# lista.insere(4, 40)
#
# lista.insere(3, 25)
# lista.insere(5, 35)
#
# print("Lista após 1as inserções:")
#
# lista.exibir()
#
# lista.insere(2, 2000)
# ret = lista.insere(1, 101)
#
# print(f"Inserção do 101 na posição 1 = {ret}\n")
#
# print("Lista após as 2as inserções:")
# lista.exibir()
#
# ret = lista.insere(20, 500)
# print(f"Inserção do 20 na posição 500 = {ret}\n")
#
# print(f"Posição do elemento 10 = {lista.posicao(10)}")
# print(f"Posição do elemento 30 = {lista.posicao(30)}")
# print(f"Posição do elemento 15 = {lista.posicao(15)}")
# print(f"Posição do elemento 40 = {lista.posicao(40)}")
#
# print(f"Tamanho = {lista.num_elem}")
#
# dado = lista.remove(3)
# print(f"Dado removido = {dado}\n\n")
#
# print("Lista depois da 1a remoção:")
# lista.exibir()

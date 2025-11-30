
from .jogo import JogoDigital, JogoFisico

class Carrinho:
    def __init__(self):
        self._itens = []

    def adicionar(self, jogo):
        self._itens.append(jogo)
        print(f"[CARRINHO] '{jogo.get_nome()}' foi adicionado.")

    def remover(self, jogo):
        if jogo in self._itens:
            self._itens.remove(jogo)
            print(f"[CARRINHO] '{jogo.get_nome()}' removido.")

    def calcular_total(self):
        return sum(j.get_preco() for j in self._itens)

    def get_itens(self):
        return list(self._itens)

    def checkout(self, usuario, metodo_pagamento, endereco_entrega=None):
        total = self.calcular_total()
        print(f"[CHECKOUT] Total da compra: R$ {total:.2f}")

        metodo_pagamento.pagar(total)

        for jogo in self._itens:
            if isinstance(jogo, JogoDigital):
                usuario.adicionar_a_biblioteca(jogo)
                jogo.baixar()

            elif isinstance(jogo, JogoFisico):
                if endereco_entrega:
                    if jogo.enviar(endereco_entrega):
                        usuario.adicionar_a_biblioteca(jogo)
                else:
                    print(f"[ERRO] Endereço necessário para enviar '{jogo.get_nome()}'.")
        
        print("[OK] Compra concluída!")
        self._itens.clear()
        return True

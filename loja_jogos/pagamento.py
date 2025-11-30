
import abc

class PagamentoStrategy(abc.ABC):
    @abc.abstractmethod
    def pagar(self, valor: float) -> bool:
        pass


class PagamentoPix(PagamentoStrategy):
    def __init__(self, chave):
        self.chave = chave

    def pagar(self, valor):
        print(f"[PAGAMENTO PIX] Valor: R$ {valor:.2f}")
        print(f"[PIX] Chave usada: {self.chave}")
        print("[PROCESSANDO...]")
        print("[OK] Pagamento aprovado pelo PIX!")
        return True


class PagamentoCartao(PagamentoStrategy):
    def __init__(self, numero, titular, validade, cvv):
        self.numero = numero
        self.titular = titular
        self.validade = validade
        self.cvv = cvv

    def pagar(self, valor):
        print(f"[PAGAMENTO CARTÃO] Titular: {self.titular}")
        print(f"[VALOR] R$ {valor:.2f}")
        print("[PROCESSANDO...]")
        print("[OK] Pagamento aprovado!")
        return True

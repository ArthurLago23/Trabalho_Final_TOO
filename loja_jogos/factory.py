
from .jogo import JogoDigital, JogoFisico

class JogoFactory:
    def criar_jogo(self, tipo, nome, preco, tamanho_gb=None, estoque=None):
        if tipo == "digital":
            return JogoDigital(nome, preco, tamanho_gb)
        elif tipo == "fisico":
            return JogoFisico(nome, preco, estoque)
        else:
            raise ValueError("Tipo inválido")


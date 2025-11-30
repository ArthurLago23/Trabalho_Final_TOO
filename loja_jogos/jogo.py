
class Jogo:
    def __init__(self, nome: str, preco: float) -> None:
        self._nome = nome
        self._preco = float(preco)

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco


class JogoDigital(Jogo):
    def __init__(self, nome, preco, tamanho_gb):
        super().__init__(nome, preco)
        self.tamanho_gb = tamanho_gb
        self._baixado = False

    def baixar(self):
        if not self._baixado:
            print(f"[DOWNLOAD] Baixando '{self._nome}' ({self.tamanho_gb} GB)...")
            self._baixado = True
            print(f"[OK] Download concluído!")
        else:
            print(f"[INFO] '{self._nome}' já foi baixado.")


class JogoFisico(Jogo):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco)
        self.estoque = estoque

    def enviar(self, endereco):
        if self.estoque <= 0:
            print(f"[ERRO] Sem estoque de '{self._nome}'!")
            return False
        self.estoque -= 1
        print(f"[ENVIO] Enviando '{self._nome}' para {endereco}...")
        print(f"[INFO] Estoque restante: {self.estoque}")
        return True

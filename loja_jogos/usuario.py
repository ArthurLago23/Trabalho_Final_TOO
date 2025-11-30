
class Usuario:
    def __init__(self, nome):
        self._nome = nome
        self._biblioteca = []

    def adicionar_a_biblioteca(self, jogo):
        self._biblioteca.append(jogo)
        print(f"[BIBLIOTECA] '{jogo.get_nome()}' foi adicionado à biblioteca de {self._nome}.")

    def get_biblioteca(self):
        return list(self._biblioteca)

    def get_nome(self):
        return self._nome

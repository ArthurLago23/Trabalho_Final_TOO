
from loja_jogos.factory import JogoFactory
from loja_jogos.pagamento import PagamentoPix, PagamentoCartao
from loja_jogos.usuario import Usuario
from loja_jogos.carrinho import Carrinho

def main():
    print("\n=== SISTEMA DE LOJA DE JOGOS ===\n")

    factory = JogoFactory()
    usuario = Usuario("Arthur Lago")
    carrinho = Carrinho()

    jogo1 = factory.criar_jogo("digital", "C2", 90.90, tamanho_gb=30)
    """jogo2 = factory.criar_jogo("fisico", "Castle Raiders", 249.90, estoque=0)"""

    carrinho.adicionar(jogo1)
    """carrinho.adicionar(jogo2)"""
    """carrinho.remover(jogo1)"""
    """carrinho.remover(jogo1)"""

    metodo = PagamentoPix("123-chave-pix")

    carrinho.checkout(usuario, metodo, endereco_entrega="Rua Exemplo 123")

    print("\n=== FIM ===")

if __name__ == "__main__":
    main()

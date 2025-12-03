O projeto está organizado em módulos:

jogo.py:
    Jogo (classe base)

    JogoDigital

    JogoFisico

factory.py
    Implementa a JogoFactory, responsável por criar jogos digitais ou físicos.

pagamento.py
    Implementa o padrão Strategy com:
        PagamentoStrategy (abstrata)

            PagamentoPix

            PagamentoCartao

usuario.py
    Classe Usuario, que possui uma biblioteca de jogos.

carrinho.py
    Classe Carrinho, que gerencia itens, calcula total e finaliza a compra.

main.py
    Arquivo principal que demonstra o funcionamento do sistema.


Funcionalidades:

    Criar jogos digitais e físicos via Factory

    Adicionar itens ao carrinho

    Realizar checkout utilizando pagamento por PIX ou cartão

    Enviar jogos físicos para um endereço

    Baixar jogos digitais automaticamente após a compra

    Armazenar jogos na biblioteca do usuário

Conceitos Utilizados:

    Herança (Jogo → JogoDigital / JogoFisico)

    Polimorfismo (PagamentoStrategy)

    Encapsulamento(self._preco)

    Padrão Factory (criação de jogos)

    Padrão Strategy (múltiplas formas de pagamento)
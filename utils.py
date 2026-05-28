def ler_preco():

    while True:

        try:

            preco_str = input("Preço: ")

            preco = float(
                preco_str.replace(',', '.')
            )

            return preco

        except ValueError:

            print("Preço inválido!")


def ler_quantidade(mensagem):

    while True:

        try:

            return int(input(mensagem))

        except ValueError:

            print("Digite um número inteiro!")

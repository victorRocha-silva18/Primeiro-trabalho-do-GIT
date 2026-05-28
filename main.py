from produtos import (

    cadastrar_produto,

    listar_produtos,

    entrada_produto,

    saida_produto,

    verificar_estoque,

    monitor_estoque
)

from relatorios import relatorio


while True:

    print("\n=== ERP ESTOQUE ===")

    print("1 - Cadastrar Produto")

    print("2 - Listar Produtos")

    print("3 - Entrada Produto")

    print("4 - Saída Produto")

    print("5 - Verificar Estoque")

    print("6 - Relatório")

    print("7 - Monitoramento Tempo Real")

    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        cadastrar_produto()

    elif opcao == "2":

        listar_produtos()

    elif opcao == "3":

        entrada_produto()

    elif opcao == "4":

        saida_produto()

    elif opcao == "5":

        verificar_estoque()

    elif opcao == "6":

        relatorio()

    elif opcao == "7":

        monitor_estoque()

    elif opcao == "0":

        print("Sistema encerrado!")

        break

    else:

        print("Opção inválida!")

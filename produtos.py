import os
import time

from banco import conexao, cursor

from utils import (
    ler_preco,
    ler_quantidade
)

produtos_lista = []


def cadastrar_produto():

    nome = input("Nome do produto: ")

    preco = ler_preco()

    quantidade = ler_quantidade(
        "Quantidade: "
    )

    produtos_lista.append(
        [nome, preco, quantidade]
    )

    cursor.execute("""
    INSERT INTO produtos
    (nome, preco, quantidade)

    VALUES (?, ?, ?)
    """, (nome, preco, quantidade))

    conexao.commit()

    print("Produto cadastrado!")

    mostrar_estoque_atualizado()


def listar_produtos():

    cursor.execute("""
    SELECT * FROM produtos
    """)

    produtos = cursor.fetchall()

    print("\n=== ESTOQUE ===")

    for produto in produtos:

        print(produto)


def mostrar_estoque_atualizado():

    cursor.execute("""
    SELECT id, nome, quantidade
    FROM produtos
    """)

    produtos = cursor.fetchall()

    print("\n=== ESTOQUE ATUALIZADO ===")

    for produto in produtos:

        print(
            f"ID: {produto[0]} | "
            f"Produto: {produto[1]} | "
            f"Quantidade: {produto[2]}"
        )


def entrada_produto():

    id_produto = int(
        input("ID do produto: ")
    )

    entrada = int(
        input("Quantidade de entrada: ")
    )

    cursor.execute("""
    UPDATE produtos

    SET quantidade = quantidade + ?

    WHERE id = ?
    """, (entrada, id_produto))

    conexao.commit()

    print("Entrada realizada!")

    mostrar_estoque_atualizado()


def saida_produto():

    id_produto = int(
        input("ID do produto: ")
    )

    saida = int(
        input("Quantidade de saída: ")
    )

    cursor.execute("""
    SELECT quantidade

    FROM produtos

    WHERE id = ?
    """, (id_produto,))

    resultado = cursor.fetchone()

    if resultado is None:

        print("Produto não encontrado!")

        return

    estoque_atual = resultado[0]

    if saida > estoque_atual:

        print("Estoque insuficiente!")

    else:

        cursor.execute("""
        UPDATE produtos

        SET quantidade = quantidade - ?

        WHERE id = ?
        """, (saida, id_produto))

        conexao.commit()

        print("Saída realizada!")

        mostrar_estoque_atualizado()


def verificar_estoque():

    cursor.execute("""
    SELECT nome, quantidade

    FROM produtos

    WHERE quantidade <= 5
    """)

    produtos = cursor.fetchall()

    print("\n=== ESTOQUE BAIXO ===")

    for produto in produtos:

        print(produto)


def monitor_estoque():

    while True:

        os.system("cls")

        cursor.execute("""
        SELECT id, nome, quantidade
        FROM produtos
        """)

        produtos = cursor.fetchall()

        print(
            "=== MONITORAMENTO "
            "DE ESTOQUE ===\n"
        )

        for produto in produtos:

            print(
                f"ID: {produto[0]} | "
                f"Produto: {produto[1]} | "
                f"Quantidade: {produto[2]}"
            )

        print(
            "\nAtualizando em "
            "tempo real..."
        )

        time.sleep(2)

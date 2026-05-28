import pandas as pd

from banco import conexao


def relatorio():

    df = pd.read_sql_query(
        "SELECT * FROM produtos",
        conexao
    )

    print(df)

    valor_total = (
        df["preco"] * df["quantidade"]
    ).sum()

    print("\nValor total do estoque:")

    print(valor_total)

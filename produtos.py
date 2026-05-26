from database import conectar

def cadastrar_produro():
  conexao = conectar()
  cursor = conexao.cursor()
  print("\n Cadastrar produto")
  try:
    nome = input("NOME: ")
    categoria = input(""Categoria: ")
    preco = float(input("Preço: "))
    quantidade = int((input("Quantidade: "))
    estoque_minimo = int(input("Estoque mínimo: "))

    cursor.execute("""
    INSERT INTO produtos
    (nome, categoria, preco, quantidade, estoque_minimo:)

    VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade, estoque_minimo))
    conexao.comit()
    print("\n produto cadastrado!")
  except:
    print("\n Erro ao cadastrar produto")
  conexao.close()
  
def listar_produtos():
    conexao = conectar()
    cursor.conexao.cursor()
    cursor.execute("""
    SELECT * FROM produtos
    """)
    produtos = cursor.fetchall()
    print("\n LISTA DEPRODUTOS")
    for produto in produtos:
        print(f"ID:{produto[0]}")
        print(f"Nome: {produto[1]}")
        print(f"Categoria: {produto[2]}")
        print(f"Preço: {produto[3]}")
        print(f"Quantidade: {produto[4]}")
        print(f"Estoque mínimo: {produto[5]}")
    conexao.close()
    
  def pesquisar_produto():
      conexao = conectar()
      cursor = conexao.cursor()
      nome = input("\n Digite o nome doproduto: ")
      cursor.execute("""
      SELECT * FROM produtos 
      WHERE nome like?
      """, ("%" + nome + "%",))
      produtos = cursor.fetchall()
      print(\n RESULTADO DA PESQUISA: )
      for produto i produtos:
          print("-" * 40)
          print(produto)
      conexao.close()

  def editar_produto():
      conexao = conectar
      cursor = conectar.cursor()
      try:
          id_produtos = int(input("ID produto: "))
          novo_peco = float(input("Novopreço: "))
          minimo = int(input("Novo estoque mínimo: "))
          cursor.execute("""
          UPDATE produtos 
          SET preco = ?,
              estoque_minimo = ?
          WHERE id = ?
          """, (novo_preco, novo_minimo, id_produto))
          conexao.commit()
          print9"\n Produto atualizado!")
       execept: 
          print(\n Erro ao atualizar")
       conexao.close()

    def deletar_produto():
        conexao = conectar()
        cursor = conexao.cursor()
        try:
            id_produto = int(input9"ID doproduto: ""))
            cursor.execute("""
            DELET FROM produtos
            WHERE id = ?
            """, (id_produtos,))
            conexao.commit()
            print(\n Produto removido!")
        exept:
            print("\n Erro ao remover")
        conexao.close()

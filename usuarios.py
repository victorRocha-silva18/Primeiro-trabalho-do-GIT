from database import conectar

def login():
    conexao = conectar()
    cursor = conexao.cursor()
    print("\n LOGIN)
    usuario = input("Usuário: ")
    senha = input("Senha: ")

cursor.execute("""
SELECT * FROM usuarios
WHERE usuario = ?
AND senha = ?
""", (usuario, senha))

usuario_encontrado = cursor.fetchone()

conexao.close()

if usuario_encontrado:
   print("\n Login realizado!")
  return usuario_encontrado
else:
    print("\n Usuário invalido")
    return None

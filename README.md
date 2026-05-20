 Sistema de Controle de Estoque em Python

Sistema de gerenciamento de estoque desenvolvido em Python com foco em controle de produtos, movimentação de entrada e saída, análise de dados e persistência em arquivos.

O projeto foi desenvolvido com objetivo acadêmico e prático, aplicando conceitos de:

- Programação em Python
- Estruturas de dados
- Manipulação de tabelas com Pandas
- Organização modular
- CRUD de produtos
- Automação de estoque
- Tratamento de dados
- Lógica de negócio

 Funcionalidades



Tecnologias Utilizadas

- Python 3.x
- Pandas
- Google Colab
- Git & GitHub
- ChatGPT
  
Estrutura do Projeto
```bash
📁 sistema-estoque/
│
├── estoque.ipynb
├── produtos.csv
├── README.md
└── requirements.txt
```

---
 Como Executar o Projeto

 Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

---

 Acesse a pasta

```bash
cd NOME-DO-REPOSITORIO
```

---

Instale as dependências

```bash
pip install pandas
```

Ou:

```bash
pip install -r requirements.txt
```

---

 Execute o projeto

Caso esteja usando:

 Google Colab

Abra o arquivo `.ipynb` no Google Colab.

 VS Code / Terminal

```bash
python nome_do_arquivo.py
```

---

 Conceitos Aplicados

 CRUD

O sistema implementa operações de:

- Create → Cadastro de produtos
- Read → Consulta de informações
- Update → Atualização de estoque
- Delete → Remoção de produtos

---

 Pandas

A biblioteca Pandas foi utilizada para:

- Organização tabular dos dados
- Leitura e escrita de arquivos CSV
- Manipulação de estoque
- Filtragem e atualização de registros
- Estruturação dos relatórios

Exemplo:

```python
df = pd.read_csv("produtos.csv")
```

---

 Fluxo do Sistema

```text
Usuário
   ↓
Interface/Menu
   ↓
Funções do Sistema
   ↓
Manipulação dos Dados
   ↓
Atualização do Estoque
   ↓
Salvamento em CSV
```

---

 Exemplo de Funcionamento

Cadastro de Produto

```python
Produto: Mouse Gamer
Quantidade: 10
Preço: 150
```

 Saída de Estoque

```python
Produto removido do estoque com sucesso.
Quantidade atualizada.
```

---

 Principais Funções do Projeto

| Função | Responsabilidade |

| cadastrar_produto() | Adiciona novos produtos |
| remover_produto() | Remove produtos |
| atualizar_estoque() | Atualiza quantidades |
| listar_produtos() | Exibe os produtos |
| salvar_dados() | Salva no CSV |
| carregar_dados() | Lê os dados salvos |

---

 Arquitetura do Projeto

O projeto segue uma arquitetura simples baseada em separação de responsabilidades:

- Entrada de dados
- Regras de negócio
- Manipulação do DataFrame
- Persistência dos arquivos


 Melhorias Futuras

- [ ] Interface gráfica
- [ ] Integração com banco de dados
- [ ] Sistema web com Flask/Django
- [ ] Controle de usuários
- [ ] Dashboard de relatórios
- [ ] API REST
- [ ] Deploy online


Objetivo do Projeto

Este projeto foi desenvolvido para aprimorar conhecimentos em:

- Programação Python
- Manipulação de dados
- Estruturas condicionais e de repetição
- Modularização
- Versionamento com Git/GitHub
- Desenvolvimento de sistemas reais


 Autor

Desenvolvido por Victor Rocha da Silva

GitHub:

LinkedIn:

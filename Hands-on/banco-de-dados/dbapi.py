import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent
DB_PATH = ROOT_PATH / "banco-de-dados" / "meu_banco.db"

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()


def criar_tabela(con, cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    con.commit()


def inserir_dados(con, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    con.commit()


def atualizar_dados(con, cursor, id, nome, email):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?;", data)
    con.commit()


def excluir_dados(con, cursor, id):
    data = (
        id,
    )  # nesse caso, a vírgula é necessária para indicar que é uma tupla de um único elemento
    cursor.execute("DELETE FROM clientes WHERE id = ?;", data)  # separamos
    con.commit()



# Utiliza a func atualizar_dados para atualizar o cliente com id 1 "João" e email "joao@exemplo.com" para João Silva e "joao@teste.com"
# atualizar_dados(con, cursor, 1, "João Silva", "joao@teste.com")
# # Utiliza a func atualizar_dados para atualizar o cliente com id 2 "Giovana" e email "giovana@exemplo.com" para Giovanna Jardim e "giovanna@teste.com"
# atualizar_dados(con, cursor, 2, "Giovanna Jardim", "giovanna@teste.com")


# Utiliza a func excluir_dados para excluir o cliente com id 1
# excluir_dados(con, cursor, 1)

# Utiliza a func inserir_dados para inserir um novo cliente com nome "João" e email "joao@exemplo.com" - um usuário que já existia antes do delete
# inserir_dados(con, cursor, "João", "joao@exemplo.com")
# Executei apenas para mostrar que o "autoincrement" faz com que, mesmo que o id 1 tenha sido excluído,
# e um novo usuário seja inserido, (mesmo que com o mesmo dado e email de um usuário que já existia), o id será 3 ao invés de 1.

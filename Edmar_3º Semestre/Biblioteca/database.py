import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")
def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS usuarios
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   matricula TEXT UNIQUE NOT NULL)
                   ''')
    cursor.execute('''
                  CREATE TABLE IF NOT EXISTS livros (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   titulo TEXT NOT NULL,
                   autor TEXT NOT NULL,
                   ano INTEGER,
                   disponivel INTEGER DEFAULT 1)
                   ''')
                 
    cursor.execute(''' 
                   CREATE TABLE IF NOT EXISTS emprestimos (
                   id INTEGER PRIMARY KEY AUTO INCREMENT,
                   usuario_id INTEGER,
                   livro_id INTEGER,
                   data_emprestimos TEXT,
                   data_devolucao TEXT,
                   FOREIGN KEY(usuario_id) references usuarios(id),
                   FOREIGN KEY(livros_id) references livros(id))
                   ''')
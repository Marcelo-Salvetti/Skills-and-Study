from database import conectar

def cadastrar_livre():
    titulo = input("Titulo do livro:")
    autor = input("Autor: ")
    ano = int(input("Ano de publicação: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros(titulo, autor, ano) VALUES(?, ?,?)", (titulo, autor, ano))
    conn.commit()
    print("Livro cadastrado com sucesso!")
    conn.close()

def listar_livros_disponiveis():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM livros WHERE disponivel = 1")
    livros = cursor.fetchall()

    if livros:
        print("Livros disponiveis: ")
        for livro in livros:
            print(f"{livro[0]} - {livro[1]}")
    else:
        print("Nenhum Livro disponivel!")    

    conn.close()            


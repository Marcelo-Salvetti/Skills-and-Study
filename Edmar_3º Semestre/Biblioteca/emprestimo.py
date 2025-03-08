from database import conectar
from datetime import datetime

def emprestar_livros():
    usuario_id = input("ID do usuario: ")
    livro_id = input("ID do livro: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(" SELECT disponivel FROM livros WHERE id = ?",(livro_id,))
    livro = cursor.fetchone()
    if livro and livro[0] == 1:
        data_emprestimo = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO emprestimos(usuario_id,livro_id,data_emprestimo) VALUES(?,?,?)",(usuario_id,livro_id,data_emprestimo))
        cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = ?",(livro_id,))
        conn.commit()
        print("Emprestimo realizado com sucesso!!")
    else:
        print("Erro: Livro não disponivel! ")
    conn.close()    

def devolver_livros():
    livro_id = input("ID do livro a ser devolvido: ")
    
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM emprestimos WHERE livro_id = ? AND data_devolucao IS NULL",(livro_id,))
    emprestimo = cursor.fetchone()
    if emprestimo:
        data_devolucao = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",(data_devolucao, emprestimo[0]))
        cursor.execute("UPDATE livros SET disponivel = 1 WHERE id = ?", (livro_id,))
        conn.commit()
        print("Livro devolvido com sucesso!")
    else:
        print("Erro: Livro não encontrado!")    
    conn.close()
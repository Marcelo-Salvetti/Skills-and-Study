from database import conectar

def cadastrar_usuario():
    nome = input("Nome do usuario")
    matricula = input("Matricula: ")
    
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios(nome, matricula) VALUES(?, ?)",(nome, matricula))
        conn.commit()
        print("Usuario cadastrado com sucesso!")

    except:
        print("Ocorreu um erro ao cadastrar o usuario.")

    conn.close()    

import sqlite3

def adicionar_paciente(nome, idade, cpf):
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pacientes(nome, idade, cpf) VALUES(?,?,?)", (nome, idade, cpf))
    conn.commit()
    conn.close()

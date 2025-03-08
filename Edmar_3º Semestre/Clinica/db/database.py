import sqlite3

def criar_banco():
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pacientes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   idade INTEGER,
                   cpf TEXT)''')
   
    cursor.execute('''CREATE TABLE IF NOT EXISTS medicos(
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nome TEXT,
                  especialidade TEXT, )''')
    
    cursor.execute(''' CREATE TABLE IF NOT EXISTS consultas(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   paciente_id INTEGER,
                   medico_id INTEGER,
                   data TEXT,
                   FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
                   FOREIGN KEY(medico_id) REFERENCES medicos(id))
                   ''')
    conn.commit()
    conn.close()

criar_banco()

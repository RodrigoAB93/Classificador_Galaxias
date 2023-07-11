import sqlite3

# Conectar-se ao banco de dados ou criar um novo  banco de dados
conn = sqlite3.connect('classificadorgalaxias.db')

# Criar um cursor para executar comandos
cursor = conn.cursor()

# Criar tabela com os campos especificados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        u REAL,
        r REAL,
        g REAL,
        i REAL,
        z REAL,
        deVAB_u REAL,
        deVAB_g REAL,
        deVAB_r REAL,
        deVAB_i REAL,
        deVAB_z REAL,
        mCr4_u REAL,
        mCr4_g REAL,
        mCr4_r REAL,
        mCr4_i REAL,
        mCr4_z REAL,
        petroR50_r REAL,
        petroR90_r REAL,
        petroR50_u REAL,
        petroR90_u REAL,
        petroR50_z REAL,
        petroR90_z REAL
        
    )
''')

conn.commit()
conn.close()


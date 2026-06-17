# criar_tabela_simples.py
import sqlite3

conn = sqlite3.connect("quantex.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        term VARCHAR,
        ticker VARCHAR,
        headline VARCHAR,
        explanation TEXT,
        result VARCHAR
    )
""")

conn.commit()
conn.close()

print("✅ Tabela 'news' criada com sucesso!")
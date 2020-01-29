import psycopg2

# Open communication with the database
conn = psycopg2.connect(host = 'localhost', database = 'estudos', user = 'postgres', password = 'postgres')
cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY, 
    name TEXT NOT NULL, 
    email TEXT NOT NULL, 
    username TEXT NOT NULL, 
    password TEXT NOT NULL
  );
""")

print("Conectado ao banco de dados...")

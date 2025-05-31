import psycopg2
from psycopg2 import sql

# Conexión directamente a tu base de datos del proyecto
conn = psycopg2.connect(
    dbname="axyoma",  # ESTA es tu base de datos real
    user="postgres",  # Superusuario
    password="123456789",  # Cambia si es diferente
    host="localhost",
    port="5432"
)

conn.autocommit = True
cur = conn.cursor()

# Usuario de Django al que le quieres dar permisos
usuario_django = "axyoma_user"

# Dar permisos completos sobre el esquema `public` de axyoma
cur.execute(sql.SQL("GRANT ALL ON SCHEMA public TO {};").format(sql.Identifier(usuario_django)))

print("✅ Permisos asignados correctamente en la base de datos 'axyoma'.")
cur.close()
conn.close()

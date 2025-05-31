import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

SUPERUSER = 'postgres'         # Usuario administrador de postgres
SUPERPASS = '123456789'  # Cambia aquí por tu contraseña
HOST = 'localhost'
PORT = '5432'

NEW_USER = 'axyoma_user'
NEW_PASS = '123456789'
NEW_DB = 'axyoma'

def create_user_and_db():
    try:
        con = psycopg2.connect(
            dbname='postgres',
            user=SUPERUSER,
            password=SUPERPASS,
            host=HOST,
            port=PORT
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        # Crear usuario si no existe
        cur.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (NEW_USER,))
        if not cur.fetchone():
            cur.execute(f"CREATE USER {NEW_USER} WITH PASSWORD %s", (NEW_PASS,))
            cur.execute(f"ALTER USER {NEW_USER} CREATEDB")
            print(f"Usuario '{NEW_USER}' creado y permisos asignados.")
        else:
            print(f"Usuario '{NEW_USER}' ya existe.")

        # Crear base de datos si no existe
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (NEW_DB,))
        if not cur.fetchone():
            cur.execute(f'CREATE DATABASE "{NEW_DB}" OWNER {NEW_USER}')
            print(f"Base de datos '{NEW_DB}' creada con propietario '{NEW_USER}'.")
        else:
            print(f"Base de datos '{NEW_DB}' ya existe.")

        cur.close()
        con.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    create_user_and_db()

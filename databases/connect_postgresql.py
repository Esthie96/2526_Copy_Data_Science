import psycopg2
from psycopg2 import sql

# Connection parameters
conn_parameters = {
    'host': 'db.rqexamkwhkugvqqrvdsr.supabase.co',
    'database': 'postgres',
    'user': 'Esthie96',
    'password': 'Kt#7Lr3dWX3zq-k',
    'port': '5432'
}

try:
    # Establish connection
    conn = psycopg2.connect(**conn_parameters)
    cursor = conn.cursor()
    
    # Execute a query
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"PostgreSQL version: {version[0]}")
    
    # Close connections
    cursor.close()
    conn.close()
    
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")

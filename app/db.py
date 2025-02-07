import os
import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    """Get a connection to the CockroachDB cluster."""
    user = os.getenv("CRDB_USER", "root")
    host1 = os.getenv("CRDB_HOST_NODE1", "node1")
    dbname = "hashdb"  # or get from env

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        host=host1, 
        port=os.getenv("CRDB_SQL_PORT", "26257"),
        # password=os.getenv("CRDB_PASSWORD", ""),  # if needed
        sslmode="disable"  # in insecure mode
    )
    return conn

def init_db():
    """(Optional) Create tables if not already existing. Alternatively use init script."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS device_hashes (
        id SERIAL PRIMARY KEY,
        user_id VARCHAR(255) NOT NULL,
        device_id VARCHAR(255) NOT NULL,
        hash_value TEXT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT now()
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE DATABASE IF NOT EXISTS hashdb;")
            cur.execute("USE hashdb;")
            cur.execute(create_table_sql)
        conn.commit()

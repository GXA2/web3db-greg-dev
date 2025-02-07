from db import get_connection

def get_latest_hash(user_id: str, device_id: str):
    """
    Returns the latest hash version for the given user_id/device_id.
    If none exist, returns None.
    """
    query = """
        SELECT hash_value
        FROM device_hashes
        WHERE user_id = %s AND device_id = %s
        ORDER BY created_at DESC
        LIMIT 1;
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (user_id, device_id))
            result = cur.fetchone()
            if result:
                return result[0]  # hash_value
            else:
                return None

def add_hash(user_id: str, device_id: str, hash_value: str):
    """
    Adds a hash to the database, along with user/device IDs and a timestamp.
    """
    insert_sql = """
        INSERT INTO device_hashes (user_id, device_id, hash_value)
        VALUES (%s, %s, %s);
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(insert_sql, (user_id, device_id, hash_value))
        conn.commit()

if __name__ == "__main__":
    # Simple CLI or usage demonstration:
    import sys
    if len(sys.argv) < 2:
        print("Usage: python main.py [get|add] args...")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "get":
        # e.g. python main.py get user123 deviceA
        user_id = sys.argv[2]
        device_id = sys.argv[3]
        latest = get_latest_hash(user_id, device_id)
        print("Latest hash:", latest)
    elif cmd == "add":
        # e.g. python main.py add user123 deviceA SomeHashValue
        user_id = sys.argv[2]
        device_id = sys.argv[3]
        hash_val = sys.argv[4]
        add_hash(user_id, device_id, hash_val)
        print(f"Hash '{hash_val}' added for user '{user_id}' / device '{device_id}'.")
    else:
        print("Unknown command.")

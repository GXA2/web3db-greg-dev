import random
import string
from main import add_hash

def random_hash(length=16):
    """Generate a random alphanumeric string of given length."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_test_data():
    # We can simulate a few user/device combos
    user_device_pairs = [
        ("user1", "deviceA"),
        ("user1", "deviceB"),
        ("user2", "deviceC"),
        ("user3", "deviceA"),
    ]

    for (u, d) in user_device_pairs:
        # Insert multiple times so there's a 'latest'
        for _ in range(3):
            hash_val = random_hash()
            add_hash(u, d, hash_val)
            print(f"Inserted hash '{hash_val}' for user='{u}' / device='{d}'.")

if __name__ == "__main__":
    generate_test_data()

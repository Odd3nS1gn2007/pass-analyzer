import hashlib
import os


COMMON_PASSWORD_FILE = "common_passwords.txt"
PASSWORD_HISTORY_FILE = "password_history.bin"


def hash_password(password):
    return hashlib.sha256(password.encode()).digest()


def is_common_password(password):
    if not os.path.exists(COMMON_PASSWORD_FILE):
        return False

    with open(COMMON_PASSWORD_FILE, "r") as file:
        common_passwords = file.read().splitlines()

    common_passwords = [pwd.lower() for pwd in common_passwords]

    return password.lower() in common_passwords


def is_reused_password(password):
    if not os.path.exists(PASSWORD_HISTORY_FILE):
        return False

    hashed_password = hash_password(password)

    with open(PASSWORD_HISTORY_FILE, "rb") as file:
        while True:
            stored_hash = file.read(32)

            if not stored_hash:
                break

            if stored_hash == hashed_password:
                return True

    return False


def store_password(password):
    hashed_password = hash_password(password)

    with open(PASSWORD_HISTORY_FILE, "ab") as file:
        file.write(hashed_password)
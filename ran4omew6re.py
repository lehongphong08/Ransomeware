from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        # Đọc dữ liệu từ tập tin
        file_data = file.read()

    
    encrypted_data = f.encrypt(file_data)

    
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        # Đọc dữ liệu từ tập tin
        encrypted_data = file.read()

    
    decrypted_data = f.decrypt(encrypted_data)

    
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt(file_path, key)


def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt(file_path, key)


def main():
    generate_key()
    key = load_key()

    
    encrypt_directory("hphong", key)

    
    decrypt_directory("hphong", key)

if __name__ == "__main__":
    main()

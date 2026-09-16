import hashlib
import hmac
import os

def generate_file_hashes(file_path, hmac_key):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' tidak ditemukan.")
        return

    with open(file_path, 'rb') as f:
        file_data = f.read()

    # SHA
    sha1_hash = hashlib.sha1(file_data).hexdigest()

    # MD-5
    md5_hash = hashlib.md5(file_data).hexdigest()

    # HMAC-SHA256
    key_bytes = hmac_key.encode('utf-8')
    hmac_hash = hmac.new(key_bytes, file_data, hashlib.sha256).hexdigest()

    print(f"Target File : {file_path}")
    print("-" * 50)
    print(f"SHA1        : {sha1_hash}")
    print(f"MD5         : {md5_hash}")
    print(f"HMAC-SHA256 : {hmac_hash}")
    print("-" * 50)

nama_file_gambar = "PPBS UNPAD.jpg" 
kunci = "kripto2026"

generate_file_hashes(nama_file_gambar, kunci)
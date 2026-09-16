def clean_text(text):
    return ''.join(char for char in text.upper() if char.isalpha())


def find_ciphertext(plaintext, key):
    plaintext = clean_text(plaintext)
    key = clean_text(key)
    result = []
    for i, char in enumerate(plaintext):
        shift = ord(key[i % len(key)]) - ord('A')
        c = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        result.append(c)
    return ''.join(result)


def find_plaintext(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    key = clean_text(key)
    result = []
    for i, char in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) - ord('A')
        p = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        result.append(p)
    return ''.join(result)


def find_key(plaintext, ciphertext):
    plaintext = clean_text(plaintext)
    ciphertext = clean_text(ciphertext)

    if len(plaintext) != len(ciphertext):
        return "Error: panjang plaintext dan ciphertext harus sama!"

    result = []
    for p_char, c_char in zip(plaintext, ciphertext):
        shift = (ord(c_char) - ord(p_char)) % 26
        k = chr(shift + ord('A'))
        result.append(k)
    return ''.join(result)


def menu():
    while True:
        print("\n******** MENU VIGENERE CIPHER ********")
        print("1. Cari Ciphertext (Enkripsi)")
        print("2. Cari Plaintext (Dekripsi)")
        print("3. Cari Key")
        print("4. Keluar")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            pt = input("Masukkan Plaintext : ")
            key = input("Masukkan Key       : ")
            ct = find_ciphertext(pt, key)
            print(f"\nHasil Ciphertext   : {ct}")

        elif pilihan == '2':
            ct = input("Masukkan Ciphertext: ")
            key = input("Masukkan Key       : ")
            pt = find_plaintext(ct, key)
            print(f"\nHasil Plaintext    : {pt}")

        elif pilihan == '3':
            pt = input("Masukkan Plaintext : ")
            ct = input("Masukkan Ciphertext: ")
            key = find_key(pt, ct)
            print(f"\nHasil Key          : {key}")

        elif pilihan == '4':
            print("Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu()
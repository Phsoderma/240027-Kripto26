import numpy as np

def text_to_numbers(text):
    text = text.upper().replace(" ", "")
    return [ord(char) - ord('A') for char in text if char.isalpha()]

def numbers_to_text(numbers):
    return "".join([chr(int(num) + ord('A')) for num in numbers])

def mod_inverse(a, m=26):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, m=26):
    det = int(np.round(np.linalg.det(matrix))) % m
    det_inv = mod_inverse(det, m)
    
    if det_inv is None:
        return None

    adj = np.array([[matrix[1, 1], -matrix[0, 1]],
                    [-matrix[1, 0], matrix[0, 0]]]) % m

    inv_matrix = (det_inv * adj) % m
    return inv_matrix.astype(int)

def encrypt_hill(plaintext, key_matrix):
    nums = text_to_numbers(plaintext)
    if len(nums) % 2 != 0:
        nums.append(ord('X') - ord('A'))
    
    ciphertext = []
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2])
        encrypted_pair = np.dot(key_matrix, pair) % 26
        ciphertext.extend(encrypted_pair)
        
    return numbers_to_text(ciphertext)

def decrypt_hill(ciphertext, key_matrix):
    inv_key = matrix_mod_inverse(key_matrix)

    if inv_key is None:
        print("\n[!] Error: Kunci tidak memiliki invers modulo 26 (Determinan tidak relatif prima dengan 26).")
        return None
    
    nums = text_to_numbers(ciphertext)
    plaintext = []
    
    for i in range(0, len(nums), 2):
        pair = np.array(nums[i:i+2])
        decrypted_pair = np.dot(inv_key, pair) % 26
        plaintext.extend(decrypted_pair)
        
    return numbers_to_text(plaintext)

def find_key_algebraic(plaintext, ciphertext):
    pt_nums = text_to_numbers(plaintext)
    ct_nums = text_to_numbers(ciphertext)
    
    if len(pt_nums) < 4 or len(ct_nums) < 4:
        print("\n[!] Dibutuhkan minimal 4 karakter Plaintext dan Ciphertext!")
        return None

    P = np.array([
        [pt_nums[0], pt_nums[2]],
        [pt_nums[1], pt_nums[3]]
    ])
    
    C = np.array([
        [ct_nums[0], ct_nums[2]],
        [ct_nums[1], ct_nums[3]]
    ])
    
    P_inv = matrix_mod_inverse(P, 26)
    
    if P_inv is None:
        print("\n[!] Matriks Plaintext (P) tidak memiliki invers mod 26.")
        print("    Coba gunakan pasangan huruf yang berbeda sebagai awal kalimat!")
        return None

    K = np.dot(C, P_inv) % 26
    return K.astype(int)

def main():
    while True:
        print("\n" + "="*35)
        print("      PROGRAM HILL CIPHER 2x2")
        print("="*35)
        print("1. Enkripsi Pesan")
        print("2. Dekripsi Pesan")
        print("3. Cari Kunci")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ").strip()
        
        if pilihan == '1':
            pt = input("\nMasukkan Plaintext: ")
            print("Masukkan Matriks Kunci 2x2:")
            k11 = int(input("K[0,0]: "))
            k12 = int(input("K[0,1]: "))
            k21 = int(input("K[1,0]: "))
            k22 = int(input("K[1,1]: "))
            
            key = np.array([[k11, k12], [k21, k22]])
            result = encrypt_hill(pt, key)
            print(f"\n[+] Hasil Ciphertext: {result}")
            
        elif pilihan == '2':
            ct = input("\nMasukkan Ciphertext: ")
            print("Masukkan Matriks Kunci 2x2:")
            k11 = int(input("K[0,0]: "))
            k12 = int(input("K[0,1]: "))
            k21 = int(input("K[1,0]: "))
            k22 = int(input("K[1,1]: "))
            
            key = np.array([[k11, k12], [k21, k22]])
            result = decrypt_hill(ct, key)
            if result:
                print(f"\n[+] Hasil Plaintext: {result}")
                
        elif pilihan == '3':
            pt = input("Masukkan Plaintext (misal: FRIDAY): ")
            ct = input("Masukkan Ciphertext (misal: PQCFKU): ")
            
            key = find_key_algebraic(pt, ct)
            if key is not None:
                print("\n[+] Matriks Kunci (K) Ditemukan:")
                print(key)
                
        elif pilihan == '4':
            print("\nTerima kasih!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
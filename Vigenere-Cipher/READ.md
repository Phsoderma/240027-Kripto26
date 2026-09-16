# Vigenère Cipher — Python

Program sederhana berbasis menu untuk melakukan enkripsi, dekripsi, dan pencarian kunci menggunakan algoritma **Vigenère Cipher**.

## Daftar Isi

- [Tentang Program](#tentang-program)
- [Fitur](#fitur)
- [Konsep Dasar Algoritma](#konsep-dasar-algoritma)
- [Struktur Fungsi](#struktur-fungsi)
- [Cara Menjalankan](#cara-menjalankan)
- [Contoh Penggunaan](#contoh-penggunaan)
- [Batasan Program](#batasan-program)

## Tentang Program

Vigenère Cipher adalah teknik penyandian (cipher) klasik yang menggunakan kata kunci (key) untuk menggeser setiap huruf pada plaintext secara berulang. Program ini mengimplementasikan tiga operasi utama:

1. **Enkripsi** — mengubah plaintext menjadi ciphertext menggunakan key
2. **Dekripsi** — mengubah ciphertext kembali menjadi plaintext menggunakan key
3. **Pencarian Key** — menemukan key yang digunakan jika plaintext dan ciphertext sudah diketahui

## Fitur

- Menu interaktif berbasis teks (CLI)
- Mendukung input huruf besar/kecil (otomatis dinormalisasi ke kapital)
- Otomatis membersihkan spasi dan karakter non-alfabet dari input
- Kunci berulang otomatis mengikuti panjang teks

## Konsep Dasar Algoritma

Setiap huruf direpresentasikan sebagai angka: `A = 0, B = 1, ..., Z = 25`.

### Rumus Enkripsi

```
C[i] = (P[i] + K[i]) mod 26
```

### Rumus Dekripsi

```
P[i] = (C[i] - K[i]) mod 26
```

### Rumus Pencarian Key

```
K[i] = (C[i] - P[i]) mod 26
```

Keterangan:
- `P[i]` = nilai huruf plaintext pada posisi ke-i
- `C[i]` = nilai huruf ciphertext pada posisi ke-i
- `K[i]` = nilai huruf key pada posisi ke-i (key diulang menggunakan `i % len(key)`)

### Ilustrasi Perulangan Key

Jika key adalah `KUNCI` (panjang 5) dan teks memiliki 10 huruf, maka key akan diulang sebagai berikut:

| Index (i)      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|----------------|---|---|---|---|---|---|---|---|---|---|
| i % 5          | 0 | 1 | 2 | 3 | 4 | 0 | 1 | 2 | 3 | 4 |
| Huruf key ke-  | K | U | N | C | I | K | U | N | C | I |

## Struktur Fungsi

| Fungsi | Deskripsi |
|---|---|
| `clean_text(text)` | Menghapus spasi/simbol dan mengubah teks menjadi kapital semua |
| `find_ciphertext(plaintext, key)` | Menghitung ciphertext dari plaintext dan key |
| `find_plaintext(ciphertext, key)` | Menghitung plaintext dari ciphertext dan key |
| `find_key(plaintext, ciphertext)` | Menghitung key dari plaintext dan ciphertext |
| `menu()` | Menampilkan menu interaktif dan mengarahkan ke fungsi yang sesuai |

## Cara Menjalankan

1. Pastikan Python sudah terinstal (Python 3.x)
2. Simpan kode program ke dalam file, misalnya `vigenere.py`
3. Jalankan melalui terminal:

```bash
python vigenere.py
```

4. Ikuti menu yang muncul:

```
******** MENU VIGENERE CIPHER ********
1. Cari Ciphertext (Enkripsi)
2. Cari Plaintext (Dekripsi)
3. Cari Key
4. Keluar
Pilih menu (1-4):
```

## Contoh Penggunaan

### 1. Mencari Ciphertext (dari Plaintext + Key)

```
Pilih menu (1-4): 1
Masukkan Plaintext : Hello World
Masukkan Key       : KUNCI

Hasil Ciphertext   : RYTNWYQZLT
```

### 2. Mencari Plaintext (dari Ciphertext + Key)

```
Pilih menu (1-4): 2
Masukkan Ciphertext: RYTNWYQZLT
Masukkan Key       : KUNCI

Hasil Plaintext    : HELLOWORLD
```

### 3. Mencari Key (dari Plaintext + Ciphertext)

```
Pilih menu (1-4): 3
Masukkan Plaintext : HELLOWORLD
Masukkan Ciphertext: RYTNWYQZLT

Hasil Key          : KUNCIKUNCI
```

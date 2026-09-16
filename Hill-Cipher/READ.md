# Alur Kerja Program Hill Cipher

Berikut adalah penjelasan alur kerja program Hill Cipher 2x2 berdasarkan fungsi dan nilai/formula yang ada pada kode Python.

---

## 1. Menu Interaktif

Program berjalan dalam *looping* (perulangan) menu utama dan mengeksekusi fungsi sesuai opsi yang dipilih oleh pengguna:

* **Pilihan 1 (Enkripsi):** Meminta input *plaintext* dan 4 nilai matriks kunci, lalu memanggil fungsi `encrypt_hill`.
* **Pilihan 2 (Dekripsi):** Meminta input *ciphertext* dan 4 nilai matriks kunci, lalu memanggil fungsi `decrypt_hill`.
* **Pilihan 3 (Cari Kunci):** Meminta input *plaintext* dan *ciphertext* (minimal 4 karakter), lalu memanggil fungsi `find_key_algebraic`.
* **Pilihan 4 (Keluar):** Mengakhiri program.

---

## 2. Fungsi Enkripsi (`encrypt_hill`)

1. **Konversi Teks:** Memanggil `text_to_numbers` untuk mengubah *plaintext* menjadi array angka ($A=0, B=1, \dots, Z=25$).
2. **Padding:** Mengecek panjang array angka. Jika ganjil (tidak habis dibagi 2), karakter `'X'` (nilai 23) ditambahkan ke akhir array.
3. **Proses Perkalian Blok:**
   * Program mengambil setiap pasang angka (2 angka) sebagai vektor kolom.
   * Melakukan perkalian matriks: $(K \times \text{vektor}) \pmod{26}$.
4. **Hasil:** Memanggil `numbers_to_text` untuk mengonversi angka hasil perkalian kembali menjadi string *ciphertext*.

### Output Menu 1 (Enkripsi):
![Output Menu 1](assets/Output%20Menu%201.png)

---

## 3. Fungsi Dekripsi (`decrypt_hill`)

1. **Hitung Matriks Invers ($K^{-1}$):**
   * Memanggil `matrix_mod_inverse(key_matrix)` untuk menghitung $K^{-1} \pmod{26}$.
   * Menghitung determinan matriks $K$: $\text{det} = (ad - bc) \pmod{26}$.
   * Mencari nilai invers modular dari determinan tersebut terhadap 26 (`mod_inverse`).
   * Jika invers determinan tidak ada, program menampilkan pesan peringatan bahwa kunci tidak valid dan menghentikan dekripsi.
   * Jika ada, hitung matriks adjoint dan kalikan dengan invers determinan.
2. **Konversi Teks:** Mengubah *ciphertext* menjadi array angka dengan `text_to_numbers`.
3. **Proses Perkalian Blok:**
   * Mengambil setiap pasang angka *ciphertext*.
   * Melakukan perkalian matriks: $(K^{-1} \times \text{vektor}) \pmod{26}$.
4. **Hasil:** Mengonversi hasil angka kembali ke bentuk string *plaintext* dengan `numbers_to_text`.

### Output Menu 2 (Dekripsi):
![Output Menu 2](assets/Output%20Menu%202.png)

---

## 4. Fungsi Mencari Kunci (`find_key_algebraic`)

Fungsi ini mencari matriks kunci $K$ menggunakan rumus $K = (C \cdot P^{-1}) \pmod{26}$ berdasarkan sampel *plaintext* dan *ciphertext*:

1. **Validasi Input:** Mengecek apakah panjang *plaintext* dan *ciphertext* minimal 4 karakter.
2. **Penyusunan Matriks $P$ dan $C$:**
   * Mengambil 4 angka pertama dari *plaintext* ($p_1, p_2, p_3, p_4$) dan menyusun matriks $P$:
   * Mengambil 4 angka pertama dari *ciphertext* ($c_1, c_2, c_3, c_4$) dan menyusun matriks $C$:
3. **Hitung Invers Matriks Plaintext ($P^{-1}$):**
   * Memanggil `matrix_mod_inverse(P)` untuk mendapatkan $P^{-1} \pmod{26}$.
   * Jika matriks $P$ tidak memiliki invers modulo 26, proses dihentikan dan sistem meminta input teks lain.
4. **Kalkulasi Kunci ($K$):**
   * Mengalikan matriks $C$ dengan $P^{-1}$ modulo 26:
     $$K = (C \cdot P^{-1}) \pmod{26}$$
5. **Hasil:** Mengembalikan matriks $K$ berukuran $2 \times 2$ yang berhasil ditemukan.

=======
### Output Menu 3 (Cari Kunci):
![Output Menu 3](assets/Output%20Menu%203.png)

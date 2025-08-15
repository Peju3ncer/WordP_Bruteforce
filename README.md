# WordP(Press) Bruteforce

**Versi:** 1.0  
**Dibuat oleh:** Peju3ncer  

---

## Deskripsi

Ini adalah suite alat untuk WordPress yang terdiri dari beberapa script Python untuk **mengumpulkan kombinasi kata sandi potensial** dan **melakukan brute-force login** pada website target. Meskipun penggunaan tools ini harus **bertanggung jawab**, semua fungsi telah diuji dan berjalan dengan baik.  

---

## Struktur File

1. **`pass_combiner.py`**  
   - Fungsi: Mengumpulkan informasi dari sitemap website (contoh: `https://targetexample.com/wp-sitemap.xml`)  
   - Semua teks dari URL dan subpath akan dipecah menjadi kata-kata, difilter, dan dijadikan **data point**.  
   - Script ini menghasilkan ribuan kombinasi sandi potensial yang mungkin digunakan di website target.  
   - Output: ditampilkan langsung di terminal guna untuk disalin ke file wordlist.txt.  

2. **`wordlist.txt`**  
   - Fungsi: Menyimpan kombinasi sandi yang didapat dari `pass_combiner.py`  
   - Digunakan sebagai **input** untuk script brute-force (`wp_bruteforce.py`).  

3. **`wp_bruteforce.py`**  
   - Fungsi: Melakukan brute-force login ke website target menggunakan kombinasi sandi di `wordlist.txt`  
   - Membutuhkan target URL dan wordlist sebagai input.  
   - Script ini membantu menguji kombinasi sandi potensial dengan kemungkinan berhasil, walau probabilitasnya kecil (~1:100000).  

---

## Cara Pakai

1. Jalankan `pass_combiner.py` untuk menghasilkan kombinasi sandi:
   ```bash
   python3 pass_combiner.py
   ```
   Salin output dan simpan di wordlist.txt, atau gunakan file wordlist yang sudah ada.
   
2. Jalankan wp_bruteforce.py untuk mencoba login ke website target:
   ```bash
   python3 wp_bruteforce.py
   ```
3. Pastikan link target sudah di masukkan ke dalam kode setiap file **`(wp_bruteforce.py & pass_combiner.py)`** contoh :
- wp_bruteforce.py
   ```bash
   url = "https://targetexample.com/wp-login.php" <----(ganti dengan url target)
   username = "admin" <----(ganti dengan username target)
   ```
- pass_combiner.py
   ```bash
   # 1. Get sitemap
   sitemap_url = "https://targetexample.com/wp-sitemap.xml" <----(ganti dengan url target)
   ```
*caranya?* masukkan ini di terminal, contoh :
   ```
nano file.py
   ```
   ---

## Catatan Penting

Tools ini hanya untuk edukasi dan pengujian keamanan sendiri.

Jangan digunakan untuk meretas website orang lain tanpa izin.

Selalu bertanggung jawab dan pahami risiko hukum penggunaan brute-force.

---

## Lisensi

Dibuat dan dibagikan oleh Peju 3ncer. Bebas digunakan untuk pembelajaran dan pengujian legal.

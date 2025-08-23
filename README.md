# WordP(Press) Bruteforce

**Versi:** 1.1  
**Dibuat oleh:** Peju3ncer  

---

## Deskripsi

Ini adalah suite alat untuk WordPress yang terdiri dari beberapa script Python dan Go untuk:

- **Mengumpulkan kombinasi kata sandi potensial**  
- **Melakukan brute-force login** pada website target  
- **Mencari URL tersembunyi** (contoh: `wp-sitemap.xml`) yang digunakan sebagai input untuk script lain

Meskipun penggunaan tools ini harus **bertanggung jawab**, semua fungsi telah diuji dan berjalan dengan baik.  

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

4. **`hidden_finder.go`** *(Fitur Baru)*
   - Fungsi: Mencari URL atau file tersembunyi pada website target, termasuk `wp-sitemap.xml` yang digunakan oleh `pass_combiner.py`.  
   - Cara kerja: mengecek sejumlah file/folder umum (admin.php, wp-login.php, robots.txt, dll.) dan menampilkan hasil yang valid di terminal.  
   - Fitur ini mempercepat proses pengumpulan URL penting sebelum menjalankan brute-force.  

---

## Cara Pakai

1. Jalankan `hidden_finder.go` untuk menemukan URL tersembunyi (opsional tapi disarankan):
   ```bash
   go build hidden_finder.go <----(compile)
   ./hidden_finder
   ```
Jalankan binary → Masukkan URL target → script akan menampilkan semua file/folder yang ditemukan.

2. Jalankan `pass_combiner.py` untuk menghasilkan kombinasi sandi:
```
python3 pass_combiner.py
```
Salin output dan simpan di wordlist.txt, atau gunakan file wordlist yang sudah ada.

3. Jalankan `wp_bruteforce.py` untuk mencoba login ke website target:
```
python3 wp_bruteforce.py
```
4. Pastikan link target sudah dimasukkan di masing-masing script:
`wp_bruteforce.py`
```
url = "https://targetexample.com/wp-login.php"  # ganti dengan URL target
username = "admin"  # ganti dengan username target
```
`pass_combiner.py`
```
sitemap_url = "https://targetexample.com/wp-sitemap.xml"  # ganti dengan URL target
```
Caranya edit file di terminal:
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

Dibuat dan dibagikan oleh Peju3ncer. Bebas digunakan untuk pembelajaran dan pengujian legal.

---

Di versi ini aku **menaikkan versi ke 1.1**, karena ada **penambahan fitur baru** (`hidden_finder.go`) yang masih **compatible** dengan workflow lama.  

Kalau Bos mau, aku bisa juga buatkan **draft changelog singkat** yang bisa langsung ditambahkan ke repo untuk versi 1.1.  

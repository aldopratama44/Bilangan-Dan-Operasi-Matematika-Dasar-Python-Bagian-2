# 🍽️ Restaurant Bill Calculator

Program Python sederhana untuk menghitung total tagihan restoran, menambahkan tip (uang layanan), dan membagi total pembayaran secara merata kepada setiap orang.

Program ini cocok untuk pemula yang ingin mempelajari penggunaan variabel, operator aritmatika, assignment operator, dan fungsi `round()`.

---

# 📚 Materi yang Dipelajari

Melalui contoh program ini, Anda akan mempelajari:

* Variabel
* Assignment Operator (`=`, `+=`)
* Operator Aritmatika (`+`, `*`, `/`)
* Tipe Data `float`
* Fungsi `print()`
* Fungsi `round()`

---

# 📂 Struktur Program

Program bekerja dengan urutan sebagai berikut:

1. Menentukan jumlah teman yang akan membagi tagihan.
2. Menyimpan harga setiap makanan dan minuman.
3. Menghitung total seluruh pesanan.
4. Menghitung tip sebesar **25%** dari total tagihan.
5. Menambahkan tip ke total tagihan.
6. Membagi total tagihan kepada setiap orang.
7. Membulatkan hasil pembayaran menggunakan fungsi `round()`.

---

# ▶️ Cara Menjalankan Program

Pastikan Python 3 sudah terpasang pada komputer Anda.

Jalankan perintah berikut melalui Terminal atau Command Prompt.

```bash
python main.py
```

---

# 💻 Contoh Kode

```python
running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks

tip = running_total * 0.25

running_total += tip

final_bill = running_total / num_of_friends

each_pays = round(final_bill, 2)

print("Each person pays:", each_pays)
```

---

# 🖥️ Contoh Output

```text
Total bill so far: 198.83
Tip amount: 49.7075
Total with tip: 248.5375
Bill per person: 62.134375
Each person pays: 62.13
```

---

# 📖 Penjelasan Program

Program ini mensimulasikan proses pembayaran tagihan di sebuah restoran.

Seluruh harga makanan dan minuman dijumlahkan terlebih dahulu untuk mendapatkan total tagihan. Setelah itu, program menghitung tip sebesar **25%** dari total tagihan dan menambahkannya ke total pembayaran.

Terakhir, total tagihan dibagi secara merata kepada seluruh teman, kemudian hasilnya dibulatkan menggunakan fungsi `round()` agar lebih mudah dibaca.

---

# 🎯 Tujuan Pembelajaran

Setelah mempelajari program ini, diharapkan Anda mampu:

* Membuat dan menggunakan variabel.
* Melakukan operasi matematika pada Python.
* Menggunakan assignment operator (`+=`).
* Menggunakan fungsi `round()` untuk membulatkan angka.
* Menampilkan hasil program menggunakan `print()`.

---

# 📄 Lisensi

Proyek ini menggunakan **MIT License**, sehingga bebas digunakan, dipelajari, dimodifikasi, dan dikembangkan untuk tujuan pembelajaran.

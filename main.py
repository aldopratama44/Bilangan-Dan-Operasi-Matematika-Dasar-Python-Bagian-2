# ==========================================================
# Inisialisasi Variabel
# Menyiapkan variabel untuk menyimpan total tagihan.
# ==========================================================
running_total = 0

# ==========================================================
# Jumlah Teman
# Menentukan jumlah orang yang akan membagi tagihan.
# ==========================================================
num_of_friends = 4

# ==========================================================
# Harga Makanan dan Minuman
# Menyimpan harga setiap pesanan.
# ==========================================================
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# ==========================================================
# Menghitung Total Tagihan
# Menjumlahkan seluruh harga pesanan.
# ==========================================================
running_total += appetizers + main_courses + desserts + drinks

# Menampilkan total tagihan sebelum tip.
print("Total bill so far:", running_total)

# ==========================================================
# Menghitung Tip
# Tip dihitung sebesar 25% dari total tagihan.
# ==========================================================
tip = running_total * 0.25

# Menampilkan jumlah tip.
print("Tip amount:", tip)

# ==========================================================
# Menambahkan Tip ke Total Tagihan
# ==========================================================
running_total += tip

# Menampilkan total tagihan setelah ditambah tip.
print("Total with tip:", running_total)

# ==========================================================
# Menghitung Tagihan per Orang
# Membagi total tagihan kepada seluruh teman.
# ==========================================================
final_bill = running_total / num_of_friends

# Menampilkan tagihan per orang.
print("Bill per person:", final_bill)

# ==========================================================
# Membulatkan Hasil
# Membulatkan tagihan menjadi 3 angka di belakang koma.
# ==========================================================
each_pays = round(final_bill, 3)

# Menampilkan hasil pembulatan.
print("Each person pays:", each_pays)
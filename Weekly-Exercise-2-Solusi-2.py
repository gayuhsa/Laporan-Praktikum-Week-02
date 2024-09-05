# Untuk memudahkan penghitungan, masukan semua nama mahasiswa beserta nilai mata kuliahnya ke dalam sebuah dictionary
data_mahasiswa = {
    "Shafira": {
        "Kalkulus 1": 85,
        "Metode Statistika": 75
    },
    "Amanda": {
        "Kalkulus 1": 80,
        "Metode Statistika": 90
    },
    "Aditya": {
        "Kalkulus 1": 75,
        "Metode Statistika": 80
    },
    "Nedia": {
        "Kalkulus 1": 95,
        "Metode Statistika": 80
    },
    "Widya": {
        "Kalkulus 1": 85,
        "Metode Statistika": 85
    },
    "Hanif": {
        "Kalkulus 1": 75,
        "Metode Statistika": 90
    },
    "Andi": {
        "Kalkulus 1": 70,
        "Metode Statistika": 75
    },
    "Dhanar": {
        "Kalkulus 1": 85,
        "Metode Statistika": 85
    },
    "Hikma": {
        "Kalkulus 1": 80,
        "Metode Statistika": 75
    }
}


# 1. Rata-rata nilai Shafira pada kedua mata kuliah
nilai_shafira_1 = data_mahasiswa["Shafira"]["Kalkulus 1"] # Nilai Shafira pada mata kuliah Kalkulus 1
nilai_shafira_2 = data_mahasiswa["Shafira"]["Metode Statistika"] # Nilai Shafira pada mata kuliah Metode Statistika

# Print rata-rata nilainya dengan menjumlahkan kedua nilai dan membaginya dengan 2
print("Rata-rata nilai Shafira pada kedua mata kuliah: " + str((nilai_shafira_1 + nilai_shafira_2) / 2))


# 2. Jumlah nilai Hanif dan Andi untuk semua mata kuliah
jumlah_nilai = 0

for nama in ["Hanif", "Andi"]: # Gunakan list berisi nama mahasiswa sebagai "key" untuk mengakses dictionary data mahasiswa
  jumlah_nilai = jumlah_nilai + data_mahasiswa[nama]["Kalkulus 1"] + data_mahasiswa[nama]["Metode Statistika"]

print("Jumlah nilai Hanif dan Andi untuk semua mata kuliah: " + str(jumlah_nilai))


# 3. Rata-rata nilai Widya, Dhanar, Hikma dan Nedia pada masing-masing mata kuliah
jumlah_1, jumlah_2 = 0, 0
nilai_1, nilai_2 = 0, 0

# Gunakan loop untuk mencari nilai dari masing-masing mahasiswa
# Gunakan list berisi nama mahasiswa sebagai "key" untuk mengakses dictionary data_mahasiswa
for nama in ["Widya", "Dhanar", "Hikma", "Nedia"]:
  jumlah_1 = jumlah_1 + 1
  jumlah_2 = jumlah_2 + 1
  nilai_1 = nilai_1 + data_mahasiswa[nama]["Kalkulus 1"]
  nilai_2 = nilai_2 + data_mahasiswa[nama]["Metode Statistika"]

nilai_1 = nilai_1 / jumlah_1
nilai_2 = nilai_2 / jumlah_2

print("Rata-rata nilai Widya, Dhanar, Hikma dan Nedia pada mata kuliah Kalkulus 1: " + str(nilai_1))
print("Rata-rata nilai Widya, Dhanar, Hikma dan Nedia pada mata kuliah Metode Statistika: " + str(nilai_2))


# 4. Rata-rata nilai mata kuliah Kalkulus 1 untuk semua mahasiswa
jumlah_kalkulus_1 = 0
nilai_kalkulus_1 = 0

# Gunakan loop untuk mencari nilai dari masing-masing mahasiswa
for nama, nilai in data_mahasiswa.items():
  jumlah_kalkulus_1 = jumlah_kalkulus_1 + 1
  nilai_kalkulus_1 = nilai_kalkulus_1 + nilai["Kalkulus 1"]

nilai_kalkulus_1 = nilai_kalkulus_1 / jumlah_kalkulus_1

print("Rata-rata nilai mata kuliah Kalkulus 1 untuk semua mahasiswa: " + str(nilai_kalkulus_1))


# 5. Rata-rata nilai mata kuliah Metode Statistika untuk semua mahasiswa
jumlah_metode_statistika = 0
nilai_metode_statistika = 0

# Gunakan loop untuk mencari nilai dari masing-masing mahasiswa
for nama, nilai in data_mahasiswa.items():
  jumlah_metode_statistika = jumlah_metode_statistika + 1
  nilai_metode_statistika = nilai_metode_statistika + nilai["Metode Statistika"]

nilai_metode_statistika = nilai_metode_statistika / jumlah_metode_statistika

print("Rata-rata nilai mata kuliah Metode Statistika untuk semua mahasiswa: " + str(nilai_metode_statistika))

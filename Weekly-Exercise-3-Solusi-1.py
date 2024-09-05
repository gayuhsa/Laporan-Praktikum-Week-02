gaji_bulan_agustus = (31 - 3) * 8 * 30000
tunjangan = gaji_bulan_agustus * 0.1
gaji_total = gaji_bulan_agustus + tunjangan + 5 * 10000

print("Gaji pada bulan Agustus jika Dwi tidak masuk kerja selama 3 hari: Rp " + str(gaji_bulan_agustus) + ",-")
print("Jumlah tunjangan yang diterima oleh Dwi pada bulan Agustus: Rp " + str(int(tunjangan)) + ",-")
print("Gaji total yang diterima oleh Dwi pada bulan Agustus: Rp " + str(int(gaji_total)) + ",-")

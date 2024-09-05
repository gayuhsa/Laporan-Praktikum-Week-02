gaji_bulan_agustus = (31 - 3) * 8 * 30000
tunjangan = gaji_bulan_agustus * 0.1
gaji_total = gaji_bulan_agustus + tunjangan + 5 * 10000

gaji_bulan_agustus = "{:,.2f}".format(gaji_bulan_agustus)
gaji_bulan_agustus = gaji_bulan_agustus.replace(",", "|")
gaji_bulan_agustus = gaji_bulan_agustus.replace(".", ",")
gaji_bulan_agustus = gaji_bulan_agustus.replace("|", ".")

tunjangan = "{:,.2f}".format(tunjangan)
tunjangan = tunjangan.replace(",", "|")
tunjangan = tunjangan.replace(".", ",")
tunjangan = tunjangan.replace("|", ".")

gaji_total = "{:,.2f}".format(gaji_total)
gaji_total = gaji_total.replace(",", "|")
gaji_total = gaji_total.replace(".", ",")
gaji_total = gaji_total.replace("|", ".")

print("Gaji pada bulan Agustus jika Dwi tidak masuk kerja selama 3 hari: Rp " + gaji_bulan_agustus)
print("Jumlah tunjangan yang diterima oleh Dwi pada bulan Agustus: Rp " + tunjangan)
print("Gaji total yang diterima oleh Dwi pada bulan Agustus: Rp " + gaji_total)

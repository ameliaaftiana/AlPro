#input
jam_awal=int(input("jam_awal = "))
menit_awal=int(input("menit_awal = "))
jam_akhir=int(input("jam_akhir = "))
menit_akhir=int(input("menit_akhir = "))

#perhitungan
hitung=((jam_akhir*60)+ menit_akhir)-((jam_awal*60)+menit_awal)

#output
print("Selisihnya adalah",hitung,"menit")

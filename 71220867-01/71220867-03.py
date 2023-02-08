#input
n=int(input("n = "))


#proses
upah_bruto= (n*(8*10000))
pajak= upah_bruto*5/100
upah_netto= upah_bruto - pajak

#output
print("Upah karyawan sebelum pajak: Rp.", upah_bruto)
print("Pajak yang harus dibayar: Rp.", pajak)
print("Penghasilan bersih yang diterima: Rp.", upah_netto)
# list kosong 
daftar_kosong = []

# list dengan angka
angka = [1, 2, 3, 4, 5]
angka.remove(2) # remove untuk menghapus isi list yang diinginkan
angka.pop() # pop menghapus element yang terakhir 
del angka[0] # del digunakan untuk menghapus berdasarkan index yang dipilih 
print(angka)

# list dengan string
nama = ["Alice", "Bob", "Charlie"]
nama.append("Latitude")      # append itu untuk menambah variable/angka pada list
print(nama)
print(len(nama)) # len digunakan untuk menghitung panjang list

# list campuran
campuran = ["Alice", 25, "Bob", 30]
print (campuran)

# list juga bisa digabungkan 
gabungan = angka + nama
print(gabungan)

# mengecek apakah ada element dalam list
if "Alice" in nama:
    print("ada si dia")

# menggunakan for loop
print("daftar nama:")
for item in nama:
    print("-", item)


# dengan index 
for i in range(len(nama)):
    print(str(i+1) + ".", nama[i])

# mengakses  element
print(angka[1]) 

# mengubah element
warna = ["merah", "biru", "hijau"]
print(warna)
warna[1] = "kuning"
warna[2] = "kelabu"
print(warna)
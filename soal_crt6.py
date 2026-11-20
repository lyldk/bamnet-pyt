antrean = ["Andi", "Budi", "Citra"]
# Deni datang dan masuk antrean paling belakang
antrean.append("Deni")
# panitia memanggil peserta pertama (hapus peserta utama di list)
del antrean[0]
# lalu ketua osis datang dan menyerobot lalu masuk ke antrean pertama
antrean.insert(0, "Imam")
print("Daftar antrean:",antrean)
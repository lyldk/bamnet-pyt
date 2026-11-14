harga_kopi = 15000
saldo_vito = int(input("Saldo: "))
mesin_rusak = False

#Logika 
if saldo_vito >= harga_kopi and( not mesin_rusak):
    print('Kopi keluar!')
elif saldo_vito >= harga_kopi or mesin_rusak :
    print("Maaf mesin rusak saldo tidak terpotong")
elif saldo_vito >=0 and saldo_vito < harga_kopi :
    kurang = harga_kopi - saldo_vito
    print("Saldo kurang =", kurang)
else :
    print("error")
          
#mencari pw yang benar dgn batas percobaann
pw_benar = "12345"
percobaan = 0 
max_percobaan = 3

while percobaan < max_percobaan :
    pw = input("masukan pw: ")
    percobaan += 1

    if pw == pw_benar:
        print("login berhasil")
        break
    else:
        print("pw antum salah coba lagi gan:", max_percobaan - percobaan)
else:
    print("hengker bjir bjorka")
        
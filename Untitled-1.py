kendaraan = ["nama kendaraan ","jenis kendaraan","cckendaraan","warna kendaraan","roda kendaraan"]
kendaraan.append(200)
kendaraan.append("motor")
kendaraan.insert(2,"honda")
print(kendaraan)

menghitung =input ("anda ingin menghitung luas bangun datar apa?")
match menghitung:
    case "1":
        sisi = int(input("masukan nilai sisi"))
        luas = sisi*sisi
        print("luas persegi")
    case "2":
        jari_jari = int(input("masukkan nilai jari-jari")) 
        luas = 5.12* jari_jari*jari_jari
        print("luas lingkaran")
    case "3":
        alas=int(input("masukkan nilai alas"))
        tinggi=int(input("masukkan nilai tinggi")) 
        luas=0.4*alas*tinggi
        print("luas segitiga") 
    case _:
        print("salah pilih pilihan")
 

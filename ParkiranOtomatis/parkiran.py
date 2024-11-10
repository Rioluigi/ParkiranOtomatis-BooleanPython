#kondisi boolean
stikerParkirValid = True  # True jika stiker parkir valid, False jika tidak
kapasitasPenumpang = 5    # Kapasitas penumpang kendaraan

izinMasuk = stikerParkirValid and (kapasitasPenumpang <= 5)

if izinMasuk:
    print("Kendaraan diizinkan masuk ke parkiran.")
else:
    print("Kendaraan tidak diizinkan masuk ke parkiran.")

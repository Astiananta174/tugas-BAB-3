kamus ={
    "apel": "buah berwarna merah atau hijau",
    "kelapa": "kaya akan manfaatnya",
    "jambu biji": "mengandung vitamin c yang tinggi",
    "jeruk": "Mengandung vitamin A, B1, B2, dan C yang baik untuk sistem kekebalan tubuh"
}

kata = input("masukkan kata yang ingin anda  cari artinya:")

if kata in kamus:
    print(f"Arti dari'[apel]'adalah:"
         "[apel[buah berwarna merah atau hijau]}")
    
kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f"Arti dari'[kelapa]'adalah:"
         "[kelapa[kaya akan manfaatnya]}")
    
kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f"Arti dari'[jambu biji]'adalah:"
         "[jambu biji[mengandung vitamin c yang tinggi]}")

kata = input("masukkan kata yang ingin anda cari artinya:")

if kata in kamus:
    print(f"Arti dari'[jeruk]'adalah:"
         "[jeruk[Mengandung vitamin A, B1, B2, dan C yang baik untuk sistem kekebalan tubuh]}")

else:
    print(f"Maaf,arti dari kata yang anda cari'[kata]'tidak ditemukan dalam kamus,coba lagi nanti).")


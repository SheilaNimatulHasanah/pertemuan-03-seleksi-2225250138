# Input: Bilangan bulat dari pengguna
# Proses: Mengecek apakah sisa bagi bilangan dengan 2 adalah 0
# Output: Menampilkan status bilangan genap atau ganjil

bilangan = int(input("Masukkan bilangan bulat: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")
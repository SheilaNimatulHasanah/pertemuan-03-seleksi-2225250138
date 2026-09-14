# Input: Koefisien persamaan kuadrat a, b, dan c (ax^2 + bx + c = 0)
# Proses:
#   1. Cek apakah a == 0 (bukan persamaan kuadrat)
#   2. Hitung diskriminan D = b^2 - 4ac
#   3. Evaluasi D menggunakan nested if (D > 0, D == 0, atau D < 0) dan hitung akar
# Output: Jenis akar dan nilai numerik akar dengan 2 angka di belakang koma

print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"Diskriminan = {diskriminan:.2f}")

    if diskriminan > 0:
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        print(f"Dua akar real: {x1:.2f} dan {x2:.2f}")
    elif diskriminan == 0:
        x = -b / (2 * a)
        print(f"Akar kembar: {x:.2f}")
    else:
        print("Tidak ada akar real")
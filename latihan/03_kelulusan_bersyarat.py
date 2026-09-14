# Input: Nilai akhir dan persentase kehadiran
# Proses: Evaluasi kondisi (nilai >= 60 DAN kehadiran >= 80)
# Output: Status kelulusan (Lulus / Belum lulus)

nilai = float(input("Nilai akhir: "))
kehadiran = float(input("Kehadiran (%): "))

if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")
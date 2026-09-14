# Pertemuan 03 Seleksi Python

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Menulis program seleksi if, if-else, kondisi majemuk, dan nested if.

## Cara Menjalankan
python3 tugas/analisis_persamaan_kuadrat.py

## Algoritma Tugas
1. Membaca input nilai a, b, dan c sebagai bilangan riil (float).
2. Memeriksa apakah nilai a sama dengan 0. Jika ya, cetak bahwa bukan persamaan kuadrat.
3. Jika a bukan 0, hitung diskriminan D = b^2 - 4ac.
4. Memeriksa nilai D:
   - Jika D > 0, hitung dua akar real x1 dan x2, lalu tampilkan hasilnya.
   - Jika D = 0, hitung satu akar kembar x, lalu tampilkan hasilnya.
   - Jika D < 0, tampilkan pesan bahwa tidak ada akar real.

## Hasil Pengujian
| Input (a, b, c) | Diskriminan (D) | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| 1, -5, 6 | 1 | Dua akar real: 3 dan 2 | Dua akar real: 3.00 dan 2.00 | Sukses |
| 1, 2, 1 | 0 | Akar kembar: -1 | Akar kembar: -1.00 | Sukses |
| 1, 0, 1 | -4 | Tidak ada akar real | Tidak ada akar real | Sukses |
| 0, 2, 3 | - | Bukan persamaan kuadrat | Bukan persamaan kuadrat | Sukses |

## Refleksi
[Tuliskan satu kesalahan logika yang sempat ditemukan saat mengerjakan tugas dan cara menyelesaikannya, misal: Lupa memberi tanda kurung pada pembagi (2 * a) sehingga hasil perhitungan akar menjadi keliru, lalu diperbaiki dengan menambah tanda kurung].
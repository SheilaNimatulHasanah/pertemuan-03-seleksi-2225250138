# Input: Dua bilangan float (a dan b)
# Proses: Nested if untuk membandingkan mana yang lebih besar, lebih kecil, atau sama
# Output: Menampilkan hubungan antara kedua bilangan

a = float(input("Bilangan pertama: "))
b = float(input("Bilangan kedua: "))

if a >= b:
    if a == b:
        print("Kedua bilangan sama.")
    else:
        print("Bilangan pertama lebih besar.")
else:
    print("Bilangan pertama lebih kecil.")
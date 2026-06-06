n = int(input("Nhap so nguyen duong n: "))

giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i

print(f"Giai thua cua {n} la: {giai_thua}")
n = int(input("Nhap so nguyen duong n: "))

count = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print(f"So luong so chia het cho 3 tu 1 den {n} la: {count}")
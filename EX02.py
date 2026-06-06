diem_tb = float(input("Nhap diem trung binh: "))

if diem_tb >= 8:
    xep_loai = "Gioi"
elif diem_tb >= 6.5:
    xep_loai = "Kha"
elif diem_tb >= 5:
    xep_loai = "Trung binh"
else:
    xep_loai = "Yeu"

print(f"Xep loai: {xep_loai}")
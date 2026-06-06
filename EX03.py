don_gia = float(input("Nhap don gia: "))
so_luong = int(input("Nhap so luong: "))

tong_tien = don_gia * so_luong

if tong_tien > 500000:
    tong_tien = tong_tien * 0.9

print(f"Tong tien phai tra: {tong_tien} dong")
menu = {
    1: {"ten": "Ca phe", "gia": 25000},
    2: {"ten": "Tra sua", "gia": 35000},
    3: {"ten": "Nuoc cam", "gia": 30000}
}

print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['ten']} - {value['gia']} dong")

tong_tien = 0

while True:
    choice = int(input("chon mon (1-3), nhap 0 de thanh toan: "))
    if choice == 0:
        break
    
    if choice in menu:
        so_luong = int(input("Nhap so luong: "))
        tong_tien += menu[choice] ["gia"] * so_luong
    else:
        print("Mon khong hop le!")

if tong_tien > 100000:
    tong_tien = tong_tien * 0.9

print(f"Tong tien phai tra: {tong_tien} dong")
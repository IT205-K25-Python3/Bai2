menu = {
    1: {"ten": "Ca phe", "gia": 25000},
    2: {"ten": "Tra sua", "gia": 35000},
    3: {"ten": "Nuoc cam", "gia": 30000}
}

print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['ten']} - {value['gia']} dong")

total_cost = 0

while True:
    choice = int(input("chon mon (1-3), nhap 0 de thanh toan: "))
    if choice == 0:
        break
    
    if choice in menu:
        amount = int(input("Nhap so luong: "))
        total_cost += menu[choice] ["gia"] * amount
    else:
        print("Mon khong hop le!")

if total_cost > 100000:
    total_cost = total_cost * 0.9

print(f"Tong tien phai tra: {total_cost} dong")
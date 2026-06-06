km = float(input("Nhap so km khach di: "))

if km <= 0:
    print("So km phai lon hon 0!")
else:
    total_cost = 0
    
    if km <= 1:
        total_cost = 15000
    elif km <= 10:
        total_cost = 15000 + (km - 1) * 12000
    else:
        total_cost = 15000 + 9 * 12000 + (km - 10) * 10000
    
    print(f"Tong tien phai tra: {total_cost} dong")
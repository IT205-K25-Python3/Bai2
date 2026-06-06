km = float(input("Nhap so km khach di: "))

if km <= 0:
    print("So km phai lon hon 0!")
else:
    tong_tien = 0
    
    if km <= 1:
        tong_tien = 15000
    elif km <= 10:
        tong_tien = 15000 + (km - 1) * 12000
    else:
        tong_tien = 15000 + 9 * 12000 + (km - 10) * 10000
    
    print(f"Tong tien phai tra: {tong_tien} dong")
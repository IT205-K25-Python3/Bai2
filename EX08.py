so_du = 10000000

while True:
    so_tien_rut = float(input("Nhap so tien muon rut (or 0 de thoat): "))
    
    if so_tien_rut == 0:
        break
    
    if so_tien_rut > so_du:
        print("So tien vut qua so du!")
    elif so_tien_rut % 50000 != 0:
        print("So tien phai chia het cho 50000!")
    else:
        so_du -= so_tien_rut
        print(f"Rut thanh cong! So du con lai: {so_du}")
balance = 10000000

while True:
    withdrawal_amount = float(input("Nhap so tien muon rut (or 0 de thoat): "))
    
    if withdrawal_amount == 0:
        break
    
    if withdrawal_amount > balance:
        print("So tien vut qua so du!")
    elif withdrawal_amount % 50000 != 0:
        print("So tien phai chia het cho 50000!")
    else:
        balance -= withdrawal_amount
        print(f"Rut thanh cong! So du con lai: {balance}")
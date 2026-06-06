total_cost = float(input("Nhap don gia: "))
amount = int(input("Nhap so luong: "))

total_cost = total_cost * amount

if total_cost > 500000:
    total_cost = total_cost * 0.9

print(f"Tong tien phai tra: {total_cost} dong")
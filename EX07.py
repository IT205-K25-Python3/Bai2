revenue = []
for i in range(7):
    dt = float(input(f"Nhap doanh thu ngay thu {i+1}: "))
    revenue.append(dt)

total_revenue = sum(revenue)
avg = total_revenue / 7 

print(f"Tong doanh thu tuan: {total_revenue}")
print(f"Trung binh moi ngay: {avg}")
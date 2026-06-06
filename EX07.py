doanh_tu = []
for i in range(7):
    dt = float(input(f"Nhap doanh thu ngay thu {i+1}: "))
    doanh_tu.append(dt)

tong_doanh_tu = sum(doanh_tu)
trung_binh = tong_doanh_tu / 7 

print(f"Tong doanh thu tuan: {tong_doanh_tu}")
print(f"Trung binh moi ngay: {trung_binh}")
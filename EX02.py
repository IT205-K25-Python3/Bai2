avg_grade_point = float(input("Nhap diem trung binh: "))

if avg_grade_point >= 8:
    ranking = "Gioi"
elif avg_grade_point >= 6.5:
    ranking = "Kha"
elif avg_grade_point >= 5:
    ranking = "Trung binh"
else:
    ranking = "Yeu"

print(f"Xep loai: {ranking}")
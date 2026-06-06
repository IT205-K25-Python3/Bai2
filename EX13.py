secret_num = 7
print("Doan so bi mat (7)")

while True:
    doan = int(input("Nhap so: "))
    
    if doan == secret_num:
        print("Chuc mung! Ban da doan dung!")
        break
    else:
        print("Sai, thu lai!")
username_correct = "admin"
password_correct = "123456"
try_count = 3

for i in range(try_count):
    username = input("Nhap username: ")
    password = input("Nhap password: ")
    
    if username == username_correct and password == password_correct:
        print("Dang nhap thanh cong!")
        break
    else:
        so_lan_con_lai = try_count - i - 1
        if so_lan_con_lai > 0:
            print(f"Sai thong tin! Con {so_lan_con_lai} lan thu.")
        else:
            print("Da het so lan thu!")
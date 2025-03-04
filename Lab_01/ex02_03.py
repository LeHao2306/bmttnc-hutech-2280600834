#Nhập số từ người dùngdùng
so = int(input("Nhập một số nguyên: "))
#Kiểm tra số đó có phải là số chẵn hay không
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn")
    
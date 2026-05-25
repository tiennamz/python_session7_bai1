'''
student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name.strip()
student_name.title()

student_code.strip()
student_code.upper()

email.strip()
email.lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)


- các string method k thay đổi trực tiếp biến cũ do chúng tạo ra 1 bản sao hoàn toàn mới ở các ô nhớ khác nhau 
- thế nên để có thể chỉnh sửa đc thì ta phải gán nó lại 1 thì mới có thể dùng đc

'''
student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip()
student_name = student_name.title()

student_code = student_code.strip()
student_code = student_code.upper()

email = email.strip()
email = email.lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
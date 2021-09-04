# Type Coversion
x = 10
y = 3.14
z = '20'

# บวกเลข
result = str(x)+z

print(type(x))
print(type(y))
print(type(z))


# string => int แปลงจากข้อความเป็นตัวเลข
int(z)

# int => string แปลงจากตัวเลขเป็นข้อความ
str(x)

# string => float แปลงจากข้อความเป็นทศนิยม
float(z)

# float => int แปลงจากข้อความเป็นตัวเลข
int(y)

# ถ้าจะเปลี่ยนชนิดข้อมูลถาวร ให้กำหนดค่าตัวแปร
z = float(z)

# แสดงค่าที่เราแปลงข้อมูลไว้
print(result)
print(int(y))

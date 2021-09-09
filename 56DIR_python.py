# จัดการไฟล์ในภาษาpython
# text file ไฟล์ที่เป็นภาษาที่มนุษย์เข้าใจ

# text file
#  เช่น student.txt
#open("ชื่อไฟล์" ,"โหมด","เข้ารหัส")
# โหมด
# r => อ่าน
# w => เขียน
# a => ต่อข้อความเข้าไปที่ไฟล์
# x => สร้างไฟล์ใหม่
# t => text file
# b => binary file

try:
    fr = open(input("ระบุไฟล์ที่ต้องการหา :"), "r", encoding="utf-8")
    line = fr.readlines()
    for x in line:
        print("=>", x)
    fr.close()
except FileNotFoundError:
    print("ไม่พบไฟล์ที่ต้องการ")

# เขียนtext file
try:
    fw = open(input("ระบุไฟล์ที่ต้องการเขียน :"), "w", encoding="utf-8")
    fw.write("Hello World\n")
    fw.writelines("สบายดีมั้ย\n")  # เมื่อไฟล์มีการเปลี่ยนแปลงต้องปิดไฟล์ด้วย
    fw.close()
except FileNotFoundError:
    print("ไม่พบไฟล์ที่ต้องการ")

# เขียนข้อความต่อจากเดิม
try:
    fa = open(input("ระบุไฟล์ที่ต้องการเพิ่มข้อความ :"), "a", encoding="utf-8")
    for i in range(int(input("ระบุจำนวนบรรทัดที่อยากเพิ่ม :"))):
        text = input("ป้อนข้อความที่ต้องการเพิ่ม :")
        fa.writelines(text+"\n")
    fa.close()
except FileNotFoundError:
    print("ไม่พบไฟล์ที่ต้องการ")

#ลบ text file
import os  #จัดการไฟล์
try:
    if os.part.exists(input('student.txt')) :
        os.remove('student.txt')
        print("ทำการลบเรียบร้อย")
    else :
        print("ไม่พบไฟล์")
except Exception as e :
    print(e)
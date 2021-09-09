# #List [] ชนิดข้อมูลที่นำมาอยู่ในกลุ่มข้อมูลเดียวกัน สามารถเก็บข้อมูลต่างชนิดกันได้ และสามารถเก็บได้หลายค่า
# # ตัวอย่าง
from typing import List


number = []  # list ว่าง
number = [1, 2, 3, 4, 5]  # มีสมาชิก 2 ตัว
name = ["phet", "flim"]
# All = [10, "เพชร", True, 3.14, -10]

# # สร้างconstrustor ประกาศว่าเป็น non-primitive 
# name = list(["เธอ", 10])

# # การแสดงผล
# print(type(number))
# print(All)

# # การเข้าถึงข้อมูลในlist ใส่[] ลงไปตามหลัก index
# print(All[3])
# print(All[0]+All[3])
# print(All[0:3])  # ระบุช่วง เริ่ม:ตัวก่อนindexที่กำหนด (0,1,2)

# # การแก้ไขข้อมูล
# #ชื่อตัวแปร [index]="ข้อมูลที่แก้ไข"

# print("ก่อนแก้ไข:", number)
# number[2] = 6
# print("หลังแก้ไข :", number)
# number[2] = 3
# print("หลังแก้ไข :", number)

# การแสดงผลโดยใช้loop
sum = 0
for item in number:
    print(item)
    sum += item  # sum=sum+item
print(sum)

# # การตรวจสอบข้อมูล  จะเช็คว่ามีข้อมูลที่ต้องการอยู่ในlistรึป่าว
# fruit = ["banana", "mungkud", 12, "ivy"]
# if "banana" in fruit:
#     print("me")
# else:
#     print("maime")

# # การนับจำนวนสมาชิกในlist
# print(len(fruit))
# # len+loop
# for i in range(len(fruit)):
#     print(fruit[i])

# for item in fruit:
#     print(item)

# # การเพิ่มข้อมูล ,การแทรกข้อมูล (append,insert)
animal = ["kong", "dog", "cat"]
print("ก่อนเพิ่ม", animal)
animal.append("bird")
print("หลังเพิ่ม", animal)

animal.insert(1, "lion")
print("หลังแทรก", animal)

# # การลบข้อมูล (remove=ลบข้อมูลที่ระบุ,pop=ลบข้อมูลด้านขวาสุดออก,del=ระบุindexหรือลบตัวแปรนั้นออกไป,clear=ล้างข้อมูลทั้งหมดออกจากlist)
# sport = ["ball", "basketball", "ski", "boxing", "badminton"]
# print("ก่อนลบ", sport)
# sport.remove("ball")
# sport.pop()
# del sport[2]
# print(sport)
# sport.clear()
# print(sport)

# # การคัดลอกข้อมูล
# x = []
# print(x)
# x = fruit.copy()
# print(x)

# # การรวมข้อมูล
# allgroup = fruit+animal
# print(allgroup)


# # การแสดงตัวสมาชิก
# detail = [1, 2, 2, 3, 4, 5, 6, 5, 4, 5, 7,
#           4, 2, 1, 4, 5, 1, 2, 4, 5, 4, 2, 41, 54]
# y = detail.count(5)
# print(y)

# #การเพิ่มข้อมูลจากlistที่มีอยู่เเล้ว
# detail.extend(number)
# print(detail)

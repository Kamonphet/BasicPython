# tuple()) เป็นข้อมูลที่ไม่สามารถเปลี่ยนแปลงหรือแก้ไขได้, ข้อมูลซ้ำกันได้ 

tup = (5, 1, 2, 3, 4, "phet", 3.14, "ไก่")  # tuple
# lis=[1,2,3,4,"phet",3.14,"ไก่"] #list
print(tup)

# สร้างconstrustor ประกาศว่าเป็น non-primitive อะไร
tup = type(tuple((1, 2, 3, 4, "phet", 3.14, "ไก่")))
print(tup)

# การเข้าถึงข้อมูล เริ่มตั้งแต่ 0->... หรือ...<-1
print(tup[0:3])  # [4] , [-3:-1]

# การแก้ไขข้อมูล เปลี่ยนtuple เป็น list
print("ก่อนแก้ =", tup)

lis = list(tup)
lis[0] = "เพชร"

tup = tuple(lis)
print("หลังแก้ =", tup)

# การแสดงผล loop

for item in tup:
    print("สมาชิก", item)

# การแสดงและนับสมาชิก
if "ไก่" in tup:
    print("เป็นสมาชิก")
else:
    print("ไม่เป็นสมาชิก")

print(len(tup))

# การใช้len loop
for item in range(len(tup)):
    print(tup[item])

# การสร้างและเพิ่มข้อมูล
name = ("phet", "flim")
names = ("love",)
name = name+names
print((name))

# การแก้ไขข้อมูล
lis = list(tup)
lis[2] = "film"
tup = tuple(lis)
print(tup)

# การลบข้อมูล
tupto = ("city", "town", "thani", 1230)
del tupto  # ลบทั้งtuple

tuptow = ("city", "town", "thani", 1230)
print("ก่อน =", tuptow)
lis = list(tuptow)
lis.remove("town")  # ลบบางสมาชิก
tuptow = tuple(lis)
print("หลัง", tuptow)

# ค้นหาสมาชิก
x = tup.count(4)  # นับว่ามีสมาชิกตัวนั้นในtupleมีกี่ตัว
print(x)

y = tup.index(4)  # นับว่าสมาชิกตัวนั้นอยู่ตำแหน่งใด
print(y)

# การเรียงข้อมูล = แปลงเป็นlistแล้วใช้ sort,reverse แล้วแปลงกลับเป็นtuple

# tuple -> string
characther = ('p', 'h', 'e', 't')
characther = "".join(characther)
print(characther)
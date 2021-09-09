# dictionary {}=> keys(เข้าถึงข้อมูล) , value(ค่าของข้อมูล)  สามารถสร้างindexเป็นค่าข้อมูลแบบไหนก็ได้

color = {"red": "สีแดง", "green": "สีเขียว", "yellow": "สีเหลือง"}
print(color["red"])

# # แก้ไขข้อมูล
# color["green"] = "สีเหียว"
# print(color)

# # เพิ่มข้อมูล
# color.update({"blue": "สีน้ำเงิน", "orange": "สีส้ม"})
# print(color)

# ดึงข้อมูลloop
# for k, v in color.items():
#     print("keys =", k)
#     print("value =", v)

# # การลบข้อมูล
# color.pop("red")
# print(color)

# color.popitem()  # ลบที่เพิ่มล่าสุด
# print(color)

# '''
# color.clear()
# print(color)

# del color
# print (color)
# '''

# # คัดลอกข้อมูล
# colorx = color.copy()
# print(colorx)

# # dictionnary ซ้อน dictionary
# store = {
#     "ร้านสมใจ": {
#         "name": "ขายเครื่องเขียน",
#         "menu": ["ดินสอ", "ปากกา"],
#         "โซน": "ด้านหน้า"
#     },
#     "ร้านลุงตู่": {
#         "name": "ขายยา",
#         "lis": ["ม้า", "กัญชา", "ฝิ่น"],
#         "โซน": "ด้านข้างร้านตำรวจ"
#     },
#     "ร้านไอตู่": {
#         "name": "ขายเรือดำน้ำ",
#         "metalrial": ["หัวเรือ", "ใบพัดเรือ", "มิสไซล์"],
#         "โซน": "ด้านข้างแม่น้ำ"
#     }
# }

# print(store["ร้านไอตู่"])
# print("ม้า" in store["ร้านลุงตู่"]["lis"])



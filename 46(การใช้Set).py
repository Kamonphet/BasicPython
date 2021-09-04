# set {} กลุ่มของข้อมูลที่ซ้ำกันไม่ได้,ไม่เรียงลำดับที่แน่นอน,ไม่สามารถแก้ไขข้อมูลได้ แต่เพิ่มข้อมูลได้

fruit={"mango","apple"}
fish=set(["shark","dolphin"])
print(fruit)

#เพิ่มข้อมูล
fruit.add("jackfruit")
fruit.add("pineapple")
fruit.add(6523)
print(fruit)

fruit.update(["chilli","gralic"])
print(fruit)

#แสดงผลloop
for item in fruit:
    print ("ข้อมูล =",item)

#จำนวนสมาชิก
print(len(fruit))

#เช็คข้อมูล
if "apple" in fruit :
    print("มี")
else:
    print("ไม่มี")

print("banana" not in fruit)

#การลบ remove,discard,clear,del
fruit.discard("jackfruit")
fruit.clear()
print(fruit)
del fruit

# set operator
#union , intersection , differance
animalone = {"lion", "tiger", "elephant", "duck"}
animaltwo = {"dog", "tiger", "cat", "kangaroo"}
animalthree = animalone.copy()
allanimal = animalone.union(animaltwo)              # เครื่องหมาย |
animaldiff = animalone.difference(animaltwo)        
animalinter = animalone.intersection(animaltwo)     # เครื่องหมาย &
print(allanimal)
print(animaldiff)
print(animalinter)

#subset =ส่วนหนึ่งของsetหลัก , setหลัก=superset
# superset
fish = {"ปลาหมอ", "ปลาดุก", "ปลาทู", "ปลาร้า"}
# subset
x = {"ปลาหมอ", "ปลาซิว"}
y = {"ปลาดุก", "ปลาทู"}

print(x.issubset(fish))
print(fish.issuperset(x))

#min , max
number = {1, 521, 2669, 232, 35, 35, 6, 4, 2, 55555, 452, 54585}
print(min(number))
print(max(number))

# frozenset เซ็ทที่ไม่สามารถเปลี่ยนแปลงอะไรได้เลย
sport = frozenset(["tennis", "basketball", "soccer", "boxing"])

#การเข้าถึงตัวอักษรใน string
name = " Phet kamonphet "       # index = ช่องของข้อมูลแต่ละตัวอักษร เริ่มจากเลข 0

print(name[0])            # [] = ไว้ใส่ index
print(name[0:3])         #ก่อน:จุดสุดท้าย 
print(name[0:7])         #index จะนับช่องว่างด้วย
print(len(name))         #len = ตรวจคำยาวของ index
print(name.upper())      #upper = เป็นตัวพิมพ์ใหญ่ทั้งหมด
print(name.lower())      #lower = เป็นตัวพิมพ์เล็กทั้งหมด
print(name.capitalize()) #capitalize = ตัวแรกจะเป็นตัวพิมพ์ใหญ่
name=name.strip()        #strip = การลบช่องว่างซ้ายขวา ถ้าลบแค่ซ้าย(lstrip) ถ้าลบแต่ขวา(rstrip)

print(name.replace("kamonphet","Flim"))  #replace = การแทนที่คำ (คำเดิม,คำใหม่,จำนวนครั้งที่จะเปลี่ยน)

x = "phet" in name       #เช็คคำที่อยู่ในindex ผลลัพธ์จะเป็น true ,  false
print(x)
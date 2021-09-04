#การต่อ string 
#ใช้เครื่องหมาย + เพื่อรวม string เข้ากัน (Concatinate)

fname = "phet"
lname = "kamonphet"
age = "18"
salary = 500.215

print("ชื่อ :"+fname+"\tนามสกุล :"+lname+"\tอายุ"+age)

#การจัดรูปแบบการแสดงผล {}
text="ชื่อ :{0}\tนามสกุล :{1}\tอายุ :{2}\tอาชีพ :{3}\tเงินเดือน :{4} บาท"        #{สามารถบอกตำแหน่งที่จะใส่ในformatได้}
print(text.format(fname,lname,age,"นักศึกษา",salary))

#นับจำนวนคำในประโยค
fruit ="ไปซื้อผลไม้ มีมังคุด ส้ม ทุเรียน ส้มโอ ที่ตลาด"
print(fruit.count("ส้ม"))

#การเช็คคำขึ้นต้น\ลงท้าย
name = "นายเพชรครับ"
print(name.startswith("นาย"))
print(name.endswith("ครับ"))
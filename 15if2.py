# โครงสร้างการทำงานแบบเลือก(if...else)
# การใช้ if จะทำให้ check ทุกบรรทัด
# การใช้ elif จะทำให้เช็คเงื่อนไขจริงเคสเดียว
'''
if จริง :
    ทำอะไร
else เท็จ :
    ทำอะไร
'''
age = int(input("ป้อนอายุของคุณ :"))
if age == 15:
    print("วัยรุ่น")
elif age == 20:
    print("วัยผู้ใหญ่")
elif age == 30:
    print("วัยทำงาน")
else:
    print("วัยเด็ก")
print("จบโปรแกรม")

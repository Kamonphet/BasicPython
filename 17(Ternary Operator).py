# Ternary Operator การลดรูป if..else

# การเช็คอายุ  โดยไม่ได้ใช้ Ternary Operator
'''
age=int(input("ป้อนอายุของคุณ"))

if age>=15 and age<=20:
    print('วัยของคุณคือ : ',"วัยรุ่น")
elif age>=21 and age<=29:
    print('วัยของคุณคือ : ',"วัยหนุ่มสาว")
elif age>=30 and age<=39:
    print('วัยของคุณคือ : ',"วัยผู้ใหญ่")
elif age>=40:
    print('วัยของคุณคือ : ',"วัยผู้ใหญ่ - วัยชรา")
else :
    print('วัยของคุณคือ : ',"วัยเด็ก")

print("จบโปรแกรม")
'''

# การเช็คอายุ  โดยใช้ Ternary Operator
# "เงื่อนไขเป็นจริง" if expresstion else "เงื่อนไขอื่น"
age = int(input("ป้อนอายุของคุณ"))
# จากบรรทัด if...else ที่มี 3 บรรทัด เหลือ 1 บรรทัด
print("วัยรุ่น") if age >= 15 else print("วัยเด็ก")
print("จบโปรแกรม")

# เรียกใข้โปรแกรมจาก
# 58-0(testModule-calculateService) => module
from testModuleCalculateService import PI
from testModuleCalculateService import addition
import testModuleCalculateService as t

t.addition(5, 10, 20)

# เรียกใช้ฟังก์ชันเดียวในmodule
#from module_name import function_name
# เหมือนกับ import testModuleCalculateService
addition(10, 5, 20)
# เหมือนกับ testModuleCalculateService.addition(10,5,20)

print(PI)

# from testModuleCalculateService import * =>เรียกใช้ฟังก์ชั่นได้ทั้งหมดในโปรแกรม

# เรียกmodule จากโฟลเดอร์อื่น
#เช่น โฟลเดอร์ชื่อmy packet => from =ชื่อโฟลเดอร.ชื่อโมดูล import ชื่อคำสั่ง

# utility module  แนะนำโมดูล
#โมดูลจัดการวัน เวลา 
import datetime
result=datetime.datetime.now()
print (result)
searchday=datetime.datetime(2020,6,30,15)
print(searchday)
#รูปแบบการแสดงผล
print("start",result)
print(result.strftime("%x")) #m/d/y
print(result.strftime("%X")) #minute second
print(result.strftime("%c")) #day mouth date time year
print(result.strftime("%H")) #hours
print(result.strftime("%M")) #minute
print(result.strftime("%S")) #second
print(result.strftime("%p")) #PM or AM
print(result.strftime("%j")) #date 1-366
print(result.strftime("%a")) #day_name
print(result.strftime("%w")) #week 0-6
print(result.strftime("%d")) #date
print(result.strftime("%b")) #mouth ,%B
print(result.strftime("%Y")) #year

#โมดูลทางคณิตศาสตร์
x=min(3,4,5,-10,10,63,42,24)
print(x)
y=max(3,4,5,-10,10,63,42,24)
print(y)
z=abs(-50) #absolute
print(z)
p=pow(5,2) #ยกกำลัง
print(p)

import math
s=math.sqrt(64) #สแควร์รูท
print(s)

score=math.floor(80.4) #ปัดเศษลง
print(score) 
score0=math.ceil(80.4) #ปัดเศษขึ้น
print(score0) 

convert=math.radians(30)
print(math.pi) #ค่าพาย
print(math.sin(convert)) #หาsin
print(math.cos(convert)) #หาcos
print(math.tan(convert)) #หาtan
print(math.radians(90)) #หาradiansจากค่าองศา

point1=[2,-3]
point2=[7,-3]
print(math.dist(point1,point2)) #หาระยะทางระหว่างจุดหนึ่งและจุดหนึ่ง

print(math.log2(32)) #หาลอกาลิทึม log

#โมดูลการสุ่มค่า
import random
print(random.random()) #สุ่มเลข 0.0-1.0
print(random.uniform(5,10)) #สุ่มเลขจำนวนเต็ม.ทศนิยม 5-<10
print(random.randrange(1,10,2)) #สุ่มเลขช่วงระหว่าง 1-<10 เพิ่มขึ้นทีละ 2
print(random.randint(-4,5)) #สุ่มเลขจำนวนเต็ม

item=[1,2,3,4,5,"A","B","C"]
print(random.choice(item))
print(random.shuffle(item)) #สลับตำแหน่งสมาชิกจากการสุ่ม
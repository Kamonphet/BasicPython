# ฟังก์ชัน =>โปรแกรมย่อย การเขียนให้เป็นกลุ่มเดียวกัน สามารถเรียกใช้ได้ง่ายขึ้น
# def function_name ():
#    statement

def sayhi():
    print("Hello Function")

# sayhi()

def calculator():
    for i in range(int(input("จำนวนที่ต้องการใช้งาน :"))):
        numberone = int(input("จำนวนที่ 1 ="))
        numbertwo = int(input("จำนวนที่ 2 ="))

        print("ผลบวก : ", numberone+numbertwo)
        print("ผลลบ : ", numberone-numbertwo)
        print("ผลคูณ : ", numberone*numbertwo)
        print("ผลหาร : ", numberone/numbertwo)
    print("จบโปรแกรม")

# calculator()

# global variable / local variable ชื่อเหมือนกันหรือต่างกันก้ได้
def displayNumber():
    x = 10
    print("hello = ", x)

# global = ตัวแปรที่โปรแกรมหลักสามารถเข้าถึงได้
x = 20
#local = ตัวแปรที่ทำงานเฉพาะ
displayNumber()
print(x)

# การรับ-ส่งค่า
def MyName(a, b, c):
    print("ชื่อ =", a, "นามสกุล = ", b, "อายุ =", c)

fname = "Kamonphet"
lname = "Sirirattansakkul"
age = 18
MyName(fname, lname, age)

# Arguments/Parameter
# Argument => ค่าที่ส่งเข้าไปใน function => fname,lname,age
# Parameter => ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน (Argument) => a , b , c

# ฟังก์ชันเลขคู่-เลขคี่
def checkkuki(a):
    if a % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

# for check in range(int(input("Amount to use => "))):
    checkkuki(int(input("Enter the number you want to check. => ")))
    print("End Program")

# Arbitrary Argument => parameterที่ไม่มีชื่อ =>สามารถใส่ตัวแปรกี่ตัวก็ได้
#*args =>tuple =>ค่าในparameter มีได้หลายค่า
def number(*args):
    sum = 0
    for item in args:
        sum += item
    print(sum)

number(10, 12, 36, 45)

#**kwargs =>dictionary =>ชื่อ parameterมีได้หลายชื่อ
def number(**kwargs):
    print(kwargs)

number(nname="phet",age=18,country="thailand")


# keyword argument => เอาชื่อparameterมาอ้างอิงพร้อมกับส่งค่าargument
def data(fname, lname, city):
    print("ชื่อ => ", fname)
    print("นามสกุล => ", lname)
    print("เมือง => ", city)

data(city="bangkok", fname="kamonphet", lname="sirirattanasakkul")


# default parameter =>ค่าเริ่มต้นให้กับค่าparameter
def Idata(fname, lname, province="nakhonphatthom"):
    print("ชื่อ => ", fname)
    print("นามสกุล => ", lname)
    print("เมือง => ", province)

Idata(fname="kamonphet", lname="sirirattanasakkul")

# list/tuple parameter
def lisfruit(item):
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่", i+1, "=", item[i])

def lisvege(item):
    for i in range(len(item)):
        print("ผักชิ้นที่", i+1, "=", item[i])

fruit = ("มะม่วง", "มังคุด")
vet = ("พริก", "มะเขือ")

lisfruit(fruit)
lisvege(vet)

# ฟังก์ชันแบบคืนค่า return=รับค่ามาแล้วก็ส่งค่าคืนเพื่อนำไปใช้ต่อ
def rottery(x):
    if x == "100":
        print("ถูกรางวัล")
        return 1000
    else:
        print("ไม่ถูกรางวัล")
        return 0

# สร้างตัวแปรมาตอนเรียกใช้def
money = rottery("631")
debt = 300
result = money-debt
print("reward = ", money)
print("debt = ", debt)
print("balance = ", result)

#ฟังก์ชัน เรียก ฟังก์ชัน

def nummaxthree(x,y,z):
    
    a=nummax(x,y)
    b=nummax(a,z)
    return b
    #return nummax(nummax(x,y),z)

def nummax(x,y):
    if x>y :
        return x
    else :
        return y

max=nummaxthree(10,20,30)
print ("ค่าที่มาก =",max)

# recursive Function =>เรียกฟังกชันตัวเองเพื่อวนไปเรื่อย ๆ
# หาจุดวนซ้ำ -> หาทางออกจากฟังกชัน(return) -> ต้องมีparameter
def addnumber(number):
    if number == 5:
        return
    print(number+1)
    number += 1
    addnumber(number)

addnumber(0)

def summation(number):
    if number == 1:
        return number
    else:
        return number+summation(number-1)

x = summation(5)
print(x)

# lambda function  ฟังก์ชันที่ระบุมาโดยไม่มีชื่อฟังก์ชัน แต่ก็ยังทำงานได้
#lambda arguments : expresstion
def x(name): return name
def sum(x, y): return x+y
def multiplt(a, b): return a*b

print(x("Phet"))
print(sum(5, 10))

def mypower(x):
    return lambda a: x**a

y = mypower(4)
result=y(2)
print(result)

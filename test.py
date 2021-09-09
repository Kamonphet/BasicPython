# #2-7
# row = 1 #row คือ ตัวแปรที่ใช้เก็บค่า แถว 1-12
# while row <= 12:
#     num = 2 #num คือ ตัวแปรที่ใช้เก็บค่า แม่สูตรคูณ
#     col = 1 #col คือ ตัวแปรที่ใช้เก็บค่า คอลัมน์ 1-6
#     while col <= 6: #while นี้ใช้กำหนดการแสดงแถว
#         print("%3dx%2d=%3d" % (num, row, num * row), end="")
        
#         num += 1
#         col += 1
 
#     print("")
#     row += 1
 
# print(" ")

# #8-13
# row = 1
# while row <= 12: #while ที่ 2 จะแสดงคอลัมน์
#     num = 8
#     col = 1
#     while col <= 6:
#         print("%3dx%2d=%3d" % (num, row, num * row), end=" ")
#         num += 1
#         col += 1
 
#     print(" ")
#     row += 1

# print(" ")

# #14-18
# row = 1
# while row <= 12: #while ที่ 2 จะแสดงคอลัมน์
#     num = 14
#     col = 1
#     while col <= 6:
#         print("%3dx%2d=%3d" % (num, row, num * row), end=" ")
#         num += 1
#         col += 1
 
#     print(" ")
#     row += 1

# print(" ")

# 20-24
# row = 1
# while row <= 12: #while ที่ 2 จะแสดงคอลัมน์
#     num = 20
#     col = 1
#     while col <= 5:
#         print("%3dx%2d=%3d" % (num, row, num * row), end=" ")
#         num += 1
#         col += 1
 
#     print(" ")
#     row += 1

# score1=int(input("คะแนนของนักเรียนที่ 1 >>"))
# score2=int(input("คะแนนของนักเรียนที่ 2 >>"))
# score3=int(input("คะแนนของนักเรียนที่ 3 >>"))
# score4=int(input("คะแนนของนักเรียนที่ 4 >>"))
# score5=int(input("คะแนนของนักเรียนที่ 5 >>"))
# score6=int(input("คะแนนของนักเรียนที่ 6 >>"))
# lis =[score1,score2,score3,score4,score5,score6]
# dic={">=80":"A", ">=70":"B", ">=60":"C", ">=50":"D", "<50":"F"}

# lek=1
# for i in range(len(lis)):
#     if lis[i] >=80 :
#         print("นักเรียนคนที่ ",lek," ได้เกรด ",dic[">=80"])
#     elif lis[i] >=70 :
#         print("นักเรียนคนที่ ",lek," ได้เกรด ",dic[">=70"])
#     elif lis[i] >=60 :
#         print("นักเรียนคนที่ ",lek," ได้เกรด ",dic[">=60"])
#     elif lis[i] >=50 :
#         print("นักเรียนคนที่ ",lek," ได้เกรด ",dic[">=50"])
#     else :
#         print("นักเรียนคนที่ ",lek," ได้เกรด ",dic["<50"])
#     lek = lek+1

# score1=int(input("คะแนนของนักเรียนที่ 1 >>"))
# score2=int(input("คะแนนของนักเรียนที่ 2 >>"))
# score3=int(input("คะแนนของนักเรียนที่ 3 >>"))
# score4=int(input("คะแนนของนักเรียนที่ 4 >>"))
# score5=int(input("คะแนนของนักเรียนที่ 5 >>"))
# score6=int(input("คะแนนของนักเรียนที่ 6 >>"))

# lis =[score1,score2,score3,score4,score5,score6]
# dic={">=80":"A", ">=70":"B", ">=60":"C", ">=50":"D", "<50":"F"}

# for i in range(lis) :
# if lis[i] >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score1 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score1 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score1 >=50 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# if score2 >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score2 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score2 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score2 >=50 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# if score3 >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score3 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score3 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score3 >=50 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else : 
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# if score4 >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score4 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score4 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score4 >=50 :
#   pprint("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# if score5 >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score5 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score5 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score5 >=50 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# if score6 >=80 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=80"])
# elif score6 >=70 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=70"])
# elif score6 >=60 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=60"])
# elif score6 >=50 :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic[">=50"])
# else :
#   print("นักเรียนคนที่ 1 ได้เกรด ",dic["<50"])

# import numpy as nupy
# a=nupy.array([[1,2,3],[4,5,6]])
# b=nupy.array([[7,8,9],[10,11,12]])
# print("a =","\n",a)
# print("b =","\n",b)
# print("---------------")
# print("a+b","\n",a+b)
# print("a-b","\n",a-b)
# print("a*b","\n",a*b)
# print("b/a","\n",b/a)
# print("a**b","\n",a**b)


# player = int(input('please enter count player :'))
# kanan=[]
# for i in range(player):
#   print('--------คนที่',i+1)
#   for j in range(1) :
#     lek=int(input('ใส่เลข ='))
#     lek+=int(input('ใส่เลข ='))
#     kanan.append(lek)

# for x in kanan:
#     print(x)
    

# print('เป็นผู้ชนะคะแนนสูงสุด',max(list))
# print('ผู้เล่นคนที่',list[max(list)])
# print(31%26)

def a(name):
    return 10

a(45)
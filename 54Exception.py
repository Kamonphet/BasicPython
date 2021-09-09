# Exception การจัดการข้อผิดพลาด
# การที่โปรแกรมของเรานั้นผิดพลาดแล้วเราต้องหาวิธีในการแก้ปัญหาเพื่อให้แสดงออกมาให้ผู้ใช้รู้ว่าผิดพลาดอย่างไร

# try exect
'''
try:
    คำสั่งรันโปรแกรมปกติ
except:
    คำสั่งที่ทำงานตอนโปรแกรมมีข้อผิดพลาด
'''
try:
    number1 = int(input("enter number 1 :"))
    number2 = int(input("enter number 2 :"))
    result = number1/number2
    print(result)
except ValueError:
    print("ต้องป้อนตัวเลขเท่านั้นถึงจะหารได้")
except ZeroDivisionError:
    print("ห้ามหารด้วยเลข 0")
except TypeError:
    print("ชนิดข้อมูลไม่ถูกต้อง")

# exection หลาย ๆ เหตุการณ์          /  \
    # valueError => ค่าผิดพลาด        |
    # ZeroDivision => ผิดพลาดที่เลข 0  |
    # TypeError => ชนิดข้อมูลไม่ตรงกัน   |

# ลดรูป exection
    # except Exception as e:
    # print(e)
    # else :                   #มาสามารถใส่ else ได้สำหรับถ้าไม่มีช้อผิดพลาด
    # print("จบโปรแกรม")

# finally คล้าย else แต่จะทำงานได้ทั้งตอนผิดพลาดและไม่พิดพลาดของโปรแกรม
finally:
    print("ทำงานต่อไป...")

# ทำงานร่วมกับloop while
while True:
    try:
        name=input("ป้อนชื่อผู้ใช้โปรแกรม :")
        if name == "phet" :
            print("มีชื่อนี้ในระบบแล้ว")
        number1 = int(input("enter number 1 :"))
        number2 = int(input("enter number 2 :"))
        if number1 == 0 and number2 == 0:
            break
        if number1 < 0 or number2 < 0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")
        result = number1/number2
        print(result)
    except Exception as e:
        print(e)
    finally:
        print("ทำงานต่อไป...")

# raise กำหนดข้อผิดพลาดเอง ต้องเขียนภายใต้ try

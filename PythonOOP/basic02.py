# constructor เป็น medthod พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ
#  def__init__(self):

# destructor เป็น medthod พิเศษที่จะถูกใช้งานเมื่อสิ้นสุดการทำงานของ class
# หรือถูกทำก่อนจะสลาย obj ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ
#  def__del__(self):

class Employee:

    def __init__(self):
        print("Defult Constructor")

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showdata(self):
        print("complete attribute")
        print("name = {}".format(self.name))
        print("salary = ",self.salary)
        print("Department = ",self.department)

    def __del__(self):
            print("Call Destructor")
            
# สร้างobj
obj1 = Employee("phet",50000,"Teacher")
# ปรับเปลี่ยนค่าได้โดย ชื่อตัวแปร.parameter = ค่าใหม่
obj1.salary = 70000

obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")

# เรียกใช้งาน medthod showdata
obj1.showdata()


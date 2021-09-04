# ชื่อ,เงินเดือน
# การสร้าง Class = ต้นแบบของวัตถุ
class Employee:
    # สร้าง medthod = ทำฟังก์ชัน def
    def detail(self,name,salary,department):
        print("เรียกใช้งานmedthod ใน class Employee")
        # สร้าง Attribute = กำหนดตัวแปร self.+ชื่อตัวแปร = str,int,float,ตัวแปร
        self.name = name
        self.salary = salary
        self.department = department

    def showdata(self):
        print("complete attribute")
        print("name = {}".format(self.name))
        print("salary = ",self.salary)
        print("Department = ",self.department)

# การสร้างวัตถุ = สิ่งที่ถูกสร้างขึ้้นจากคลาส
# ประกอบไปด้วย 2 อย่าง คือ คุณสมบัติ(Attribute)และพฤติกรรม(Medthod)
obj1 = Employee()
obj2 = Employee()
obj3 = Employee()

# เรียกใช้งาน medthod  detail
obj1.detail("phet",50000,"Teacher")
obj2.detail("Flim",100000,"Bussines")
obj3.detail("Family",150000,"House")

# เรียกใช้งาน medthod showdata
obj1.showdata()

# constructor เป็น medthod พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มต้นสร้างวัตถุ
#  def__init__(self):

# destructor เป็น medthod พิเศษที่จะถูกใช้งานเมื่อสิ้นสุดการทำงานของ class
# หรือถูกทำก่อนจะสลาย obj ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ
#  def__del__(self):
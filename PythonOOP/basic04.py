# การห่อหุ้ม encapsulation
    # กระบวนการซ่อนรายละเอียดการทำงานไว้ภายใน
    # ภายนอกไม่สามารถเปลี่ยนแปลงแก้ไขข้อมูลได้
    # การห่อหุ่มจะสรา้งความปลอดภัยให้แก่ข้อมูล 

# access Modifire ระดับการเข้าถึง class, attribute, medthodและอื่น ๆ ใน oop
    #public เข้มงวดน้อยสุด
    # protected(_) เข้าถึงเฉพาะclassของตัวมันเองและclassที่ถูกสืบทอด วิธีเข้าก็ใส่ _
    # private(__) เข้มงวดที่สุด วิธีเข้าก็ใส่ __

class Employee:

    def __init__(self,name,salary,department):
        # private attribute
        self._name = name  #protected
        self.__salary = salary
        self.__department = department

    # protected medthod
    def _showdata(self):
        print("complete attribute")
        print("name = {}".format(self._name))
        print("salary = ",self.__salary)
        print("Department = ",self.__department)

# สร้างวัตถุ
obj1 = Employee("phet",50000,"Teacher")
obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")

obj1._showdata()
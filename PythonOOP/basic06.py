#class variable ตัวแปรที่ทำงานภายใน class ไม่ต้องสร้างobj ขึ้นมาก่อน
# instance variable ตัวแปรที่อยู่ภายใน obj ต้องสร้างobj ขึ้นมาก่อน

class Employee:
    #class variable
    _minSalary = 12000
    _maxSalary = 50000

    def __init__(self,name,salary,department):
        # instance variable
        self._name = name  #protected
        self.__salary = salary
        self.__department = department

    # protected medthod
    def _showdata(self):
        print("complete attribute")
        print("name = {}".format(self.__name))
        print("salary = ",self.__salary)
        print("Department = ",self.__department)

# สร้างวัตถุ
obj1 = Employee("phet",50000,"Teacher")
obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")


#เรียกใช้
print(Employee._maxSalary)
# obj1._showdata()

# Inheritance การสืบทอดคุณสมบัติ => การสร้างสิ่งใหม่ขึ้นด้วยการสืบทอดหรือรับเอา
# คุณสมบัติบางอย่างมากจากสิ่งเดิมที่มีอยู่แล้วโดยการสร้างเพิ่มเิมจากสิ่งที่มีอยู่แล้ว
# แบ่งเป็น superclass และ subclass

# superclass
# super() => เรียกใช้งานคุณสมบัติในsuperclass
# class Employee:
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
        print("name = {}".format(self._name))
        print("salary = ",self.__salary)
        print("Department = ",self.__department)

    def _getIncome(self) :
        return self.__salary*12
    #แปลง obj เป็น str 
    def __str__(self) :
        return ("EmployeeName = {} ,  Department = {} , SalaryPerYear = {}".format(self._name,self.__department,self._getIncome()))

# subclass
# class name(Employee):
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        # super()._showdata()

class sale(Employee):
    __departmentName = "แผนกขาย"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)


# สร้างวัตถุ
obj1 = Employee("phet",50000,"Teacher")
obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")
account = Accounting('phet',40000)
programmer = Programmer('flim',60000)
Sale = sale('love',1000)

#เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
# account._showdata()
# print("Income = {}".format(account._getIncome()))
# print(account.__str__())
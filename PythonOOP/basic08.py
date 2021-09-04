# การพ้องรูป (Polymorphism) การที่methodชื่อเดียวกัน
# สามารถรับ argument ที่แตกต่างกันได้หลายรูปแบบ
# โดยmethodนี้จะถูกเรียกว่า overload method

# overloading method = medthodชื่อเดียวกัน พารามิเตอร์ต่างกัน
# overriding method = medthodคลาสลูก ที่มีชื่อเหมือนกับmethodคลาสแม่ (inheritance)
class Employee:
    # class variable
    _minSalary = 12000
    _maxSalary = 50000

    def __init__(self, name, salary, department):
        # instance variable
        self._name = name  # protected
        self.__salary = salary
        self.__department = department

    # protected method
    def _showdata(self):
        print("complete attribute")
        print("name = {}".format(self._name))
        print("salary = ", self.__salary)
        print("Department = ", self.__department)

    def _getIncome(self,bonus=0,overtime=0) :
        return (self.__salary*12)+bonus+overtime

    #แปลง obj เป็น str 
    def __str__(self) :
        return ("EmployeeName = {} ,  Department = {} , SalaryPerYear = {}".format(self._name,self.__department,self._getIncome()))

# subclass
# class name(Employee):
class Accounting(Employee):
    __departmentName = "แผนกบัญชี"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age

    # overriding method
    def _showdata(self):
        super()._showdata()
        print("Age = ", str(self.age))
    
    def __str__(self) :
        return (super().__str__()+" Age = {} years old".format(self.age))


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"

    def __init__(self, name, salary, exp, skill):
        super().__init__(name, salary, self.__departmentName)
        self.exp = exp
        self.skill = skill
        # super()._showdata()

    def _showdata(self):
        super()._showdata()
        print("Exp = ", self.exp)
        print("Skill = ", self.skill)

    def __str__(self) :
        return (super().__str__()+" Exp = {} years old, Skill = {}".format(self.exp,self.skill))



class sale(Employee):
    __departmentName = "แผนกขาย"

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area

    def _showdata(self):
        super()._showdata()
        print("Aera = ", self.area)
    
    def __str__(self) :
        return (super().__str__()+" Area = {}".format(self.area))


# สร้างวัตถุ
obj1 = Employee("phet", 50000, "Teacher")
obj2 = Employee("Flim", 100000, "Bussines")
obj3 = Employee("Family", 150000, "House")
account = Accounting('phet', 40000, 30)
programmer = Programmer('flim', 60000, 2, "game dev")
Sale = sale("love", 1000, "BKK")

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
print("Account_Income = {}".format(account._getIncome()))
print(account.__str__())
# programmer._showdata()

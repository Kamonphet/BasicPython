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

# สร้างวัตถุ
obj1 = Employee("phet", 50000, "Teacher")
obj2 = Employee("Flim", 100000, "Bussines")
obj3 = Employee("Family", 150000, "House")

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
# programmer._showdata()

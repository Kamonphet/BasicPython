# subclass
# class name(Employee):

from basic09Employee import Employee
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


# สร้างวัตถุ
account = Accounting('phet', 40000, 30)

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
# print("Account_Income = {}".format(account._getIncome()))
# print(account.__str__())
# print("------------------------------------------")
# programmer._showdata()

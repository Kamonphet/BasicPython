from basic09Employee import Employee
from basic09accounting import Accounting
from basic09programmer import Programmer
from basic09sale import Sale


# สร้างวัตถุ
obj1 = Employee("phet", 50000, "Teacher")
obj2 = Employee("Flim", 100000, "Bussines")
obj3 = Employee("Family", 150000, "House")
account = Accounting('phet', 40000, 30)
programmer = Programmer('flim', 60000, 2, "game dev")
sale = Sale("love", 1000, "BKK")

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
print("Account_Income = {}".format(account._getIncome()))
print(account.__str__())
print("------------------------------------------")
print("Programmer_Income = {}".format(programmer._getIncome()))
print(programmer.__str__())
print("------------------------------------------")
print("Sale_Income = {}".format(sale._getIncome()))
print(sale.__str__())
print("------------------------------------------")
# programmer._showdata()

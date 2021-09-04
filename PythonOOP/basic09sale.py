# subclass
# class name(Employee):

from basic09Employee import Employee
class Sale(Employee):
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
sale = Sale("love", 1000, "BKK")

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
# print("Sale_Income = {}".format(sale._getIncome()))
# print(sale.__str__())
# print("------------------------------------------")
# programmer._showdata()

# subclass
# class name(className):

from basic09Employee import Employee
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

# สร้างวัตถุ
programmer = Programmer('flim', 60000, 2, "game dev")

# เรียกใช้
# print(Employee._maxSalary)
# print(account._minSalary)
# print("Programmer_Income = {}".format(programmer._getIncome()))
# print(programmer.__str__())
# print("------------------------------------------")
# programmer._showdata()

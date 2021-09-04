# isinstance => เช็คว่า objนี้ถูกสร้างขึ้นจ่ก class ที่เรานิยามหรือไม่
# dir => แสดง attribute แลำ medthod
# __class__ => แสดงชื่อ class ของobj

class Employee:

    def __init__(self):
        print("Defult Constructor")

    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showdata(self):
        print("complete attribute")
        print("name = {}".format(self.name))
        print("salary = ",self.salary)
        print("Department = ",self.department)

# สร้างวัตถุ
obj1 = Employee("phet",50000,"Teacher")
obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")

# เช็ค obj ว่าอยู๋ใน classนั้น ๆ หรือไม่
print(isinstance(obj1,Employee))

# เช็ค att,med
print(dir(obj1))

#เช็ค class ของobjนั้น ๆ 
print(obj1.__class__)

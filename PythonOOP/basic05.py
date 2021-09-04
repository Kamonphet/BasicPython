#setter medthod การกำหนดค่าให้ obj
# def setName(self,newname):
#     self.__name=newname
#getter medthod การดึงค่าจาก obj
# def getName(self):
#     return self.__name

class Employee:

    def __init__(self,name,salary,department):
        # private attribute
        self._name = name  #protected
        self.__salary = salary
        self.__department = department

    # protected medthod
    def _showdata(self):
        print("complete attribute")
        print("name = {}".format(self.__name))
        print("salary = ",self.__salary)
        print("Department = ",self.__department)

    #setter
    def setName(self,newname):
        self.__name=newname

    #getter
    def getName(self):
        return self.__name

# สร้างวัตถุ
obj1 = Employee("phet",50000,"Teacher")
obj2 = Employee("Flim",100000,"Bussines")
obj3 = Employee("Family",150000,"House")

#เรียกใช้ setter
obj1.setName("Flim")

#เรียกใช้ getter
obj1.getName()
print("Name =",format(obj1.getName()))

# obj1._showdata()
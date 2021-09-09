#Pass
#มีไว้เพื่อเป็นโครงสร้างควบคุมไว้ก่อน เป็นการบ่งบอกว่าให้ผ่านการทำงานนั้นไปก่อน เพื่อให้โค้ดสามารถรันได้
age=int(input("ป้อนอายุของคุณ :"))
if age<=15 :
    if age==15 :
        pass
    elif age==14 :
        pass
    else :
        print("ประถมศึกษา")
else :
    print("จบโปรแกรม") 



#pass in function
def getname():
    pass

getname()

#Break / Continue

#Break คือคำสั่งที่ทำให้ออกจากลูปเลย
#Continue คือคำสั่งกระโดดข้ามคำสั่งต่อไปเลย

i=1
while i<=10:
    print("รอบที่ :" ,i)
    if(i==5) :
        break
    i+=1

print("จบโปรแกรม")


i=0
while i<=10:
    i+=1
    if(i==5) :
        continue
    print("รอบที่ :" ,i)

print("จบโปรแกรม")
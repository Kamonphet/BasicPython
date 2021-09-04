#return
#ใช้ส่งค่าคืนเพื่อนำไปใช้ต่อ
#สามารถใช้ออกจากฟังชันได้
def rottery(x):
    if len(x)<3 :
        return
    if x == "100":
        print("ถูกรางวัล")
        return 1000
    else:
        print("ไม่ถูกรางวัล")
        return 0

money = rottery("613")
print("รางวัล =",money)

y_n=input("จะส่งหรือไม่ (ส่ง=y / ไม่ส่ง=n) : ")
if y_n == "y":
    distance = float(input("ระยะทาง :"))
    if distance > 500:
        print("ค่าส่ง 45 บาท")
    elif distance >= 301:
        print("ค่าส่ง 35 บาท")
    elif distance >= 101:
        print("ค่าส่ง 25 บาท")
    elif distance >= 51:
        print("ค่าส่ง 15 บาท")
    elif distance >= 5:
        print("ค่าส่ง 10 บาท")
    else :
        print(distance,"< 5 !!!!ส่งฟรี!!!!")
    print("******************************")
    print("ขอบคุณที่ใช้บริการ")
elif y_n == "n":
    print("******************************")
    print("ขอบคุณที่ใช้บริการ")
else :
    print("ERROR!! PLEASE CHECK YOUR ANSWER!")
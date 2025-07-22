#ver1
# distance=float(input("ระยะทาง :"))
# if distance>=5 and distance<=50:
#     print("10 บาท")
# elif distance>=51 and distance<=100:
#     print("15 บาท")
# elif distance>=101 and distance<=300:
#     print("25 บาท")
# elif distance>=301 and distance<=500:
#     print("35 บาท")
# elif distance>500:
#     print("45 บาท")
# else :
#     print(distance,"< 5 !!!!ส่งฟรี!!!!")
#ver2
distance=float(input("ระยะทาง :"))
if distance>500:
    print("45 บาท")
elif distance>=301:
    print("35 บาท")
elif distance>=101:
    print("25 บาท")
elif distance>=51:
    print("15 บาท")
elif distance>=5:
    print("10 บาท")
else :
    print(distance,"< 5 !!!!ส่งฟรี!!!!")
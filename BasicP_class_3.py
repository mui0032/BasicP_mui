# # # # # # has_rice = True
# # # # # # has_spoon = True

# # # # # # if has_rice == True:
# # # # # #     print("มีข้าวแล้ว")
# # # # # #     if has_spoon:
# # # # # #         print("มีช้อน กินข้าวได้")
# # # # # #     else:
# # # # # #         print("ไม่มีช้อน กินข้าวไม่ได้")

# # # # # # if has_rice == True and has_spoon == True:
# # # # # #     print("มีช้อน มีข้าว กินข้าวได้")
# # # # # # else:
# # # # # #     print("ไม่มีข้าวหรือไม่มีช้อน กินข้าวไม่ได้")

# # # # # wakeup = True
# # # # # go_university = True

# # # # # if wakeup == True and go_university == True:
# # # # #     print("ตื่นแล้ว ไปเรียนๆ")
# # # # # else:
# # # # #     print("ตื่นเถิดคนดี")

# # # # for index in range(1 , 6):
# # # #     print("Round : ", index , "Hello World")

# # # t = True
# # # for index in range(1 , 7):
# # #     if index == 3:
# # #         print("Round : ", index ,"starter pack")
# # #         if t == True:
# # #             print("จริง")
# # #         else:
# # #             print("เท็จ")
# # #     else:
# # #         print("Round : ", index , "Hellow world")

# # num = float(input("Please Enter Number : "))
# # times = int(input("Please Enter Times for minus : "))

# # for times in range (1 , times+1):
# #     print("Times :",times)
# #     minus_num = int(input("Please Enter number for minus : "))
# #     num = num-minus_num
# #     print("sum :", num)
# # choice = 0
# i = 0
# while i != 1:
#      choice = input("จบเลย = กดอะไรก็ได้ / ยังก่อน = กด 1 : ")
#     print("ยังก่อน")
#     break

monster = 100
arrow = 10
bomb = 50
sword = 25

print("คุณจะโจมตีมอนเตอร์หรือไม่?")
print("1.โจมตี")
print("2.หนี")
choice = int(input("กด 1 / 2 : "))
if choice == 1 :
    times = int(input("คุณจะเลือกโจมตีกี่ครั้ง"))
    for times in range (times):
        if times == times - 1:
            if monster > 0:
                print("คุณตาย")
        elif times > 0:
            if monster > 0 and times < time:
            print("HP of monster : ", monster)
            print("คุณจะใช้อาวุธอะไรในการโจมตี?")
            print("1.arrow")
            print("2.bomb")
            print("3.sword")
            weapon = int(input("กด 1 / 2 / 3 : "))
            if weapon == 1:
                monster = monster - arrow
        else:
            print("คุณจะใช้อาวุธอะไรในการโจมตี?")
            print("1.arrow")
            print("2.bomb")
            print("3.sword")
            weapon = int(input("กด 1 / 2 / 3 : "))
            if weapon == 1:
                monster = monster - arrow
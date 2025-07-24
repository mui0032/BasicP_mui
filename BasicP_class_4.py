# # # # # # # # # def pnt_hello(year):
# # # # # # # # #     print("Hello Starter Pack #", year)
# # # # # # # # # pnt_hello(31)

# # # # # # # # def sum(num1,num2):
# # # # # # # #     print("Sum = ",num1 + num2)
# # # # # # # # sum2 = sum(1,2)
# # # # # # # # print(sum2)

# # # # # # # def eat_rice(has_rice, has_spoon):
# # # # # # #     if has_rice == 1 and has_spoon == 1:
# # # # # # #         return "กินข้าวได้"
# # # # # # #     if has_rice == 0 or has_spoon == 0:
# # # # # # #         return "อดกินนะ"
# # # # # # # print(eat_rice(True,True))

# # # # # # def calculator( num1 , num2 , cmd ):
# # # # # #     if cmd == "sum":
# # # # # #         return num1 + num2
# # # # # #     elif cmd == "minus":
# # # # # #         return num1 - num2
# # # # # #     elif cmd == "multiple":
# # # # # #         return num1 * num2
# # # # # #     elif cmd == "divi":
# # # # # #         return num1 / num2
# # # # # #     elif cmd == "power":
# # # # # #         return  num1 ** num2
# # # # # #     elif cmd == "mod":
# # # # # #         return num1 % num2
# # # # # # print(calculator(5 , 4 , "mod"))

# # # # # box = ["a" , "b"]
# # # # # print(box)
# # # # # box.append("c")
# # # # # print(box)

# # # # for i in range(5):
# # # #     print (i, "Starter Pack")
# # # # print("***************************")
# # # # for i in [0,1,2,3,4,]:
# # # #     print(i, "Starter Pack")

# # # box_fruit = ["apple" , "strawbery" , "banana"]
# # # for fruit in box_fruit:
# # #     if fruit == "strawbery":
# # #         print("เจอสตอเบอรี่แล้ว!!! อร่อยมากกกกก")
# # #     else:
# # #         print("สตอเบอรี่แล้วอยู่หนายยยยยย")

# # box_fruit = ["apple" , "strawbery" , "banana"]
# # def find_fruit(any_fruit):
# #     for fruit in box_fruit:
# #         if fruit == any_fruit:
# #             print("mitsukatta!", any_fruit ,"ga oishii na")
# #         else:
# #             print("mitsukara nai desu")
# # any_fruit = input("Please enter what fruit do you want to find ?: ")
# # find_fruit(any_fruit)

# students = {"name_student" : "Mui" , "age" : 18 , "ID" : 68130500032}
# if students["age"] < 18:
#     print("ไม่ผ่าน")
# else :
#     print("ผ่าน")

students = [{"name" : "Mui" , "age" : 18 , "ID" : 68130500032} , 
            {"name" : "Lamon" , "age" : 20 , "ID" : 68130500046}]
for student in students:
    if student["age"] > 18:
        print(student["name"] , "อายุมากกว่า 18")
    elif student["age"] < 18:
        print(student["name"] , "อายุน้อยกว่า 18")
    else:
        print(student["name"] , "อายุ 18 พอดี")
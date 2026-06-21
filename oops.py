# x=10
# print(type(x))
# y="Ajith"
# z=("ajith","kumar","s")
# a=["ajith","kumar","s"]
# b={"name":"ajith"}
# print (type(x))
# print (type(y))
# print (type(z))
# print (type(a))
# print (type(b))

# type(function used to determine the type of the object)

# def hello():
#     print("helllo")

# print(type(hello))


# class car :
#     carname=input("enter the name")
#     mileage=int(input("enter the mileage"))
#     def racecar(self):
#         return "its race car "
#     def family(self):
#         return "family car "

# car1=car()
# car2=car()
# print(car1.carname)
# car2.carname="honda"
# print(car1.carname)
# print(car2.carname)

# class Bank:
#     def __init__(self, name, balance, acc_num):
#         self.name = name
#         self.balance = balance
#         self.__acc_num = acc_num

#     def __str__(self) -> str:
#         pass

#     def get_name(self):
#         print(f"She is my sister {self.name}")

#     def get_acc_num(self):
#         return self.__acc_num
    
#     #setter
#     def set_acc_num(self,acc_num):
#         self.__acc_num=acc_num

# # Creating an instance of the Bank class
# sham = Bank("Shamini", 100000, 123)

# # Calling the get_name method
# print(sham.get_acc_num())

# sham.set_acc_num(456)

# print(sham.get_acc_num())

# # Printing the name attribute
# # print(sham.name)


# class Veh:
#     def __init__(self,wheels,airbag):
#         self.wheels=wheels
#         self.airbag=airbag

#     def move(self):
#         print("moving")

# # veh1=veh(4,5)
# # print(veh1.airbag)

# class Car(Veh):
#     windows=3


# car1 = Car(4,5)

# print(car1.wheels)
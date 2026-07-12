# odd or even problem
# def oddeven(number):
#     if number % 2==0:
#         return "add"
#     else:
#         return "odd"
    
# #input
# number = int(input("enter the number: "))
# print(oddeven(number))

#Write a program to find the given number is positive or negative.

# def checker(x):
#     if x == 0:
#         return "the number is zero"
#     elif x > 0:
#         return"the number is positive"
#     else:
#         return "negative"
    
# #input
# number = int(input("enter the number"))

# #output

# print(checker(number))

#Write a program to find the sum of two numbers.

# def sumofnum(x,y):
#     return x+y
# x = int(input("enter the number: "))
# y = int(input("enter the number: "))

# print(sumofnum(x,y))

#Write a program to find if the given number is prime or not.

# def prime(x):
#     for i in range(2,x):
#         if x%i==0:
#             return "not a prime"
#         else:
#             return "prime"
# num = int(input("enter the number: "))

# print(prime(num))

#Write a program to check if the given number is palindrome or not.

# def palindrome(x):
#     reverse_x = x[::-1]

#     if x == reverse_x:
#         return "its palindrome"
#     else:
#         return "it's not a palindrome"

# #input
# number = input("enter the sequence: ")
# #output
# print(palindrome(number))

#Write a program to check if the given number is Armstrong  

#Armstrong number is a number that is equal to the sum of cubes of its digits
# . For example 0, 1, 153, 370, 371 and 407 
# are the Armstrong numbers. Let's try to understand why 153 is an Armstrong number.

# def amstrong(x):

#     temp = x
#     p = len(str(x))
#     sum=0

#     while temp > 0:
#         digit = temp % 10
#         sum = sum + digit**p
#         temp=temp//10

#     if sum == x:
#         return "Armstrong"
#     else:
#         return"Not a Armstrong"
# #input
# numer = int(input("enter the number: "))
# #output
# print(amstrong(numer))

# Write a program to check if the given strings are anagram or not.
# def anagram(x,y):
#     if sorted(x) == sorted(y):
#         return "its anagram"
#     else:
#         return "No,it's not a anagram"
    
# #input
# string1=input("enter thr string 1: ")
# string2=input("enter thr string 2: ")
# #output
# print(anagram(string1,string2))


#Write a program to find a maximum of two numbers.

# def max(x,y):
#     if x>y:
#         return x 
#     elif x==y:
#         return " Equal numbers "
#     else:
#         return y

# #input
# x=int(input("enter the number 1: "))
# y=int(input("enter the number 2: "))
# #output
# print(f"the max value is :{max(x,y)}")


#min
# def min(x,y):
#     if x>y:
#         return y
#     elif x==y:
#         return " Equal numbers "
#     else:
#         return x

# #input
# x=int(input("enter the number 1: "))
# y=int(input("enter the number 2: "))
# #output
# print(f"the min value is :{min(x,y)}")

#Write a program to find a maximum of three numbers.
# def maxthree(x,y,z):
#     if x > y and x > z:
#         return x
#     elif y > x and y > z:
#         return y
#     return z
# #input
# x=int(input("enter the number: "))
# y=int(input("enter the number: "))
# z=int(input("enter the number: "))
# #output
# print(f"the max value is :{maxthree(x,y,z)}")

#Write a program to find a minimum of three numbers.

# def minthree(x,y,z):
#     if x < y and x < z:
#         return x
#     elif y < x and y < z:
#         return y
#     return z
# #input
# x=int(input("enter the number: "))
# y=int(input("enter the number: "))
# z=int(input("enter the number: "))
# #output
# print(f"the max value is :{minthree(x,y,z)}")

#Write a program to find a factorial of a number.

# def factorial(x):
#     f = 1
#     for i in range(1,x+1):
#         f=f*i
#     return f

# #input
# number = int(input("enter the number: "))
# #output
# print(f"the factorial is: {factorial(number)}")

#Write a program to find a fibonacci of a number.
# def fibonacci(x):
#     a=0
#     b=1
#     print(a)
#     print(b)
#     for i in range(1,x):
#         c=a+b
#         a=b
#         b=c
#     return c
# #input
# number = int(input("enter the number: "))
# fibonacci(number)
# #output
# print(f"the series is {fibonacci(number)}")


#list comprehension 

# list1=[1,2,3,4,5]
# square =[x for x in list1 if x%2==0]
# print (square)


#decorator

def decorator(func):
    def condition(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return condition

@decorator
def div(a,b):
    num=a/b
    print(num)

#div(2,4)

s="THIS IS AJITH KUMAR FROM CSE DEPARTMENT"
ot=s.split()
# print(ot)
op="".join(s)
# print(op)


# print(dir(abc))
# print(help(abc.abstractmethod))



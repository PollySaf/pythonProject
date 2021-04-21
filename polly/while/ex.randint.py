 #ex.4.1
# i=0
# num1=0
# num2=0
# num1=int(input("enter num:  "))
# num2=int(input("enter num:  "))
# for i in range (num1+1,num2):
#     if i%2==0:
#        print (i)
# print("end of session")


# ex.4.2
# i=2
# a=1
# num=int(input("enter num:  "))
# for a in range(i,num):
#     if num%a==0:
#         print("the number isn't prime")
#         break
# else:
#          print("the number is prime" )

# ex.4.3
#
# from random import randint
# num=randint(1,9)
# num1=int(input("enter num:   "))
# while num1>1 and num1<9:
#     if num1<num:
#      print ("the num is low")
#      num1 = int(input("enter num:   "))
#     if num1>num:
#      num1 = int(input("enter num:   "))
#      print("the num is high")
#     if num1==num:
#      num1 = int(input("enter num:   "))
#      print("the num is right")

# ex4.4
#  my.num.is.25

# from random import randint
# system_guess=randint(0,100)
# print(system_guess)
# answer=input("low or high or right?")
# h1=100
# l1=0
# counter=0
# while answer!="right":
#     if answer=="high":
#         h1 = system_guess - 1
#
#     if answer=="low":
#         l1=system_guess+1
#     system_guess = randint(l1, h1)
#     print(system_guess)
#     answer = input("low or high or right?")
#     counter+=1
# #     76
# print("good job")
# print(counter)


# ex4.5
# num=int(input("how many numbers do you want?    "))
# first=0
# second=1
# print(first)
# print(second)
# for i in range(num-2):
#     new=first+second
#     first=second
#     second=new
#     print(new)
# ex4.6
# sum=0
# text=input("enter string: ")
# for i in text:
#     if i=="m":
#         sum+=1
#         continue
#     if i!="m":
#         continue
# print(sum)
#
#







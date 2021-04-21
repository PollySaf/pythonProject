#5.2

# str="banana"
# print(str[::-1])


# # 1
# str=input("enter string:  ")
# # banana
# str_new=""
# # bnn
#
# for i in (str):
#     if i.upper()!="A":
#        str_new=str_new+i
# print(str_new)



#2
# str=input("enter string:  ")
# str_new=""
#
# for i in (str):
#     print(f"{str[0]}{str[-1]}")


# 3
# from random import *
#
# name=input("enter string: ")
# password=" "
#
# for i in range(6):
#     num=randint(0,len(name)-1)
#     digit=name[num]
#     password+=digit
# print(password)



# ex.4

# str1=input("enter string: ")
# str2=input("enter string: ")
# counter=0
#
# for i in str1:
#     if i in str2:
#      counter+=1
# print(counter)


# 5

# str1=input("enter string:   ")
# str2=input("enter string:   ")
# print(str2.count(str1))
# print(str2.find(str1))
# list1=[]
# count=0
# for i in range(0,len(str2)):
#     res=str2.find(str1,count)
#     print("res: ", res)
#     list1.append(res)
#     co
#     unt=res+1
#     if res==-1:
#         break
# list1.pop()
# print(list1)
# str1=input("enter string:   ")
# str2=input("enter string:   ")
#
# str1=input("enter string:   ")
# str2=input("enter string:   ")
# start=o
# list_index=[]
# for i in range(str2.count(str1)):
#     str1_loc=str2.index(str1,start)
#     print(str1_loc)
#     start_search=str1_loc+1
#     list_index.append(str1_loc)
# print(list_index)





# 6
# list=input("enter sentence:  ")
# list=list.split()
# str= ""
#
# for i in (list):
#     str=str+ i.capitalize()+" "
# print(str)

# 7
#
# sen=input("enter sentence: ")
# letter=input("enter letter: ")
# count=sen.count(letter)
# for i in range(count):
#     sen=sen.replace(letter,letter.capitalize())
# print(sen)





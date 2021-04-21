# import datetime
# print(datetime.datetime.now())
# print(datetime.datetime(2020,12,12,23,59,59))

#
# 9.1
# name=input("what is your name")
# age=int(input(("how old a u")))
# from datetime import datetime
# now=datetime.now()
# year=now.strftime("%Y")
# year=int(year)+100-age
# print(year)

# 9.2
#
# from datetime import *
# now=datetime.now()
# DD=now.strftime("%d")
# MM=now.strftime("%m")
# YY=now.strftime("%y")
# print(DD+"/"+MM+"/"+YY)
# print(MM+"/"+DD+"/"+YY)

# from datetime import datetime
# datetime.now()
# now=datetime.now()
# DD=now.strftime("%d")
# MM=now.strftime("%m")
# YY=now.strftime("%y")
# print(DD+"/"+MM+"/"+YY)
# print(MM+"/"+DD+"/"+YY)
#
# 9.3
from datetime import *

day = input("enter day of b-day: ")
month = input("enter month of b-day: ")
year = input("enter year of b-day: ")


date_string = day + " " + month + " " + year
datetime_object = datetime.strptime(date_string, "%d %B %Y")

print(datetime_object.strftime("%Y-%m-%d"))

#
# 9.4
# import datetime
# DD=int(input("enter day: "))
# if DD==5 or DD==6:
#     DD=DD+5
# elif DD==0:
#     DD=DD+6
#
# today=datetime.datetime(DD,1,1)
# print(today.strftime("%A"))
#
# from datetime import *
# now=datetime.now()
# YY=now.strftime("%Y")
# MM=now.strftime("%B")
# print(today.strftime("%A"),MM,YY)
# date=input("enter date:  ")
# dateInput= datetime.datetime.strptime(date, "%d %b %y ")
# print(str(dateInput))


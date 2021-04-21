num=int(input("enter the number"))

while num>99 and num<1000:
    print(num//100+num//10%10+num%10)
    num =int(input("enter the number"))
    print("failed")


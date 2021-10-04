# int1=((input("enter your no")))
# if 50>=int:
#     print("no is less than 50")

int1=int(input("enter number::"))
if int1>50:
    if int1%2==0:
      print("no is divisible by 2")
    else:
        print("not divisible")
elif int1<50:
    if int1%2==0:
        print("no is even")
    else:
        print("even not")

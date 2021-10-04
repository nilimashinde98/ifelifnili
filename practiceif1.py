a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
opr= input("enter any opreator")
if opr=="+" or opr=="addition":
    print(a+b)
elif opr=="-" or opr=="substraction":
    print(a-b)
elif opr=="/" or opr=="division":
    print(a/b)
elif opr=="*" or opr=="multiplication":
    print(a*b)
elif opr=="**" or opr=="exponent":
    print(a**b)
elif opr=="//" or opr=="floor division":
    print(a//b)
elif opr=="%" or opr=="module":
    print(a%b)
else:
    print("enter valid operator.")
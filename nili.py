a=int(input("enter the no"))
b=int(input("enter the no"))
c=int(input("enter the no"))
d=int(input("enter the no"))
e=int(input("enter the no"))
if a>b:
    print("2nd largest is ",a)
    if b>c:
        print("2nd largest is ",b)
        if c>d:
            print("2nd largest no ",c)
            if d>e:
                print("2nd largest no ",d)
                if e>a:
                    print("2nd largest no ",e)
                else:
                    print("2nd largest no ",a)
            else:
                print("2nd largest no is",e)
        else:
            print("2nd no is greater",d)
    else:
        print("2nd largest is greater",c)
else:
    print("second largest is greater",b)
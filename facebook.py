# num1=int(input("enter 1st no"))
# num2=int(input("enter 2nd no"))
# num3=int(input("enter 3rd no"))
# if num1>num2:
#     print("num1 is maximum")
# elif num2>num3:
#     print("num2 is maximum")
# elif num3>num1:
#     print("num3 is maximum")
# # else:
# #     print("no is minimum")



print("welcome in facebook")
language=input("enter your language")
if language=="english" or "hindi" or "marathi":
    name=(input("enter your name"))
    if name=="nilimashinde":
        email_id=input("enter your email")
        if email_id=="nilima@gmail.com":
            password=input("enter your password")
            if password==password:
                gender=input("enter the gender")
                if gender=="male" or "female" or "others":
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")  
    else:
        print("invalid")              
else:
    print("invalid")

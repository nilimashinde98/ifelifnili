day=input("enter you day: ")
meal=input("enter your meal,breakfast or lunch or dinner: ")
if day == "monday":
 
    if meal == "breakfast":
       print("poha")
    elif meal == "lunch":
       print("rajma chaval")
    elif meal == "dinner":
       print("bhaji chapati")

elif day == "tuesday":
    if meal=="breakfast":
        print("poori sabji")
    elif meal =="lunch":
        print("only rice")
    elif meal == "dinner":
        print("chicken")

elif day == "wednsday":
    if meal =="breackfast":
         print("tupka")
    elif meal == "lunch":
        print("paratha")
    elif meal == "dinner":
        print("roti sabji")

elif day == "thursday":
    if meal == "breakfast":
        print("magiii")
    elif meal == "lunch":
        print("vegetable rice roti")
    elif meal == "dinner":
        print("ooots")

elif day == "friday":
    if meal == "breakfast":
        print("appeee")
    elif meal == "lunch":
        print("puranpoli")
    elif meal == "dinner":
        print("mataki")

elif day == "saturday":
    if meal == "breakfast":
        print("pasta")
    elif meal == "lunch":
        print("chicken tikkka masala")
    elif meal == "dinner":
        print("coconut vegeterian korma")
else:
    print("go to hotel")



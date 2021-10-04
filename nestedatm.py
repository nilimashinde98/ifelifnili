
print ( " *Welcome to Pune Bank " )
print ( " Please swipe your atm card " )
balance = 5000000
lang = input ( " Which language do you prefer ? " )
if lang == "english" or lang == "ENGLISH" or lang == "English" :
    PIN = int ( input ( " Enter your PIN number : " ) )
    if PIN>=1 and PIN<=9  :
        print ( " Correct PIN number. " )
        trans = input ( " Enter the type of transaction ( Please enter number from 1-6 ) : " )
        if trans == "1" :
            print ( " 1. Balance enquiry " )
            slip = input ( "Do you want a receipt of your account balance? (yes or no): " )
            if slip == "yes" :  
                print ( "Here is your receipt. Please collect it. Thanks for using Pune Bank! " 
                 
# With the help of [If], [elif], [else] I Make A my First Assistant "Dl Chat Bot"

print("Hi, I am 'DL-Bot'. Do you want to make a driving license?")
Decision1 = (input("Yes and No:-> "))


if Decision1 .lower()== "yes": 
   age =int(input ("Enter Your Age"))
   if age >= 18:
        print("You are eligible for a driving license!")
        Decision2 = input("Are you want to apply ''driving license'' ")
        if Decision2 .lower()== "yes":
            print("Go to 'parivahan.gov.in' Portal ")
        elif Decision2 .lower()== "no":
            print("Ok But, you are eligible. You can aaply in future by 'parivahan.gov.in' Portal")
            print("Ok, Thank You")
        else:
            print("Invalid input! Please enter Yes or No.")
   else:
        print("You are not eligible. You must be at least 18 years old.")

elif Decision1 .lower()== "no":
    print('Soory, we are only here for "diving Lincance reletted services"')

else:
    print("Invalid input! Please enter Yes or No.")




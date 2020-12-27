from validate_email import validate_email
from datetime import date 
from dateutil import parser
import holidays 
import Email_script
  
# Select country 
uk_holidays = holidays.UnitedKingdom() #this code snippet is from geeksforgeeks
  
# Print all the holidays in UnitedKingdom in year 2018 
for ptr in holidays.UnitedKingdom(years = 2021).items():  
    print(ptr) 

print("\nFor which event you want reminder? Please enter the date from following list with DD-MM-YYYY format.")
while(1):
    
    date = parser.parse(input("Enter date: "))

    if uk_holidays.get(date) != None :
        print('So you want to get notified for',uk_holidays.get(date),"? Great! Please share your email below.")
        while(1):
            email = input("Enter Email : ")
            is_valid = validate_email(email,verify=False)
            if bool(is_valid):
                print("You are done, we'll remind you with email on ", date)
                Email_script.email_script(email)
                break
            else:
                print("Email is invalid, Please enter again.")
        break


    else:
        print("This date doesn't have any holiday, please choose another date!")
    
    
    

# print("For which event you want to get a reminder?")
# print("Here we've a list for bunch of events.")
# print("1. New year's Eve\n")
# print("2. Guru Govind Singh Jayanti\n")
# print("3. Epiphany\n")
# print("4. Orthodox Christmas Day\n")
# print("5. Stephen Foster Memorial Day\n")
# print("6. Orthodox New Year\n")
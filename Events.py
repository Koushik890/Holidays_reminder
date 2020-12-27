from validate_email import validate_email
from datetime import date ,datetime,timedelta
from dateutil import parser
import holidays 
from Email_script import *
  
# Select country 
uk_holidays = holidays.UnitedKingdom() #this code snippet is from geeksforgeeks
  
# Print all the holidays in UnitedKingdom in year 2018 
for ptr in holidays.UnitedKingdom(years = 2021).items():  
    print(ptr) 

print("\nFor which event you would like to get reminder? Please enter the date from following list with DD-MM-YYYY format.")
while(1):
    
    remind_date = parser.parse(input("Enter date: "))
    remind_date = datetime.date(remind_date)
    msg_seding_date = remind_date - timedelta(days = 5)
    todays_date = date.today()
    if uk_holidays.get(remind_date) != None :
        print('So you want to get notified for',uk_holidays.get(remind_date),"? Great! Please share your email below.")
        while(1):
            email = input("Enter Email : ")
            is_valid = validate_email(email,verify=False)
            if bool(is_valid):
                print("You are done, we'll remind you with email on", msg_seding_date)
                message = "Reminder to take gifts for " + uk_holidays.get(remind_date) + " holiday ✨✨🎊."
                if todays_date == msg_seding_date:
                    email_script(email, message)
                    
                
                
                #Email_script.email_script(email,msg)
                break
            else:
                print("Email is invalid, Please enter again.")
        break
    else:
        print("This date doesn't have any holiday, please choose another date!")



    







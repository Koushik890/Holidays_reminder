
from datetime import date 
from dateutil import parser
import holidays 
  
# Select country 
uk_holidays = holidays.UnitedKingdom() #this code snippet is from geeksforgeeks
  
# Print all the holidays in UnitedKingdom in year 2018 
for ptr in holidays.UnitedKingdom(years = 2020).items():  
    print(ptr) 

print("\nFor which event you want reminder? Please enter the date with DD-MM-YYYY format.")
date = parser.parse(input("Enter date: "))


print(uk_holidays.get(date)) 
# print("For which event you want to get a reminder?")
# print("Here we've a list for bunch of events.")
# print("1. New year's Eve\n")
# print("2. Guru Govind Singh Jayanti\n")
# print("3. Epiphany\n")
# print("4. Orthodox Christmas Day\n")
# print("5. Stephen Foster Memorial Day\n")
# print("6. Orthodox New Year\n")
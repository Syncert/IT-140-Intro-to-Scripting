input_month = str(input())
input_day = int(input())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October","November","December"]
months_31 = ["January", "March", "May", "July", "August", "October", "December"]
months_30 = ["April", "June", "September", "November"]
#set validation criteria to print invalid when certain months are above 30
if input_month not in months or (input_day < 0) or (input_day > 31):
    print("Invalid")
elif input_month not in months_31 and (input_day >= 31):
    print("Invalid")
elif input_month not in months_30 and (input_day >= 30):
    print("Invalid")

else:
#Between March 20 and June 20 is spring
#Between June 21 - Sept 21 is summer
#Between Sept 22 and Dec 20 is Autumn
#Between Dec 21 and Mar 19 is Winter

    if input_month == "March" and input_day >= 20:
            print("Spring")
    elif input_month == "March" and input_day < 20:
            print("Winter")
    elif input_month == "April" or input_month =="May":
            print("Spring")
    elif input_month == "June" and input_day < 20:
            print("Spring")
    elif input_month == "June" and input_day >= 20:
            print("Summer")
    elif input_month == "July" or input_month == "August":
            print("Summer")
    elif input_month == "September" and input_day <= 21:
            print("Summer")
    elif input_month == "September" and input_day > 21:
            print("Autumn")
    elif input_month == "October" or input_month == "November":
            print("Autumn")
    elif input_month == "December" and input_day <= 20:
            print("Autumn")
    elif input_month == "December" and input_day > 20:
            print("Winter")
    elif input_month == "January" or "February":
            print("Winter")

print(input_month, input_day)

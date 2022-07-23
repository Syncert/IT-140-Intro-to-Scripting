# Get users year of birth using input of name and year
# current year
from datetime import date
current_year = date.today().year
user_name = str(input( "What is your name?\n" ))
user_age = int(input( "How old are you?\n" ))
user_year_birth = current_year - user_age
print("Hello {}! You were born in {}.".format(user_name, user_year_birth))
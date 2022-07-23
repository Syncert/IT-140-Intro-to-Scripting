user_age = int(input())
if user_age <= 18:
   print('18 or less')
else:
   print('Over 18')

   user_tickets = int(input())

if user_tickets < 5 : 
    num_tickets = 1
else: 
    num_tickets = user_tickets

print('Value of num_tickets:', num_tickets)

year = int(input())

if year >= 2101 : 
    print('Distant future')
elif year >= 2001 :
    print('21st century')
elif year >= 1901 : 
    print('20th century')
else: 
    print('Long ago')

    
car_year = int(input())

if car_year <= 1969 :
    print("Few safety features.")
if car_year >= 1970 : 
    print("Probably has seat belts.")
if car_year >= 1990 : 
    print("Probably has antilock brakes.")
if car_year >= 2000 :
    print("Probably has airbags.")


num_cents = int(input())
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')

# is user in highschool

user_grade = int(input())
if 9 <= user_grade <= 12 :
    print('in high school')
else:
    print('not in high school')
#Defining Classes

class PatientData:
    def __init__(self):
        self.height_inches = 0
        self.weight_pounds = 0

patient = PatientData()
print('Patient data (before):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


patient.height_inches = int(input())
patient.weight_pounds = int(input())

print('Patient data (after):', end=' ')
print(patient.height_inches, 'in,', end=' ')
print(patient.weight_pounds, 'lbs')


#example 2 defining class
class InventoryTag:
    def __init__(self):
        self.item_id = 0
        self.quantity_remaining = 0

red_sweater = InventoryTag()
red_sweater.item_id = int(input())
red_sweater.quantity_remaining = int(input())

print("ID:",red_sweater.item_id)
print("Qty:",red_sweater.quantity_remaining)

#calculate pay 


class Employee:
    def __init__(self):
        self.wage = 0
        self.hours_worked = 0

    def calculate_pay(self):
        wage = self.wage
        hours = self.hours_worked
        pay = wage * hours 
        return pay

alice = Employee()
alice.wage = 9.25
alice.hours_worked = 35
print('Alice:\n Net pay: {:.2f}'.format(alice.calculate_pay()))

barbara = Employee()
barbara.wage = 11.50
barbara.hours_worked = 20
print('Barbara:\n Net pay: {:.2f}'.format(barbara.calculate_pay()))

#person-info class

class PersonInfo:
    def __init__(self):
        self.num_kids = 0

    # FIXME: Write inc_num_kids(self)

    def inc_num_kids(self):
        self.num_kids = self.num_kids + 1
        return self.num_kids

person1 = PersonInfo()

print('Kids:', person1.num_kids)
person1.inc_num_kids()
print('New baby, kids now:', person1.num_kids)

#use classes to create airline reservation system

class Seat:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def reserve(self, fn, ln, pd):
        self.first_name = fn
        self.last_name = ln
        self.paid = pd

    def make_empty(self):
        self.first_name = ''
        self.last_name = ''
        self.paid = 0.0

    def is_empty(self):
        return self.first_name == ''

    def print_seat(self):
        print('{} {}, Paid: {:.2f}'.format(self.first_name, self.last_name, self.paid))


def make_seats_empty(seats):
    for s in seats:
        s.make_empty()


def print_seats(seats):
    for s in range(len(seats)):
        print('{}:'.format(s), end=' ')
        seats[s].print_seat()

num_seats = 5

available_seats = []
for i in range(num_seats):
    available_seats.append(Seat())

command = input('Enter command (p/r/q): ')
while command != 'q':
    if command == 'p':  # Print seats
        print_seats(available_seats)
    elif command == 'r':  # Reserve a seat
        seat_num = int(input('Enter seat num:\n'))
        if not available_seats[seat_num].is_empty():
            print('Seat not empty')
        else:
            fname = input('Enter first name:\n')
            lname = input('Enter last name:\n')
            paid = float(input('Enter amount paid:\n'))
            available_seats[seat_num].reserve(fname, lname, paid)
    else:
        print('Invalid command.')

    command = input('Enter command (p/r/q):\n')


#race time class 

class RaceTime:

    def __init__(self, start_hrs, start_mins, end_hrs, end_mins, dist):
        self.start_hrs = start_hrs
        self.start_mins = start_mins
        self.end_hrs = end_hrs
        self.end_mins = end_mins
        self.distance = dist

    def print_time(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        print('Time to complete race: {}:{}'.format(hours, minutes))

    def print_pace(self):
        if self.end_mins >= self.start_mins:
            minutes = self.end_mins - self.start_mins
            hours = self.end_hrs - self.start_hrs
        else:
            minutes = 60 - self.start_mins + self.end_mins
            hours = self.end_hrs - self.start_hrs - 1

        total_minutes = hours*60 + minutes
        print('Avg pace (mins/mile): {:.2f}'.format(total_minutes / self.distance))

distance = 5.0

start_hrs = int(input('Enter starting time hours: '))
start_mins = int(input('Enter starting time minutes: '))
end_hrs = int(input('Enter ending time hours: '))
end_mins = int(input('Enter ending time minutes: '))

race_time = RaceTime(start_hrs, start_mins, end_hrs, end_mins, distance)

race_time.print_time()
race_time.print_pace()

#phone number program

class PhonePlan:

    def __init__(self, num_mins = 0, num_messages = 0):
        self.num_mins = num_mins
        self.num_messages = num_messages

    def print_plan(self):
        print('Mins:', self.num_mins, end=' ')
        print('Messages:', self.num_messages)


my_plan = PhonePlan(int(input()), int(input()))
dads_plan = PhonePlan()
moms_plan = PhonePlan(int(input()))

print('My plan...', end=' ')
my_plan.print_plan()

print('Dad\'s plan...', end=' ')
dads_plan.print_plan()

print('Mom\'s plan...', end= ' ')
moms_plan.print_plan()

#customization of printing class instance
class Car:
    def __init__(self, make, model, year, miles, price):
        self.make = make
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price

    def __str__(self):
        return ('{} {} {}:\n Mileage: {}\n Sticker price: ${}'.format(self.year, self.make, self.model, self.miles, self.price))

cars = []
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

for car in cars:
    print(car)


#Overloading less-than operator of time-class allows comparison

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __str__(self):
        return '{}:{}'.format(self.hours, self.minutes)

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours:
            if self.minutes < other.minutes:
                return True
        return False

num_times = 3
times = []

# Obtain times from user input
for i in range(num_times):
    user_input = input('Enter time (Hrs:Mins): ')
    tokens = user_input.split(':')
    times.append(Time(int(tokens[0]), int(tokens[1])))

min_time = times[0]
for t in times:
    if t < min_time :
        min_time = t

print('\nEarliest time is', min_time)

#comparing quarterback classes

class Quarterback:
    def __init__(self, yrds, tds, cmps, atts, ints, wins):
        self.wins = wins

        # Calculate quarterback passer rating (NCAA)
        self.rating = ((8.4*yrds) + (330*tds) + (100*cmps) - (200 * ints))/atts

    def __le__(self, other):
        if (self.rating <= other.rating) or (self.wins <= other.wins):
            return True
        return False

    def __gt__(self, other):
        if (self.rating > other.rating) or (self.wins > other.wins):
            return True
        return False
        

peyton = Quarterback(yrds=4700, atts=679, cmps=450, tds=33, ints=17, wins=10)
eli = Quarterback(yrds=4002, atts=539, cmps=339, tds=31, ints=25, wins=9)
tom = Quarterback(yrds=4806, tds=50, cmps=398, atts=578, ints=8, wins=16)

if peyton > eli:
    print('Peyton is the better QB')
elif peyton < eli:
    print('Eli is the better QB')

elif tom > peyton:
    print('Tom is the better QB')

elif tom < peyton:
    print('Peyton is the better QB')
else:
    print('It is not clear who the better QB is...')



#Lab car value (classes)
#Complete the Car class by creating an attribute purchase_price (type int) and the method print_info() that outputs the car's information.

class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0
        self.current_value = 0

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)
    
    def print_info(self):
        print('Model Year: {}\n Purchase Price:{}\n Current Value:{}'.format(self.model_year, self.purchase_price, self.current_value))


if __name__ == "__main__":    
    year = int(input()) 
    price = int(input())
    current_year = int(input())
    
    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
    
#Winning Team (classes)
#Complete the team class implementation

class Team:
    def __init__(self):
        self.team_name = 'none'
        self.team_wins = 0
        self.team_losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)

if __name__ == "__main__":
    
    team = Team()
   
    team_name = input()
    team_wins = int(input())
    team_losses = int(input())
    
    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses
    
    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team', team.team_name,'has a winning average!')
    else:
        print('Team', team.team_name, 'has a losing average.')

#hashing example


# FIXME: Import sha224 also
from hashlib import md5, sha1, sha224

text = input("Enter text to hash ('q' to quit): ")

# Add sha224 to prompt
algorithm = input('\nEnter algorithm (md5/sha1): ')
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
elif algorithm == 'sha224':
    output = sha224(text.encode('utf-8'))
else:
    output = 'Invalid algorithm selection'

print('\nHash value:', output.hexdigest())

#Array Operations Program
import numpy as np

array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Some common array operations

print('Adding arrays (array1 + array2)')
print(array1 + array2)

print('\nSubtracting arrays (array1 - array2)')
print(array1 - array2)

print('\nMultiplying arrays (array1 * array2)')
print(array1 * array2)

print('\nMatrix multiply (dot(array1 * array2))')
print(np.dot(array1, array2))

print('\nFinding square root of each element in array1')
print(np.sqrt(array1))

print('\nFinding minimum element in array1')
print(array1.min())

print('\nFinding maximum element in array1')
print(array1.max())
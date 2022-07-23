#print pizza diameter

def print_pizza_area(pizza_diameter):
	   pi_val = 3.14159265
	   pizza_radius = pizza_diameter / 2.0
	   pizza_area = pi_val * pizza_radius * pizza_radius
	   print('{:.1f} inch pizza is {:.3f} inches squared'
	       .format(pizza_diameter, pizza_area))
	
print_pizza_area(12.0)
print_pizza_area(16.0)

def print_pizza_volume(pizza_diameter, pizza_height):
    pi_val = 3.14159265

    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    pizza_volume = pizza_area * pizza_height
    print('{:.1f} x {:.1f} inch pizza is {:.3f} inches cubed.'
        .format(pizza_diameter, pizza_height, pizza_volume))


print_pizza_volume(12.0, 0.3)
print_pizza_volume(12.0, 0.8)
print_pizza_volume(16.0, 0.8)

#output hours as minutes function
def output_minutes_as_hours(orig_minutes):

    hours = orig_minutes / 60
    print(hours)

minutes = float(input())
output_minutes_as_hours(minutes)

#function to print total inches
def print_total_inches(feet, inches):
    total_inches = (feet * 12) + inches
    print( 'Total inches: {}'.format(total_inches))

feet = int(input())
inches = int(input())
print_total_inches(feet, inches)


def print_val(x):
    print(x)

print_val(9.0)

#inches to centimeters
CM_PER_INCH = 2.54
INCHES_PER_FOOT = 12
	
def height_US_to_cm(feet, inches):
	"""Converts height in feet/inches to centimeters"""
	total_inches = feet * INCHES_PER_FOOT + inches
	cm = total_inches * CM_PER_INCH
	return cm		

feet = 6
inches = 4
	
centimeters = height_US_to_cm(feet, inches)
print('Centimeters:', centimeters)

#celsius to fahrenheit 
def c_to_f(temp_c):
    return  (temp_c * 9/5) + 32

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

temp_f = c_to_f(temp_c)

print('Fahrenheit:' , temp_f)

#hierarchal function
def calc_circle_area(circle_diameter):
	pi_val = 3.14159265
	
	circle_radius = circle_diameter / 2.0
	circle_area = pi_val * circle_radius * circle_radius
	return circle_area

def pizza_calories(pizza_diameter):
	calories_per_square_inch = 16.7    # Regular crust pepperoni pizza
	
	total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
	return total_calories


print('12 inch pizza has {:.2f} calories.'.format(pizza_calories(12.0)))
print('14 inch pizza has {:.2f} calories.'.format(pizza_calories(14.0)))


#max sum program

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

max_sum = 0.0

num_a = float(input())
num_b = float(input())
num_y = float(input())
num_z = float(input())

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

print('max_sum is:', max_sum)

#program to calculate pyramid_volume

length = float(input())
width = float(input())
height = float(input())


def pyramid_volume(length,width,height):
    base_area = length * width
    pyramid_volume = base_area * height * 1/3
    return pyramid_volume

print(pyramid_volume(length, width, height))

#use function to find mph_and_minutes_to_mile

def mph_and_minutes_to_miles(miles_per_hour , minutes_traveled):
    hours_traveled = minutes_traveled / 60
    miles_traveled = hours_traveled * miles_per_hour
    return miles_traveled


miles_per_hour = float(input())
minutes_traveled = float(input())

print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))


#printing stubs
def get_user_num():
    print("FIXME: Finish get_user_num()")
    return -1
    

def compute_avg(a, b):
    print("FIXME: Finish compute_avg()")
    return -1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)

#Example: ebay_fee() function
#Note: This section requires knowledge of if-else and loop statements.
#A function's block of statements may include branches, loops, and other statements. The following example uses a function to compute the amount that an online auction/sales website charges a customer who sells an item online.



def ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', ebay_fee(selling_price))


#popcorn time
def print_popcorn_time(bag_ounces): 
    if user_ounces < 3: 
        print( 'Too small')
    elif user_ounces > 10:
        print( 'Too large')
    else:
        seconds = 6 * bag_ounces
        print('{} seconds'.format(seconds))

user_ounces = int(input())
print_popcorn_time(user_ounces)

#loop function shampoo
def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    if num_cycles > 4:
        print('Too many.')
    if num_cycles >= 1 and num_cycles <= 4:
        loop = 1
        while loop <= num_cycles:
            print('{} : Lather and rinse.'.format(loop))
            loop = loop + 1
        print('Done.')

user_cycles = int(input())
shampoo_instructions(user_cycles)

#temp conversion functions
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    
    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = float(input())
print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')

#swap first and last in list


def swap(list):
    first_list = list[0]
    last_list = list[-1]
    list[0] = last_list
    list[-1] = first_list
    return values_list

values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)

#pennies function
def number_of_pennies(dollars=0, pennies=0):
    dollar_pennies = dollars * 100
    total_pennies = dollar_pennies + pennies
    return total_pennies

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only


#function to calculate tip
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

def split_check(bill, people, tax_percentage=0.09, tip_percentage=0.15):
    tax = bill * tax_percentage
    tip = bill * tip_percentage
    total = (bill + tax + tip)/people
    return total
    

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print('Cost per diner:', split_check(bill, people))

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print('Cost per diner:', split_check(bill, people))

#physics define trajectory

import math

def trajectory(t, a, v, g, h): 
    """Calculates new x,y position""" 
    x = v * t * math.cos(a) 
    y = h + v * t * math.sin(a) - 0.5 * g * t * t 
    return (x,y)

def degree_to_radians(degrees): 
    """Converts degrees to radians""" 
    return ((degrees * math.pi) / 180.0)

gravity = 9.81 # Earth gravity (m/s^2) 
time = 1.0 # time (s) 
x_loc = 0 
h = 0 

angle = float(input('Launch angle (deg): ')) 
print(angle) 
angle = degree_to_radians(angle)

velocity = float(input('Launch velocity (m/s): ')) 
print(velocity)

height = float(input('Initial height (m): '))  
y_loc = height 
print(y_loc)

while ( y_loc >= 0.0 ): # While above ground 
    print('Time {:3.0f} x = {:3.0f} y = {:3.0f}'.format(time, x_loc, y_loc)) 
    x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)  
    time += 1.0
 

 #compute gas volume
gas_const = 8.3144621

def compute_gas_volume(gas_pressure, gas_temperature, gas_moles):
    gas_volume = (gas_moles * gas_const * gas_temperature)/gas_pressure
    return gas_volume

gas_pressure = float(input())
gas_moles = float(input())
gas_temperature = float(input())
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')


#swap

def swap_values(user_val1, user_val2):
    temp = user_val1
    user_val1 = user_val2
    user_val2 = temp
    return user_val1, user_val2
    
    
a1 = input()
a2 = input()

output1, output2 = swap_values(a1, a2)
print(str(output1) + " " + str(output2))

#zybooks fuckery
def swap_values(user_val1, user_val2):
    tmp = user_val1
    user_val1 = user_val2
    user_val2 = tmp
    return user_val1, user_val2

if __name__ == '__main__':

    v1, v2 = swap_values(input(),input())
    print("{} {}".format(v1, v2))
#Ancestor loop


year_considered = 2020  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print('Ancestors in {}: {}'.format(year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation


#while loop

user_num = int(input())
while user_num > -1:
  print('Body')
  user_num = int(input())

print('Done.')

#while loop ; taught about infinite loops

user_num = int(input())

while user_num >= 1: 
    print(user_num/2)
    user_num = user_num / 2

    
#find GCD
num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print('GCD is {}'.format(num_a))

# Loop Conversation
'''
Program that has a conversation with the user.
Uses elif branching and a random number to mix up the program's responses.
'''
import random  # Import a library to generate random numbers

print('Tell me something about yourself.')
print('You can type \'Goodbye\' at anytime to quit.\n')

user_text = input()

while user_text != 'Goodbye':
    random_num = random.randint(0, 2)  # Gives a random number between 0 and 2
    if random_num == 0:
        print('\nPlease explain further.\n')
    elif random_num == 1:
        print("\nWhy do you say: '{}'?\n".format(user_text))
    elif random_num == 2:
        print('\nWhat else can you share?\n')
    else:
        print('\nUh-oh, something went wrong. Try again.\n')

    user_text = input()

print('It was nice talking with you. Goodbye.\n')


#auto-bid program
import random
random.seed(5)

keep_going = '-'
next_bid = 0

while keep_going != "n":
   next_bid = next_bid + random.randint(1, 10)
   print('I\'ll bid ${}!'.format(next_bid))
   print('Continue bidding?', end=' ')
   keep_going = input()

num_insects = int(input()) # Must be >= 1

#Given positive integer num_insects, write a while loop that prints that number doubled up to, but without exceeding 100. Follow each number with a space.

while num_insects < 101: 
    print(num_insects, end = " ")
    num_insects = num_insects * 2

'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print('Initial savings of ${}'.format(initial_savings))
print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')


#loop over election years
year = 1792
current_year = 2021

while year < 2021:
    print(year)
    year = year + 4

#Factorial
N = int(input())  # Read user-entered number
total = N
# Initialize the loop variable
i = total - 1
while i >= 1:
    total = total * (i)
    i = i - 1

print(total)

#Write a while loop that prints from 1 to user_num, increasing by 1 each time.
i = 1

user_num = int(input()) # Assume positive

while i <= user_num:
    print (i) 
    i = i + 1

#print stars
num_printed = 0

num_stars = int(input())

while num_printed < num_stars:
    print('*')
    num_printed = num_printed + 1


#print stock prices
# NOTE: The following statement converts the input into a list container
stock_prices = input().split()

for price in stock_prices:
    print('$', price)

#print emails from dictionary
contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

new_contact = input()
new_email = input()
contact_emails[new_contact] = new_email

for email in contact_emails:
    print('{} is {}'.format(contact_emails[email],email))

'''Program that calculates savings and interest'''
#alter range value to change how many years are calculated by label, what years
initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year {}: ${:.2f}'.format(i, savings))
    savings = savings + (savings*interest_rate)

print('\n')
'''Program that calculates savings and interest'''
#Range and formulas updated to output in range of 2 
#compounds at same rate of years in range
initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(0,years,2):
    savings = savings + (savings*interest_rate*i)
    print(' Savings in year {}: ${:.2f}'.format(i, savings))

print('\n')

"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)

'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('{}{}.com'.format(letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)
    for i in range (0,10):
        print('{}{}.com'.format(letter1, i))

#Run the program below and observe the output. Modify the program to print one asterisk per 5 units. So if the user enters 40, print 8 asterisks.
num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num//5):
            print('*', end=' ')
        print('\n')

print('Goodbye.')
 

#input rows columns print rectangle
num_rows = int(input())
num_cols = int(input())
for i in range (num_rows):
    print('*', end = ' ')
    for j in range(num_cols-1):
        print('*', end=' ')
    print()

#Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat

num_rows = int(input())
num_cols = int(input())

first_seat = ord('A')
seat = 1
for i in range(1,num_rows+1):
    for j in range(first_seat, first_seat + num_cols):
        seat = chr (j)
        print(i, end = "")
        print(seat, end = " ")

print()

#program to find exact amount of tacos and empanadas with money

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('${} buys {} empanadas and {} tacos without change.'
        .format(meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')


#empinada program with continue statement
empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('${} buys {} empanadas and {} tacos without change.'
                  .format(meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')
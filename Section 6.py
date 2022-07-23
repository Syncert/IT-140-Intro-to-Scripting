#oldest people list program

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

rank_person = int(input('Enter N (1-5): '))

if rank_person == 1:
    print('The {}st oldest person lived {} years' \
        .format(rank_person, oldest_people[rank_person-1]))
elif rank_person == 2 :
    print('The {}nd oldest person lived {} years' \
        .format(rank_person, oldest_people[rank_person-1]))
elif rank_person == 3 :
    print('The {}rd oldest person lived {} years' \
        .format(rank_person, oldest_people[rank_person-1]))
elif (rank_person == 4) or (rank_person == 5) :
    print('The {}th oldest person lived {} years' \
        .format(rank_person, oldest_people[rank_person-1]))
else:
    print("please submit number between 1-5")


#Rider VIP vs Regular Queue

riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider 
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        name = input('Enter name:').strip().lower().lower()
        print(name)
        line.insert(1,name)
        num_vips = num_vips + 1 

    elif user_input == '3':  # Dispatch ride
        counter = riders_per_ride

        while counter > 0:
            del line[0]
            counter = counter - 1
            

    elif user_input == '4':  # Print riders waiting in line
        print('{} person(s) waiting:'.format(len(line)), line)

    else:
        print('Unknown menu option')

    user_input = input(menu).strip().lower()
    print(user_input)

#Program to determine Basketball stats

#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print("Total Points:{}".format(sum(points)))
# Print Average PPG
print("Total Avg PPG:{:.2f}".format(sum(points)/sum(games_played)))
# Print best scoring years (Ex: 2004/2005)
max_years = "{}/{}".format(points.index(max(points)) + 2003,points.index(max(points)) + 2004)
min_years = "{}/{}".format(points.index(min(points)) + 2003,points.index(min(points)) + 2004)
print("Best scoring year:{}".format(max_years))
# Print worst scoring years (Ex: 2004/2005)
print("Worst scoring year:{}".format(min_years))

#Record user guesses
#Write a loop to populate the list user_guesses with a number of guesses. The variable num_guesses is the number of guesses the user will have, which is read first as an integer. Read each guess (an integer) one at a time using int(input()).

num_guesses = int(input())
print("Input {} numbers".format(num_guesses))
user_guesses = []
counter = 0
while counter < num_guesses:
    guess = int(input())
    user_guesses.append(guess)
    counter += 1

print('user_guesses:', user_guesses)

#Assign sum_extra with the total extra credit received given list test_grades. Full credit is 100, so anything over 100 is extra credit.

#Sample output for the given program with input: '101 83 107 90'

user_input = input()
test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0

for grade in test_grades:
    if grade > 100:
        sum_extra = sum_extra + (grade - 100)

print('Sum extra:', sum_extra)

#Write a loop to print all elements in hourly_temperature. Separate elements with a -> surrounded by spaces.

user_input = input()
hourly_temperature = user_input.split()

for temperature in hourly_temperature:
    print(temperature, end = " ")
    if len(hourly_temperature) > (hourly_temperature.index(temperature) + 1):
        print("-> ", end = "")
        continue
    elif len(hourly_temperature) == (hourly_temperature.index(temperature) + 1):
        print("\n", end = "")
        break


# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,  
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        0
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: {} miles'.format(distances[int(city1)][int(city2)]))


#Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]
#https://www.w3schools.com/python/python_lists_comprehension.asp

mult_table = [[int(num) for num in line.split()] for line in lines]

for list in mult_table:
    for element in list:
        print(element, end = "")
        if len(list) > (list.index(element) + 1):
            print ( " | ", end = "")
        elif len(list) == (list.index(element) + 1):
            print("")


#Iterate over copy of the list

nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('{}: {}'.format(pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('{}: {}'.format(pos, val))
    
# Remove elements from nums1 if also in nums2
print()
for val in nums1[:]:
    if val in nums2[:]:
        print('Deleting {}'.format(val))
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')

#A list can be useful in solving various engineering problems. 
#One problem is computing the voltage drop across a series of resistors. 
# If the total voltage across the resistors is V, then the current through 
# the resistors will be I = V/R, where R is the sum of the resistances. 
# The voltage drop Vx across resistor x is then Vx = I · Rx.
#calculating voltage drop per resistor
#R = Ohms
num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print ("Input voltage applied to circuit:{}".format(input_voltage))

print('Input ohms of {} resistors'.format(num_resistors))
for i in range(num_resistors):
    res = float(input('{})'.format(i + 1)))
    print("{}) {}".format((i+1),res))
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
print("Voltage Drop per resistor is")
counter = 1
for i in resistors:
    vol_drop = current * i
    print("{}) {:.1f}V".format(counter,vol_drop))
    counter = counter + 1
    voltage_drop.append(vol_drop)
# Print the voltage drop per resistor
# ...

#matrix calculations given two-dimensional lists

m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('{}'.format(m3[i][j]), end=' ')
    print()  # Print single newline


#Statistics are often calculated with varying amounts of input 
# data. Write a program that takes any number of integers as 
# input, and outputs the average and max.

print("Please input any string of numbers separated by a space")
num_input = input()
num_list = [int(i) for i in num_input.split()]
print("{} {}".format(round(sum(num_list)/len(num_list)), max(num_list)))

#Write a program that gets a list of integers from input, and 
# outputs non-negative integers in ascending order 
# (lowest to highest).
print("Please input any string of numbers separated by a space")
num_input = input()
num_list = [int(i) for i in num_input.split()]
pos_num_list = [i for i in num_list if i >= 0]
pos_num_list.sort()
for num in pos_num_list:
    print(num, end = " ")


#gradebook
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        # ...
    elif command == '2':
        # ...
    elif command == '3':
        # ...
    elif command == '4':
        break
    else:
        print('Unrecognized command.')

#Complete program later
#Write a program that uses the keys(), values(), 
# and/or items() dict methods to find statistics about the 
# student_grades dictionary. Find the following:

# Print the name and grade percentage of the student with the highest total of points.
# Find the average score of each assignment.
# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.


# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

#iterate over dictionary of countries and populations
#Sample output with input:
# 'China:1365830000,India:1247220000,United States:318463000,Indonesia:252164800':
user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }

for country,pop in country_pop.items():
    print(country, 'has', pop, 'people.')


#nested dictionary, storing grades

grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework {}: {}'.format(hw, score))

        print('Midterm: {}'.format(midterm))
        print('Final: {}'.format(final))

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))

    user_input = input('Enter student name: ')


#The following program uses nested dictionaries to store a 
# small music library. Extend the program such that a user can 
# add artists, albums, and songs to the library. First, 
# add a command that adds an artist name to the music dictionary.
# en add commands for adding albums and songs. Take care to 
# check that an artist exists in the dictionary before adding 
# an album, and that an album exists before adding a song.

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}


#Write a program that reads a list of words. Then, the program 
# outputs those words and their frequencies.

word_list = input().split()

for word in word_list: 
    word_count = word_list.count(word)
    print(word, word_count)

#replace words in statement

#automobile car   manufacturer maker   children kids
#The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.

#make empty replacement pairs dict

#gather replacement pairs
replacement_pairs = input('Please enter pairs of words to be replaced in statement')
#split into list
replace_list = replacement_pairs.split()

#make empty replacement pairs dict
repl = {}

for i in range(0,len(replace_list),2):
    repl[replace_list[i]] = replace_list[i+1]



#sentence = input()

sentence = input('Please enter sentence or statement for replacement')

for key in repl:
    sentence = sentence.replace(key, repl[key])

print(sentence)
# echoes contents of logs stored in hierarchal directory structure

import os
import datetime

curr_day = datetime.date(1997, 8, 29)

num_days = 30
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    # Build path string using current OS path separator
    file_path = os.path.join('logs', year, month, day, 'log.txt')

    f = open(file_path, 'r')
    print('{}: {}'.format(file_path, f.read()))
    f.close()

    curr_day = curr_day + datetime.timedelta(days=1)

#splits path into 2 tuple head/tail
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(os.path.split(p))

#returs true if path to existing file
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
if os.path.exists(p):
    print('Suit up...')
else:
    print('The Lamborghini then?')

#returns size in bytes of the path
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print('Size of file:', os.path.getsize(p), 'bytes')


#directory tree
import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)

#print bytes literal
my_bytes = b'This is a bytes literal'

print(my_bytes)
print(type(my_bytes))

#bytes example
print(b'123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39')

#inspecting binary comments of an image file

f = open('ball.bmp', 'rb')  # Open in binary mode using 'b'

# Read image binary data
contents = f.read()

print('Contents of ball.bmp:\n')
print(contents)

f.close()

#alter ball image
import struct

ball_file = open('ball.bmp', 'rb')
ball_data = ball_file.read()
ball_file.close()

# BMP image file format stores location
# of pixel RGB values in bytes 10-14
pixel_data_loc = ball_data[10:14]

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]

# Create sequence of 3000 red, green, and yellow pixels each
new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000

# Overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
              new_pixels + \
              ball_data[pixel_data_loc + len(new_pixels):]

# Write new image
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()

#Packing values into byte sequences

import struct

print('Result of packing 5:', end=' ')
print(struct.pack('>h', 5))

print('Result of packing 256:', end=' ')
print(struct.pack('>h', 256))

print('Result of packing 5 and 256:', end=' ')
print(struct.pack('>hh', 5, 256))

#unpacking values from byte sequence
import struct

print('Result of unpacking {}:'.format(repr('\x00\x05')), end=' ')
print(struct.unpack('>h', b'\x00\x05'))


print('Result of unpacking {}:'.format(repr('\x01\x00')), end=' ')
print(struct.unpack('>h', b'\x01\x00'))

print('Result of unpacking {}:'.format(repr('\x00\x05\x01\x00')), end=' ')
print(struct.unpack('>hh', b'\x00\x05\x01\x00'))

#use command line sequences to specify name of input file
import sys
import os

if len(sys.argv) != 2:
    print('Usage: {} input_file'.format(sys.argv[0]))
    sys.exit(1)  # 1 indicates error

print('Opening file {}.'.format(sys.argv[1]))

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())

print('Closing file {}'.format(sys.argv[1]))
f.close()  # Done with the file, so close it

print('\nnum1: {}'.format(num1))
print('num2: {}'.format(num2))
print('num1 + num2: {}'.format(num1 + num2))


#with statement to open files

print('Opening myfile.txt')

# Open a file for reading and appending
with open('myfile.txt', 'r+') as f:
    # Read in two integers
    num1 = int(f.readline())
    num2 = int(f.readline())

    product = num1 * num2

    # Write back result on own line
    f.write('\n')
    f.write(str(product))

# No need to call f.close() - f closed automatically 
print('Closed myfile.txt')


#reading each row of csv

import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    row_num = 1
    for row in grades_reader:
        print('Row #{}:'.format(row_num), row)
        row_num += 1


#calculations using csv file

import csv

# Dictionary that maps student names to a list of scores
grades = {}

# Use with statement to guarantee file closure
with open('grades.csv', 'rb') as csvfile:
    grades_reader = csv.reader(csvfile, delimiter=',')

    first_row = True
    for row in grades_reader:
        # Skip the first row with column names
        if first_row:
            first_row = False
            continue

        ## Calculate final student grade ##

        name = row[0]

        # Convert score strings into floats
        scores = [float(cell) for cell in row[1:]]

        hw1_weighted = scores[0]/10 * 0.05
        hw2_weighted = scores[1]/10 * 0.05
        mid_weighted = scores[2]/100 * 0.40
        fin_weighted = scores[3]/100 * 0.50

        grades[name] = (hw1_weighted + hw2_weighted + 
                        mid_weighted + fin_weighted) * 100

for student, score in grades.items():
    print ('%s earned %.1f%%' %).format(student, score))

#Lab 7.8
# Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. 
# The file contains a list of words separated by commas. 
# Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

#nailed it!
import csv

filename = 'input1.csv' #input()

name_dict = {}

with open(filename, "r") as csvfile:
    names = csvfile.readline().strip().split(",")
 
    for name in names:
        name_counter = 0
        for inner in names:
            if name.strip() == inner.strip():
                name_counter = name_counter + 1
        #add to dictionary with name: and count
        name_dict.update(dict({name : name_counter}))

for name, counter in name_dict.items():
    print(name.strip(), counter)



#Lab 7.9
#Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. 
# The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put 
# the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the 
# values (since multiple shows could have the same number of seasons).

#Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.
filename = "file1.txt" #input()
#Open and Read the file

contents = ""
with open(filename , "r") as file:
    contents = file.readlines()

#print(contents)

#Put file contents into a dictionary
data_dict = {}
sorted_values = []
for counter in range(0, len(contents), 2):
    key = int(contents[counter].strip("\n"))
    value = contents[counter+1].strip("\n")
    if key not in data_dict:
        data_dict[key] = value
        sorted_values.append(value)
    else:
        val = data_dict[key]
        data_dict[key] = val + '; ' + value
        sorted_values.append(value)

sorted_values.sort()
# print(sorted_values)
# print(data_dict)
#Sort by key -- number
# print(dict)
sorted_keys = sorted(data_dict)

# print(sorted_keys)

with open("output_keys.txt", "w") as out1:
    for key in sorted_keys:
        out1.write('{}: {}\n'.format(key, data_dict[key]))


#sort by title
# sorted_values = sorted(data_dict.items(), key = lambda item: item[1])
# sorted_values = []
# for titles in data_dict.values():
#     sorted_values.append(titles)

sorted_values.sort()
# print(sorted_values)

with open("output_titles.txt","w") as out2:
    for titles in sorted_values:
        out2.write('{}'.format(titles))
        out2.write("\n")
#write the sorted data to output_value.txt
# Complete the following program

num_in_tens = int(input('Enter the tens digit:\n'))
num_in_ones = int(input('Enter the ones digit:\n'))

num_in = num_in_tens*10 + num_in_ones

print('You entered', num_in)
print(num_in, '* 11 is', num_in*11)

num_out_hundreds = str(num_in_tens + ((num_in_tens + num_in_ones) // 10))
num_out_tens = str((num_in_ones+num_in_tens)%10)
num_out_ones = str(num_in_ones)

print('An easy mental way to find the answer is:')
print(num_in_tens, ',', num_in_tens, '+', num_in_ones, ',', num_in_ones)

#Build num_out from its digits:
num_out = num_out_hundreds + num_out_tens + num_out_ones

# Note this line will generate an error until the above program is complete.
print(num_out)

### Divide by X
user_num = int(input())
x = int(input())

output_1 = int(user_num/x)
output_2 = int(user_num/x/x)
output_3 = int(user_num/x/x/x)

print(output_1, output_2, output_3)

## Calculate Calories
#script to calculate calories
user_age = int(input())
user_weight = int(input())
user_heart_rate = int(input())
user_time_exercised = int(input())

caloric_expenditure = (((user_age * 0.2757)) + (user_weight * 0.03295) + (user_heart_rate * 1.0781) - 75.4991) * user_time_exercised / 8.368

print('Calories: {:.2f} calories'.format(caloric_expenditure))

#savings
import math

base = float(input('Enter initial savings: '))
print(base)

rate = float(input('Enter annual interest % rate: '))
print(rate)

years = int(input('Enter years that pass: '))
print(years)

total = base * math.pow(1 + (rate / 100), years)

print ('Savings after', years, 'years is', total) 

#find smallest number in list of 3 ; solution 1
num_1 = int(input('Input any number:'))
num_2 = int(input('Input another number:'))
num_3 = int(input('Input one more number:'))

my_numbers = [num_1, num_2, num_3]

print(min(my_numbers))


#find smallest number in list of 3 ; solution 2
a = int(input("input an integer:"))
b = int(input("input another integer:"))
c = int(input("one more integer:"))

#looking for minimum

if a < b and a < c:
    print(a)

elif  b < a and b < c:
    print(b)

else: 
    print(c)


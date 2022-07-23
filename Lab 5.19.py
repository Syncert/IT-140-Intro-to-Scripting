#define a function where you can determine the exact change
#of a input change amount
#then call function

def exact_change(user_total):
    if user_total <= 0:
        print("no change")

    num_dollars = user_total // 100
    if num_dollars == 1:
        print("{} dollar".format(num_dollars))
    if num_dollars > 1:
        print("{} dollars".format(num_dollars))
    user_total = user_total - (num_dollars*100)

    num_quarters = user_total // 25
    if num_quarters == 1:
        print("{} quarter".format(num_quarters))
    if num_quarters > 1:
        print("{} quarters".format(num_quarters))    
    user_total = user_total - (num_quarters*25)

    num_dimes = user_total // 10
    if num_dimes == 1:
        print("{} dime".format(num_dimes))
    if num_dimes > 1:
        print("{} dimes".format(num_dimes))
    user_total = user_total - (num_dimes*10)

    num_nickels = user_total // 5
    if num_nickels == 1:
        print("{} nickel".format(num_nickels))
    if num_nickels >1:
        print("{} nickels".format(num_nickels))
    user_total = user_total - (num_nickels*5)

    num_pennies = user_total // 1
    if num_pennies == 1:
        print("{} penny".format(num_pennies))
    if num_pennies > 1:
        print("{} pennies".format(num_pennies))
    user_total = user_total - (num_pennies*1)
    
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies




    
if __name__ == '__main__':
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

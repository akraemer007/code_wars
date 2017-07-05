# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
#
# For example:
#
#  persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
#                        # and 4 has only one digit.
#
#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
#                        # 1*2*6 = 12, and finally 1*2 = 2.
#
#  persistence(4) => 0   # Because 4 is already a one-digit number.
#  persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
#                  # and 4 has only one digit

def persistence(n):
    loop_count = 0           # keeps tracks of how many time I need to run the loop below

    while len(str(n)) > 1:   # checks to see if loop should run
        loop_count += 1      # At the start of each loop, adds one to the counter
        product_total = 1    # resets the total within the loop
        for x in str(n):
            product_total = product_total * int(x)
        n = product_total    # updates the total so the loop can start again.

    return loop_count

persistence(39)
persistence(999)
persistence(4)

# this was kind of a weird one. Didn't love any of the responses online.

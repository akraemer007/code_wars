# Write a function that takes an (unsigned) integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def countBits(n):
    return format(n, 'b').__str__().count('1') # format turns into binary. Need to learn what __ means

countBits(1234)

# In the following 6 digit number:
#
# 283910
# 91 is the greatest sequence of 2 digits.
#
# Complete the solution so that it returns the largest five digit number found within the number given.. The number will be passed in as a string of only digits. It should return a five digit integer. The number passed may be as large as 1000 digits.


def solution(digits):
    slice_list = []           # empty list to keep ints

    start = -1                # establish a start number. Chose -1 since first will bring it to 0
    for x in str(digits):     # create list of 5 int numbers
        start += 1
        end = start + 5
        slice_list.append(str(digits)[start:end])

    largest = 0               # this for loop identifieds the largest
    for x in slice_list:
        if int(x) > largest:
            largest = int(x)
    return largest
solution(283910123)

# This one was fun for a couple reasons:
# 1. This one I learned that you can't loop over ints.
# 2. it strengthened my understanding of append.
# 3. It is my first assessment that has multiple different for loops.
# 4. I worked on working with ranges

# I'm happy with my overall progresss. I think I really get these string manipulations now.
# My brain has changed to raw for loop thinking rather than apply() which is so easy.

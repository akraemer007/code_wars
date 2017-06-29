# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    below_number = range(1, number)

    div_3 = [x for x in below_number if x%3==0] # keep div by 3
    div_5 = [x for x in below_number if x%5==0] # keep div by 5
    div_5 = [x for x in div_5 if x%3!=0]

    return sum(div_3) + sum(div_5)

# solution(10)

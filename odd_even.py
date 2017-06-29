# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N.
# Write a method that takes the array as an argument and returns N.

# For example:
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160

def find_outlier(integers):
  div_2_remain = [x % 2 for x in integers] # two things here: wrapping in [] outputs a list. Also, it's interesting that the for is formatted differently when on one line

  even_odd = []   # create placeholder list
  even_count = 0  # create placeholder variable

  # figure out if it's an even or odd and make a list that ids even or odd better.
  for x in div_2_remain:
    if x == 0:
        even_odd.append(0)
        even_count += 1
    else:
        even_odd.append(1)
        even_count += 0

  # checks:
  # print even_count
  # print even_odd

  # based on whether or not it's even or odd, it will index the number I flagged.
  if even_count > 1:
      position = even_odd.index(1)
      return integers[position]
  else:
      position = even_odd.index(0)
      return integers[position]

# find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])

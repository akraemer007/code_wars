# ###Lyrics... Pyramids are amazing! Both in architectural and mathematical sense. If you have a computer, you can mess with pyramids even if you are not in Egypt at the time. For example, let's consider the following problem. Imagine that you have a plane pyramid built of numbers, like this one here:
#
#    /3/
#   \7\ 4
#  2 \4\ 6
# 8 5 \9\ 3
# Here comes the task...
#
# Let's say that the 'slide down' is a sum of consecutive numbers from the top to the bottom of the pyramid. As you can see, the longest 'slide down' is 3 + 7 + 4 + 9 = 23
#
# Your task is to write a function longestSlideDown (in ruby: longest_slide_down) that takes a pyramid representation as argument and returns its' longest 'slide down'. For example,

# def longestSlideDown(pyramid):
#     sum_list_old = pyramid[0]
#     level = 1
#     summing = []
#     index = 0
#     for x in pyramid[1:]: # layer of pyramid
#         for i in x:
#
#             summing = [i + ]
#
#             index += 1


# I am sooooo stuck!

def longestSlideDown(pyramid):
    reverse_pyramid = pyramid[::-1]
    previous_step = reverse_pyramid[0]

    # for x in reverse_pyramid[1:]:
    x = [2,4,6]

        # for i in x:

    i = 2



longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])
# print(23)

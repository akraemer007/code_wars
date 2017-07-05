# Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.
#
# Examples:
# validParentheses( "()" ) => returns true
# validParentheses( ")(()))" ) => returns false
# validParentheses( "(" ) => returns false
# validParentheses( "(())((()())())" ) => returns true
#
# All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'

def valid_parentheses(string):

    str_list_first = list(string)
    output = True
    str_list = []
    for x in str_list_first:
        if x == '(' or x == ')':
            str_list.append(x)
    while True:
        if len(str_list) == 0:
            output = True
            break
        elif len(str_list) == 1:
            output = False
            break
        if str_list.count(')') > 0:
            right_index = str_list.index(')')
            if 0 < right_index:
                if str_list[right_index - 1] == '(':
                    del str_list[right_index]
                    del str_list[right_index - 1]
                else:
                    output = False
                    break
            else:
                output = False
                break
        else:
            output = False
            break
    print(output)
    return output

valid_parentheses( "()" )
valid_parentheses( ")(()))" )
valid_parentheses( "(" )
valid_parentheses( "(())((()())())" )
valid_parentheses("hi(hi)()")

# I didn't love this one since the tests didn't match the descripton.
# I know that I did this one terribly. It's an if / else monstrocity. I didn't know a better way of doing this though. I'm glad it worked :D

# a lot of other people used a counter, which is quite clever. A '(' is worth 1 and a ')' is worth -1. If the amnt goes below 0 then the loop stops and says fail. If it ends and it's above 0 it fails. It needs to end on zero. Quite clever.

# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized.
#
# Examples:
#
# # returns "theStealthWarrior"
# to_camel_case("the-stealth-warrior")
#
# # returns "TheStealthWarrior"
# to_camel_case("The_Stealth_Warrior")

def to_camel_case(text):
    text = list(text)
    new_text = []
    position = 0
    for x in text:
        if x == '-' or x == '_':
            text[position + 1] = text[position + 1].upper()
        else:
            new_text.append(x)
        position += 1
    return ''.join(new_text)

to_camel_case("the-stealth-warrior")
to_camel_case("The_Stealth_Warrior")

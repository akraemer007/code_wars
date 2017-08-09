# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.
#
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#
# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.
#
# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"


def order(sentence):
    d = {
    '1' : '',
    '2' : '',
    '3' : '',
    '4' : '',
    '5' : '',
    '6' : '',
    '7' : '',
    '8' : '',
    '9' : ''
    }

    word_list = sentence.split(' ')
    wl_len = len(word_list)

    for i in word_list:
        if '1' in i:
            d['1'] = i
        elif '2' in i:
            d['2'] = i
        elif '3' in i:
            d['3'] = i
        elif '4' in i:
            d['4'] = i
        elif '5' in i:
            d['5'] = i
        elif '6' in i:
            d['6'] = i
        elif '7' in i:
            d['7'] = i
        elif '8' in i:
            d['8'] = i
        elif '9' in i:
            d['9'] = i

    if wl_len == 1:
        return d['1']
    elif wl_len == 2:
        return d['1'] + ' ' + d['2']
    elif wl_len == 3:
        return d['1'] + ' ' + d['2'] + ' ' + d['3']
    elif wl_len == 4:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4']
    elif wl_len == 5:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4'] + ' ' + d['5']
    elif wl_len == 6:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4'] + ' ' + d['5'] + ' ' + d['6']
    elif wl_len == 7:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4'] + ' ' + d['5'] + ' ' + d['6'] + ' ' + d['7']
    elif wl_len == 8:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4'] + ' ' + d['5'] + ' ' + d['6'] + ' ' + d['7'] + ' ' + d['8']
    elif wl_len == 9:
        return d['1'] + ' ' + d['2'] + ' ' + d['3'] + ' ' + d['4'] + ' ' + d['5'] + ' ' + d['6'] + ' ' + d['7'] + ' ' + d['8'] + ' ' + d['9']

order("is2 Thi1s T4est 3a")

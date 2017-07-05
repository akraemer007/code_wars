# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
#
#
# Examples:
#
# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    # break words out
    # identify which words are 5 or more
    # reverse 5 or more lettered words
    # put it all together


    words = sentence.split(' ') # I learned that split auto gives me my words in a string. Nice feature. Don't need to specifiy ' '.

    words_jumble = []
    for x in words:
        if len(x) >= 5:
            words_jumble.append(x[::-1]) # reverses the string x[start:end:step]
        else:
            words_jumble.append(x)

    return ' '.join(words_jumble) # Join is the opposite of split. Working it on a space string adds spaces between.

spin_words("Hey fellow warriors")

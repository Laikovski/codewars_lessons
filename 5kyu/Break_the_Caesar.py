# Break the Caesar!
# The Caesar cipher is a notorious (and notoriously simple) algorithm for encrypting a message: each letter is shifted a certain constant number of places in the alphabet. For example, applying a shift of 5 to the string "Hello, world!" yields "Mjqqt, btwqi!", which is jibberish.
#
# In this kata, your task is to decrypt Caesar-encrypted messages using nothing but your wits, your computer, and a set of the 1000 (plus a few) most common words in English in lowercase (made available to you as a preloaded variable named WORDS, which you may use in your code as if you had defined it yourself).
# Given a message, your function must return the most likely shift value as an integer.
#
# A few hints:
#
#     Be wary of punctuation
#     Shift values may not be higher than 25
# NOT READY!!! NOT WORK!!!


alpha = 'abcdefghijklmnopqrstuvwxyz'
original = list(alpha)
shift_list = list(alpha)
WORD = {'hello', 'word'}
step = 1

def break_caesar(message):
    def shift(step):
        shift_list = list(alpha)
        for i in range(step):
            shift_list.append(shift_list.pop(0))
        print(shift_list)
        print(original)
        return shift_list
    global step
    shift_list = shift(step)
    while True:
        temp = message.split(' ')
        temp = temp[0].strip('.?!:,').lower()
        print(temp)
        result_word = ''
        for item in temp:
            print(item)
            index = shift_list.index(item)
            result_word += original[index]
        print(result_word)
        if result_word in WORD:
            print('work')
            return 'work'
        else:
            step += 1
            shift(step)


break_caesar('Mjqqt, btwqi!')



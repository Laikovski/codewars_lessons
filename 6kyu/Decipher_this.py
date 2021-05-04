# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:
#
# For each word:
#
#     the second and the last letter is switched (e.g. Hello becomes Holle)
#     the first letter is replaced by its character code (e.g. H becomes 72)
#
# Note: there are no special characters used, only letters and spaces
#
# Examples
#
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'
import re
def decipher_this(string):
    res = ''
    my_list = string.split(' ')
    for i in my_list:
        k = re.split('(\d+)', i)
        k[1] = chr(int(k[1]))
        if k[2] == '':
            res += k[2]
        else:
            temp = list(k[2])
            temp[0], temp[-1] = temp[-1], temp[0]
            s = ''.join(temp)
            k[2] = s
        res += ''.join(k) + ' '
    return res.rstrip(' ')
decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")

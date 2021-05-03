# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
#
# solution("camelCasing")  ==  "camel Casing"
#


def solution(s):
    new = ''
    for i in s:
        if i == i.upper():
            new += ' ' + i
        else:
            new += i

    return new


solution("breakCamelCase")
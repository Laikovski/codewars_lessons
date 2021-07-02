"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""

def to_camel_case(text):
    str = text.title()
    word = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
    ans=''
    for j,i in enumerate(str):
        if j == 0:
            ans =ans + text[0]
        else:
            if i in word:
                ans = ans + i
    return ans

to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case('The-Stealth-Warrior')
to_camel_case("A-B-C")
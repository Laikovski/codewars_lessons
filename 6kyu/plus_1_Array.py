# Given an array of integers of any length, return an array that has 1 added to the value represented by the array.
#
#     the array can't be empty
#     only non-negative, single digit integers are allowed
#
# Return nil (or your language's equivalent) for invalid inputs.
# Examples
#
# For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].
#
# [4, 3, 2, 5] would return [4, 3, 2, 6]

def up_array(arr):
    strings = ''
    for integer in arr:
        if integer < 0:
            return None
        else:
            strings += str(integer)

    a_string = "".join(strings)
    print(f'1{a_string}1')
    ints = int(a_string) + 1
    to_string = str(ints)

    print([int(x) for x in to_string])
    # return [int(x) for x in to_string]

up_array([4, 3, 2, 5])




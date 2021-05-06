# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.
# Examples
#
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

def highest_rank(arr):
    new_dict = {num : arr.count(num) for num in arr}
    new_dict = (sorted(new_dict.items(), key=lambda item: item[0]))
    new_dict = (sorted(new_dict, key=lambda item: item[1]))
    print(new_dict[-1][0])
highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10])
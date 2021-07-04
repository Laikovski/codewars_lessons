"""This Kata is intended as a small challenge for my students
All Star Code Challenge #19
You work for an ad agency and your boss, Bob, loves a catchy slogan. He's always jumbling together "buzz" words until
he gets one he likes. You're looking to impress Boss Bob with a function that can do his job for him.
Create a function called sloganMaker() that accepts an array of string "buzz" words. The function returns an array of
all possible UNIQUE string permutations of the buzz words (concatonated and separated by spaces).

Your boss is not very bright, so anticipate him using the same "buzz" word more than once, by accident.
The function should ignore these duplicate string inputs."""


def slogan_maker(array):
    from itertools import permutations
    array = remove_duplicate(array)
    return [' '.join(element) for element in list(permutations(array, len(array)))]


def remove_duplicate(old_list):
    final_list = []
    for num in old_list:
        if num not in final_list:
            final_list.append(num)
    return final_list

slogan_maker(["super"])
slogan_maker(["super", "hot"])
slogan_maker(["super", "guacamole", "super", "super", "hot", "guacamole"])
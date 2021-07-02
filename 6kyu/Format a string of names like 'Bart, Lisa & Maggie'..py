"""
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''

"""
def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]["name"]
    elif len(names) >= 2:
        res = ''
        for item in names:
            if names.index(item) == len(names) - 2:
                res += f'{item["name"]} & '
            else:
                res += f'{item["name"]}, '
        return res.rstrip(', ')

namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]),
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
namelist([])


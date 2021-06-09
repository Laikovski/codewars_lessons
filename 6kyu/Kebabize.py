# Modify the kebabize function so that it converts a camel case string into a kebab case.
#
# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps
#
# Notes:
#
#     the returned string should only contain lowercase letters


import re
def kebabize(string):
    one = '-'.join([s for s in re.split("([A-Z][^A-Z]*)", string) if s]).lower()
    res = re.sub('[0|1|2|3|4|5|6|7|8|9]','', one).strip('-')
    print(res)

kebabize('myCame4lCase3dString')
kebabize('SOS')
kebabize('my-ca3mel-has3-humps')
kebabize('27JjToUJvW4hQbVzTBTt763mfAoHQcWpKhQkLEi')

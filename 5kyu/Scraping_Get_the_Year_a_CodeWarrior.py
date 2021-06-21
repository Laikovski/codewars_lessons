# #Task: Write a function get_member_since which accepts a username from someone at Codewars and returns an string containing the month and year separated by a space that they joined CodeWars.
#
# ###If you want/don't want your username to be in the tests, ask me in the discourse area. There can't be too many though because the server may time out.
#
# #Example:
#
# >>> get_member_since('dpleshkov')
# Jul 2016
# >>> get_member_since('jhoffner')
# Oct 2012
#
# #Libraries/Recommendations:
#
# ##Python:
#
#     urllib.request.urlopen: Opens up a webpage.
#     re: The RegEx library for Python.
#     bs4(BeautifulSoup): A tool for scraping HTML and XML.
#     Python 2 is not working for this kata. :(


from urllib.request import urlopen
import re

def get_member_since(username):
    url = f'https://www.codewars.com/users/{username}'
    html = str(urlopen(url).read())
    date = re.search('Member Since:</b>(.*?)</div>', html)
    return date.group(1) if date else None
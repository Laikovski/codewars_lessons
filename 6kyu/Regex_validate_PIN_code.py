# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
# Examples
#
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# first
import re
def validate_pin(pin):
    r = re.fullmatch('^([\d]{4})$|^([\d]{6})$', pin)
    return True if r else False

# second
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


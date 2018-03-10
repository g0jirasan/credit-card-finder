import re
import sys

def check_sum(numeric_string, includes_check_digit=False):
    if not includes_check_digit:
        numeric_string += '0'
    EVEN_VALUES = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
    evens = numeric_string[:-1][::-2]
    odds = numeric_string[::-2]
    return sum(int(i) for i in odds) + sum(EVEN_VALUES[int(i)] for i in evens)

def find_check_digit(numeric_string):
    return 9 * check_sum(numeric_string) % 10

def check_luhn(candidate):
    return candidate.isdigit() and check_sum(candidate, True) % 10 == 0

def check_regex(candidate):
    PATTERN = re.compile(r'(4(?:\d{12}|\d{15})'      # Visa
                         r'|5[1-5]\d{14}'            # Mastercard
                         r')$')
    return bool(PATTERN.match(candidate))

def is_valid_cc(candidate):
    return check_regex(candidate) and check_luhn(candidate)

if len (sys.argv) < 2:
	print "Please specify file."
	sys.exit(0)


position = 0
input_file = sys.argv[1]
fp = open(input_file, "rb")

while True:
	fp.seek(position)
	byte = fp.read(16)
     	position = position + 1
    	result = is_valid_cc(byte)
        if result == 1:
    		print "Found Valid Card #: " + byte
    	if byte == '':
    		break
       

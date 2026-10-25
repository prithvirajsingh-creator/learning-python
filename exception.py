# getting cleaner error
import sys

try:
    x= int(input('X: '))
    y= int(input('Y: '))
except ValueError:
    print('Error : you cannot enter a string value.')
    sys.exit(1)
# zero divission error
try:
    result = x/y
except ZeroDivisionError:
    print('Error : cannot be devided by 0.')
    sys.exit(1)
    
print(f'{x} / {y} = {result}')
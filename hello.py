name = str(input('what is your name :'))
#using formatted string (f-string) to use variables effectively in a string
print(f'hello {name}')

#using conditional statements with input
n= int(input('enter a number :'))

if n<0:
    print('The given number is negative')
    
elif n>0:
    print('The given number is positive')
    
else:
    print('The given number is zero')
    
#sequence 

name = 'Prithvi'
print(name[1])

# list
name = ['aman','dbs','akshat']
print(name[1])

#tuple ----- used to store multiple values which are immutable
name = ('aman','dbs','akshat')
print(name[1])

# set ----- used to store multiple values which are unique and unordered
set = set()
set.add(1)
set.add(2)
set.add(3)
print(set)
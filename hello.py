name = str(input('what is your name :'))
#using formatted string (f-string) to use variables effectively in a string
print(f'hello {name}')

#using conditional statements with inout
n= int(input('enter a number :'))

if n<0:
    print('The given number is negative')
    
elif n>0:
    print('The given number is positive')
    
else:
    print('The given number is zero')
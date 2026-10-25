people = [
    {'name':'Harry', 'house':'Gryffindor'},
    {'name':'Cho' , 'house': 'Ravenclaw'},
    {'name':'Draco' , 'house': 'Slytherin'}
     
]
#sorting on basis of alphabatical manner of name
def f(person):
    return person['name']

people.sort(key=f)

print(people)

#sorting on the basis of alphabetical manner of house

def f(person):
    return person['house']

people.sort(key=f)

print (people)
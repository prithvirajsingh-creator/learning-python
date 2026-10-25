# decorator is a tool which takes and modifies any function

#this is an example of decoraator function
def announce(f):
    def wrapper():
        print('about to run the function...')
        f()
        print('done with the function.')
    return wrapper
#adding decorator
@announce # we use @ to add any decorator
def hello():
    print('Hello World !!!')
    
hello()
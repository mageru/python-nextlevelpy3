def printlog(func):
    def wrapper(arg):
        print('CALLING: {}'.format(func.__name__))
        return func(arg)
    return wrapper

@printlog
def f(n):
    return n+2

print(f(3))

# support multiple arguments
def audit_to_txt(func):
    def wrapper(*arg):
        print('INSTANTIATED FUNCTION: {}'.format(func.__name__))
        return func(*arg)
    return wrapper

@audit_to_txt
def test(n,y):
    return n+y

print(test(5,2))
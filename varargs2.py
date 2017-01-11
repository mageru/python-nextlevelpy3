def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))

print_all("dog","cat")
print_all("cat","dog")
print_all()
print_all(x=7, z=3)
print_all(z=3, x=7)
print_all("red","green", x=7, z=3)
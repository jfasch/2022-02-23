import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper called, func:', func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper

class debug_p:
    def __init__(self, msg):
        self.msg = msg
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(self.msg + ' wrapper called, func:', func.__name__, args, kwargs)
            return func(*args, **kwargs)
        return wrapper

@debug
def add(l,r):
    return l+r

@debug
def sub(l,r):
    return l-r

@debug_p('!!!!!!!!!!!!!!')
def add3(x,y,z):
    return x+y+z

sum = add(1, 2)
diff = sub(10, 4)
sum3 = add3(100, 200, 300)
noch_eine_summe = add(r=10, l=100)

print(sum)
print(diff)
print(sum3)
print(noch_eine_summe)

print(add.__name__)

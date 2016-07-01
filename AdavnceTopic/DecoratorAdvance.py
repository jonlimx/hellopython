from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print("Call {0}...".format(func.__name__))
        return func(*args, **kw)
    return wrapper


def log2(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print("{0} {1}()".format(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log
def gettime():
    print("2016/06/28")

@log2("Execute")
def gettime2():
    print("2016/06/28")


if __name__ == "__main__":
    gettime2()
    print(gettime2.__name__)
    gettime()
    print(gettime.__name__)



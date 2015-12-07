# doc string: we may have many many functions defined in a library, and it's hard to know all of them. So we need
# doc string, which is more like a comments for a function. And we have two ways to get it: obj.__doc__/help(obj)


def multiply(a, b):
    ''' A function that returns the result of a multiplies b

    :param a: 乘数
    :param b: 被乘数
    Input two arguments and you will get the result of a*b.
    '''
    return a*b


if __name__ == '__main__':
    print(multiply.__doc__)
    help(multiply)


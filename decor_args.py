def decor_unfolding_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args[::-1], **kwargs)
        return result

    return wrapper


@decor_unfolding_args
def f(*args):
    print(*args)


f(1, 2, 3, 4, 5, 6, 7)

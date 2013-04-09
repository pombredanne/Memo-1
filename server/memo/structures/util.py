from __pypy__.thread import atomic


def check_if_key_exists(function):
    def wrapper(*args):
        self = args[0]
        if self.is_dead:
            return 'KEY DOES NOT EXISTS'
        return function(*args)
    return wrapper


def write(function):
    function.write = True
    return function


def with_atomic(function):
    def wrapper(*args):
        with atomic:
            return function(*args)
    return function

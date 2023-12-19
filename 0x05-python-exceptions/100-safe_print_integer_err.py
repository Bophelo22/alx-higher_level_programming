#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except Exception as exception:
        print('Exception: {}'.format(exception), file=stderr)
        return (False)
    return (True)

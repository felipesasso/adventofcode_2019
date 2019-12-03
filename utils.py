import sys

def get_filename_from_arg():
    args = sys.argv
    if len(args) < 1 and len(args) > 2:
        raise ValueError('Only one argument accepted')
    return args[1]

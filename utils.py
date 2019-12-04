import sys

def get_filename_from_arg():
    args = sys.argv
    if len(args) < 1 and len(args) > 2:
        raise ValueError('Only one argument accepted')
    return args[1]

def get_int_list_from_file(filename, sep=None):
    with open(filename) as f:
        list_ = list(map(int, f.read().split(sep)))

    return list_

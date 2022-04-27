input = '1, 2, 34,5 ,  6'


def parse_conventional(input):
    # result = []
    # strs = input.split(',')
    # for s in strs:
    #     result.append(int(s.strip()))
    # return result
    return [int(s.strip()) for s in input.split(',')]


def parse_map(input):
    return list(map(int, map(str.strip, input.split(','))))


def parse_recursive(input):
    if not input:
        return []
    input = input.lstrip(', ')
    i = 1
    while input[:i].isdigit() and i < len(input):
        i += 1
    return [int(input[:i].rstrip(', '))] + parse_recursive(input[i:])


def curry(f):
    f_args = []
    def wrapper(*args):
        nonlocal f_args
        if args:
            f_args += args
            return wrapper
        res = f(*f_args)
        f_args = []
        return res
    return wrapper


@curry
def parse_curry(*args):
    # result = []
    # for a in args:
    #     result.append(int(a.strip(', ')))
    # return result
    return [int(a.strip(', ')) for a in args]


print('Conventional:')
print(parse_conventional(input))

print('\nMap:')
print(parse_map(input))

print('\nRecursion:')
print(parse_recursive(input))

print('\nCurrying:')
print(parse_curry('1, ')('  2 , ')('  34,   ')())

parse_curry('1, ')
parse_curry('  2 , ')
parse_curry('  34,   ')
parse_curry('5,')
parse_curry('6')
print(parse_curry())

parse_curry(', 7')
parse_curry(', 7')
parse_curry(', 7')
print(parse_curry())

print(parse_curry(*input.split(','))())

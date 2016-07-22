def filter_custom(l, f):
    '''Filter a list usin a function
    Return a new list that contains all the elements e of l
    for which f(e) is True
    :param l: a list
    :param f: a function that takes one argument and return either
    True of False
    '''
    new_list = []
    for e in l:
        if f(e):
            new_list.append(f(e))
    return new_list

def map_custom(l, f):
    '''Map a list using a function
    Return a new list that applies f(e) for every element e in l

    :param l: a list
    :param f: a function that takes one argument and returns a value
    '''
    new_list = []
    for e in l:
        new_list.append(f(e))
    return new_list
    pass

def reduce_custom(l, f, starting_value):
    ''' Reduce a list using a reducer function and a starting value

    Return a single value that applies f(v, e) for every
    e in l from left to right. The initial value for v
    should be starting_value, and subsequent values should
    be the previously calculated value from f(v, e)

    :param l: a list
    :param f: a function that takes one argument and returns a value
    :param staring_value: the beginning value for the reducer function
    computation
    '''
    new_list = []
    left_argument = starting_value
    for right_argument in l:
        left_argument = f(left_argument, right_argument)
    return left_argument

    f = lambda x, y: x + y
    print(reduce_custom([1,2,3,17], f, 0))

    pass

if __name__ == '__main__':
    l = [7,8,9]
    f = lambda x: x * 10
    print(map_custom(l, f))
    print(filter_custom(l, f))
    print(reduce_custom([1,2,3,17], f, 0))

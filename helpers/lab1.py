def test_median(foo):

    test_inputs = [
        [1, 2, 3, 4, 5],
        [2, 4, 8, 16, 32, 64],
        [-0.5, 8, 3.14, 42, 0, 1]
    ]

    test_outputs = [
        3,
        12,
        2.07
    ]

    for x, y in zip(test_inputs, test_outputs):

        if type(foo(x)) not in [int, float]:
            raise AssertionError(f'Expected an int or float, but got {type(foo(x))} as output')

        if foo(x) != y:
            raise AssertionError(f'Expected {y}, but got {foo(x)} for {x}')

    print('Seems OK!')

def test_euler(foo):

    test_dict = {
        0: 1,
        1: 2,
        4: 2.7083333333,
        6: 2.7180555556,
        10: 2.7182818011,
        100: 2.7182818285
    }

    for key, value in test_dict.items():
        if round(foo(key), 10) != value:
            raise AssertionError(f'Expected {value}, but got {foo(key)} for n = {key}')

    print('Seems OK!')
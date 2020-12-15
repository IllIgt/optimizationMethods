import pandas as pd
from .consts import E, DELTA, CONST_DELTA
from .initial_unimodal_segment import init_unimodal_segment


def get_fibonacci_sequence_up_to_n_value(n_value):
    last_element = current_element = 1
    fibonacci_sequence = [last_element, current_element]
    while current_element < n_value:
        last_element, current_element = current_element, last_element + current_element
        fibonacci_sequence.append(current_element)
    return fibonacci_sequence


def calculate_x(x_start, x_end, n, k, i, sequence):
    return x_start + ((sequence[n - k - i] / sequence[n - k]) * (x_end - x_start))


def fibonacci(x, func, delta=DELTA, e=E, const_delta=CONST_DELTA):
    x_uni_start, x_uni_end = init_unimodal_segment(x, func, delta)

    n_value = (x_uni_end-x_uni_start)/e
    fibonacci_sequence = get_fibonacci_sequence_up_to_n_value(n_value)
    n = len(fibonacci_sequence)-1
    x = calculate_x(x_uni_start, x_uni_end, n, 0, 2, fibonacci_sequence)
    x1 = calculate_x(x_uni_start, x_uni_end, n, 0, 1, fibonacci_sequence)
    y, y1 = map(func, [x, x1])

    for k in range(1, n-1):
        if y < y1:
            x_uni_end = x1
            x1 = x
            x = calculate_x(x_uni_start, x_uni_end, n, k, 2, fibonacci_sequence)

        elif y > y1:
            x_uni_start = x
            x = x1
            x1 = calculate_x(x_uni_start, x_uni_end, n, k, 1, fibonacci_sequence)

        y, y1 = map(func, [x, x1])

    x1 = x1 + const_delta
    y1 = func(x1)

    if y1 > y:
        opt_x = (x_uni_start+x)/2
    elif y1 < y:
        opt_x = (x+x_uni_end)/2
    else:
        raise Exception("n-1 positions are equals, check const_delta")

    return opt_x

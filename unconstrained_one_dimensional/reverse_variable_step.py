import pandas as pd
from .consts import E, B


def identify_delta_sign(x, delta, func):
    return -1 if func(x+delta) > func(x) > func(x-delta) else 1


def increment_with_delta(x, delta, b=B):
    new_delta = delta * -b
    return x, new_delta, x+new_delta


def fill_data_frame(data_frame, y, y1, x, x1, delta):
    data_frame["y"].append(y)
    data_frame["y1"].append(y1)
    data_frame["x"].append(x)
    data_frame["x1"].append(x1)
    data_frame["delta"].append(delta)


def reverse_step(x, delta, func, e=E, visualize=False):
    delta = abs(delta) * identify_delta_sign(x, delta, func)
    x1 = x + delta
    data_frame = {"y": [], "y1": [], "x": [], "x1": [], "delta": []}
    is_found = False

    while not is_found:
        y = func(x)
        y1 = func(x1)

        fill_data_frame(data_frame, y, y1, x, x1, delta)

        if y1 < y:
            x = x1
            x1 = x + delta

        elif y1 > y:
            if abs(delta) < e:
                is_found = True
            else:
                x, delta, x1 = increment_with_delta(x1, delta)

        else:
            if abs(delta) < e:
                is_found = True
                x = (x+x1)/2
            else:
                x, delta, x1 = increment_with_delta(x1, delta)

    df = pd.DataFrame(data_frame)

    if visualize:
        return df
    else:
        return x


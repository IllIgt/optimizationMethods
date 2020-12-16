from .initial_unimodal_segment import init_unimodal_segment
from .consts import CONST_DELTA, DELTA, E
import pandas as pd


def fill_data_frame(a, b, x, x1, y, y1, data_frame):
    data_frame["a"].append(a)
    data_frame["x"].append(x)
    data_frame["x1"].append(x1)
    data_frame["b"].append(b)
    data_frame["y"].append(y)
    data_frame["y1"].append(y1)


def half_division(x, func, delta=DELTA, const_delta=CONST_DELTA, e=E, visualize=False):
    data_frame = {"a": [], "x": [], "x1": [], "b": [], "y": [], "y1": []}

    x_uni_start, x_uni_end = init_unimodal_segment(x, func, delta)

    while x_uni_end - x_uni_start > e:
        x = (x_uni_start + x_uni_end) / 2 - const_delta
        x1 = x + (2 * const_delta)
        y, y1 = map(func, (x, x1))
        fill_data_frame(x_uni_start, x_uni_end, x, x1, y, y1, data_frame)

        if y < y1:
            x_uni_end = x1
        elif y > y1:
            x_uni_start = x
        else:
            x_uni_start = x
            x_uni_end = x1
    fill_data_frame(x_uni_start, x_uni_end, None, None, func(x_uni_start), func(x_uni_end), data_frame)
    x_opt = (x_uni_start+x_uni_end)/2
    if visualize:
        return pd.DataFrame(data_frame), x_opt
    else:
        return x_opt

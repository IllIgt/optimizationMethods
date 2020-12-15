from .initial_unimodal_segment import init_unimodal_segment
from .consts import E, DELTA
import pandas as pd


def divide_into_equal(x_start, x_end):
    x2 = (x_end + x_start) / 2
    x1 = (x2 + x_start) / 2
    x3 = (x_end + x2) / 2
    return x1, x2, x3


def find_min_x_by_y(xs, func):
    xy_correlation = {func(x): x for x in xs}
    return xy_correlation[min(xy_correlation.keys())]


def fill_data_frame(x, x1, x2, x3, x4, min_x, data_frame):
    data_frame["x"].append(x)
    data_frame["x1"].append(x1)
    data_frame["x2"].append(x2)
    data_frame["x3"].append(x3)
    data_frame["x4"].append(x4)
    data_frame["min_x"].append(min_x)
    data_frame["final"].append(x + ((x4 - x)/2))


def localize_optimum(x, func, delta=DELTA, e=E, visualize=False):
    init_seg = init_unimodal_segment(x, func, delta)
    data_frame = {"x": [], "x1": [], "x2": [], "x3": [], "x4": [], "min_x": [], "final": []}
    x = init_seg[0]
    x4 = init_seg[1]

    while x4 - x > e:
        x1, x2, x3 = divide_into_equal(x, x4)
        all_xs = [x, x1, x2, x3, x4]
        min_x = find_min_x_by_y(all_xs, func)
        min_x_index = all_xs.index(min_x)
        fill_data_frame(x, x1, x2, x3, x4, min_x, data_frame)
        x = all_xs[min_x_index - 1 if min_x_index != 0 else min_x_index]
        x4 = all_xs[min_x_index + 1 if min_x_index != len(all_xs)-1 else min_x_index]

    x_opt = (x4 + x)/2

    if visualize:
        return pd.DataFrame(data_frame), x_opt
    else:
        return x_opt




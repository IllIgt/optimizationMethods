from .initial_unimodal_segment import init_unimodal_segment
from .consts import K, DELTA, E
from .dichtomy import fill_data_frame
import pandas as pd


def golden_section(x, func, delta=DELTA, k=K, e=E, visualize=False):
    x_uni_start, x_uni_end = init_unimodal_segment(x, func, delta)
    data_frame = {"a": [], "x": [], "x1": [], "b": [], "y": [], "y1": []}

    while x_uni_end - x_uni_start > e:
        x = x_uni_start + ((1 - k) * (x_uni_end - x_uni_start))
        x1 = x_uni_start + (k * (x_uni_end - x_uni_start))
        y, y1 = map(func, [x, x1])

        fill_data_frame(x_uni_start, x_uni_end, x, x1, y, y1, data_frame)

        if y < y1:
            x_uni_end = x1
        elif y > y1:
            x_uni_start = x

    fill_data_frame(x_uni_start, x_uni_end, None, None, func(x_uni_start), func(x_uni_end), data_frame)
    opt_x = (x_uni_start+x_uni_end)/2
    if visualize:
        return pd.DataFrame(data_frame), opt_x
    else:
        return opt_x

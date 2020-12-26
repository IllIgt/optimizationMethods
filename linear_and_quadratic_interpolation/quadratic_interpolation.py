from .quadratic_polynomial_minimum import get_minimum
from .consts import E
from unconstrained_one_dimensional.powell_quadratic_interpolation import find_x_of_max_y
import pandas as pd
import pylab
import numpy as np


def draw(func, interval):
    x_dots = np.linspace(-3.2, 1.2)
    y_dots = [func(x) for x in x_dots]
    pylab.plot(x_dots, y_dots, label="""analyzed function""")
    pylab.scatter(interval[0], func(interval[0]), c='r')
    pylab.scatter(interval[1], func(interval[1]), c='r')
    pylab.xlabel('X', fontsize=16)
    pylab.ylabel('Y', fontsize=16)
    pylab.xticks(fontsize=12)
    pylab.yticks(fontsize=12)
    pylab.grid()
    pylab.legend(fontsize=12)
    pylab.show()


def fill_data_frame(data_frame, x, x1, x2, xt, d_x, d_y):
    data_frame["x"].append(x)
    data_frame["x1"].append(x1)
    data_frame["x2"].append(x2)
    data_frame["xt"].append(xt)
    data_frame["delta_x"].append(d_x)
    data_frame["delta_y"].append(d_y)


def sort_by_y(xs, func):
    y_to_x_correlation = {func(x): x for x in xs}
    sorted_y = sorted(y_to_x_correlation.keys())
    return [y_to_x_correlation[y] for y in sorted_y]


def interpolate(func, interval, e=E, visualize=False):
    data_frame = {"x": [], "x1": [], "x2": [], "xt": [], "delta_x": [], "delta_y": []}
    if visualize:
        draw(func, interval)

    x = interval[0]
    x2 = interval[1]
    x1 = (x+x2)/2
    if not (func(x) > func(x1) and func(x2) > func(x1)):
        raise Exception("Unable to interpolate segment. Make sure the function on the segment is unimodal and convex")
    xt = get_minimum(x, x1, x2, func)
    min_x = min([x, x1, x2])
    delta_y = abs(min(map(func, [x, x1, x2])) - func(xt))
    delta_x = abs(min_x-xt)

    fill_data_frame(data_frame, x, x1, x2, xt, delta_x, delta_y)

    while delta_y > e or delta_x > e:

        opt_x = min_x if func(min_x) <= func(xt) else xt
        all_xs = [x, x1, x2, opt_x]

        opt_x_index = all_xs.index(opt_x)
        if opt_x_index != 0 and opt_x_index != len(all_xs) - 1:
            opt_x_index = all_xs.index(opt_x)
            x1 = all_xs[opt_x_index - 1]
            x = opt_x
            x2 = all_xs[opt_x_index + 1]

        else:
            prev_xs = all_xs.copy()
            prev_xs.remove(xt)
            x_of_max_y = find_x_of_max_y(prev_xs, func)
            all_xs.remove(x_of_max_y)
            x = all_xs[0]
            x1 = all_xs[1]
            x2 = all_xs[2]

        min_x = min(x, x1, x2)
        xt = get_minimum(x, x1, x2, func)
        delta_y = abs(min(map(func, [x, x1, x2])) - func(xt))
        delta_x = abs(min_x - xt)
        fill_data_frame(data_frame, x, x1, x2, xt, delta_x, delta_y)

    if visualize:
        df = pd.DataFrame(data_frame)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        pd.options.display.expand_frame_repr = False
        return df
    else:
        return xt

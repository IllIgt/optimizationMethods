from .quadratic_approximation import approximation
from .consts import E, DELTA
import pandas as pd


def find_x_of_max_y(xs, func):
    y_to_x_correlation = {func(x): x for x in xs}
    return y_to_x_correlation[max(y_to_x_correlation.keys())]


def find_min_x_by_y(xs, func):
    y_to_x_correlation = {func(x): x for x in xs}
    return y_to_x_correlation[min(y_to_x_correlation.keys())]


def update_vars(x, x1, x2, func):
    y, y1, y2 = map(func, [x, x1, x2])
    min_x = find_min_x_by_y([x, x1, x2], func)
    tx = approximation(x, x1, x2, y, y1, y2)
    return y, y1, y2, min_x, tx


def fill_data_frame(data_frame, x, x1, x2, tx, y, y1, y2):
    data_frame["x"].append(x)
    data_frame["x1"].append(x1)
    data_frame["x2"].append(x2)
    data_frame["y"].append(y)
    data_frame["y1"].append(y1)
    data_frame["y2"].append(y2)
    data_frame["tx"].append(tx)


def powell_pre_calculation(x, func, delta):
    x1 = x + delta
    y = func(x)
    y1 = func(x1)
    if y > y1:
        x2 = x + 2 * delta
    else:
        x2 = x - delta

    return x, x1, x2, y, y1, func(x2)


def powell(x, func, delta=DELTA, e=E, visualize=False):
    data_frame = {"x": [], "x1": [], "x2": [], "tx": [], "y": [], "y1": [], "y2": []}
    x, x1, x2, y, y1, y2 = powell_pre_calculation(x, func, delta)

    y_to_x_correlation = {y: x, y1: x1, y2: x2}
    min_x = y_to_x_correlation[min([y, y1, y2])]
    tx = approximation(x, x1, x2, y, y1, y2)

    fill_data_frame(data_frame, x, x1, x2, tx, y, y1, y2)

    while abs(min_x - tx) > e:
        opt_x = min_x if func(min_x) <= func(tx) else tx
        all_xs = sorted([x, x1, x2, tx])
        opt_x_index = all_xs.index(opt_x)
        if opt_x_index != 0 and opt_x_index != len(all_xs) - 1:
            opt_x_index = all_xs.index(opt_x)
            x1 = all_xs[opt_x_index - 1]
            x = opt_x
            x2 = all_xs[opt_x_index + 1]

        else:
            prev_xs = all_xs.copy()
            prev_xs.remove(tx)
            x_of_max_y = find_x_of_max_y(prev_xs, func)
            all_xs.remove(x_of_max_y)
            x = all_xs[0]
            x1 = all_xs[1]
            x2 = all_xs[2]

        y, y1, y2, min_x, tx = update_vars(x, x1, x2, func)

        fill_data_frame(data_frame, x, x1, x2, tx, y, y1, y2)

    if visualize:
        df = pd.DataFrame(data_frame)
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        pd.options.display.expand_frame_repr = False
        return df
    else:
        return tx

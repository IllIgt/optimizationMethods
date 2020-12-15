import pandas as pd


def fill_data_frame(x, delta, y, y1, sign, data_frame):
    data_frame["x_start"].append(x)
    data_frame["x_end"].append(x+delta)
    data_frame["y"].append(y)
    data_frame["y1"].append(y1)
    data_frame["sign"].append(sign)


def init_unimodal_segment(x, func, delta, visualize=False):
    data_frame = {"x_start": [], "x_end": [], "y": [], "y1": [], "sign": []}
    y = func(x)
    sign = 1 if func(x-delta) < func(x) < func(x+delta) else -1
    delta = delta * -sign
    y1 = func(x + delta)

    fill_data_frame(x, delta, y, y1, sign, data_frame)

    changed_sign = sign * -1
    delta_multi = 1

    while not sign == changed_sign:
        delta_multi = delta_multi + 1
        y = y1
        y1 = func(x+(delta_multi*delta))
        if sign == -1:
            sign = 1 if y < y1 else -1
        else:
            sign = -1 if y < y1 else 1

        fill_data_frame(x, delta*delta_multi, y, y1, sign, data_frame)

    if visualize:
        return pd.DataFrame(data_frame)
    else:
        return [x, x+(delta*delta_multi)]


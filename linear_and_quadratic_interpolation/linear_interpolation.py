from .reverse_linear_interpolation import find_segment_indexes


def interpolate(xs, ys, target_x, visualize=False):
    if len(xs) != len(ys):
        raise Exception("x and y arrays must be the same length")

    indexes = find_segment_indexes(xs, target_x)
    x = xs[indexes[0]]
    x1 = xs[indexes[1]]
    y = ys[indexes[0]]
    y1 = ys[indexes[1]]
    ndigits = abs(str(x).find('.') - len(str(x)))
    augmentation = round((((y1-y)/(x1-x)) * (target_x-x)), ndigits)

    if visualize:
        print(f"Xk = {x}, Xk+1 = {x1}, Yk = {y}, Yk+1 = {y1}, X={target_x}")
        print("----------------------------------------------")
        print(f"Y ~= {y} + (({y1}-{y})/({x1}-{x}))*({target_x}-{x}) = ")
        print(f" = {y} + {(y1-y)/(x1-x)} * {target_x-x} = ")
        print(f" = {y} + {augmentation} = ")

    return round(y + augmentation, ndigits)

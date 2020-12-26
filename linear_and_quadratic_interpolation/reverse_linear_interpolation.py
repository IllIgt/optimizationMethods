def find_segment_indexes(elements, target_value):
    for i, value in enumerate(elements):
        if value <= target_value <= elements[i+1]:
            return i, i+1


def interpolate(xs, ys, target_y, visualize=False):
    if len(xs) != len(ys):
        raise Exception("x and y arrays must be the same length")

    indexes = find_segment_indexes(ys, target_y)
    x = xs[indexes[0]]
    x1 = xs[indexes[1]]
    y = ys[indexes[0]]
    y1 = ys[indexes[1]]
    ndigits = abs(str(x).find('.') - len(str(x)))
    augmentation = round((((x1-x)/(y1-y))*(target_y-y)), ndigits)

    if visualize:
        print(f"Xk = {x}, Xk+1 = {x1}, Yk = {y}, Yk+1 = {y1}, Y={target_y}")
        print("----------------------------------------------")
        print(f"X ~= {x} + (({x1}-{x})/({y1}-{y}))*({target_y}-{y}) = ")
        print(f" = {x} + {(x1-x)/(y1-y)} * {target_y-y} = ")
        print(f" = {x} + {augmentation} = ")
    return round(x+augmentation, ndigits)


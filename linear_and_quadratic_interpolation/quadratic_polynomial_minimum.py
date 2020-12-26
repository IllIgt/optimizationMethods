def get_minimum(x1, x2, x3, func):
    y1, y2, y3 = map(func, [x1, x2, x3])
    return 0.5*(((y1*((x2*x2)-(x3*x3))) + (y2*((x3*x3)-(x1*x1))) + (y3*((x1*x1)-(x2*x2)))) /
                ((y1*(x2-x3)) + (y2*(x3-x1)) + (y3*(x1-x2))))

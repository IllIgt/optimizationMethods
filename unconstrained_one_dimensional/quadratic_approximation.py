def approximation(x, x1, x2, y, y1, y2):
    a1 = (y1-y)/(x1-x)
    a2 = (1/(x2-x1))*(((y2-y)/(x2-x)) - ((y1-y)/(x1-x)))
    return ((x1+x)/2) - (a1/(2*a2))

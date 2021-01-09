import numpy as np
import pylab


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


def get_spline(points):
    N = len(points) - 1
    w = [(points[i + 1].x - points[i].x) for i in range(N)]
    h = [(points[i + 1].y - points[i].y) / w[i] for i in range(N)]
    ftt = [0] + [3 * (h[i + 1] - h[i]) / (w[i + 1] + w[i]) for i in range(N - 1)] + [0]
    A = [(ftt[i + 1] - ftt[i]) / (6 * w[i]) for i in range(N)]
    B = [ftt[i] / 2 for i in range(N)]
    C = [h[i] - w[i] * (ftt[i + 1] + 2 * ftt[i]) / 6 for i in range(N)]
    D = [points[i].y for i in range(N)]
    return A, B, C, D


def print_spline(points, A, B, C, D):
    for i in range(len(points) - 1):
        func = str(points[i].x) + ' <= x <= ' + str(points[i + 1].x) + ' : f(x) = '
        components = []
        if A[i]:
            components.append(f"{round(A[i], 4)} * (x-{points[i].x})^3")
        if B[i]:
            components.append(f"{round(B[i], 4)} * (x-{points[i].x})^2")
        if C[i]:
            components.append(f"{round(C[i], 4)} * (x-{points[i].x})")
        if D[i]:
            components.append(str(round(D[i], 4)))
        if components:
            func += components[0]
            for i in range(1, len(components)):
                if components[i][0] == '-':
                    func += ' - ' + components[i][1:]
                else:
                    func += ' + ' + components[i]
            print(func)
        else:
            print(func + '0')


def build_interpolated_func(point, A, B, C, D):
     return lambda x: (A * ((x-point.x)**3)) + \
               (B * ((x-point.x)**2)) + \
               (C * (x-point.x)) + D


def build_all_interpolated_funcs(points, A, B, C, D):
    funcs = []
    for i in range(len(points) - 1):
        funcs.append(build_interpolated_func(points[i], A[i], B[i], C[i], D[i]))
    return funcs


def draw_splines(points, funcs):
    for i, func in enumerate(funcs):
        x_dots = np.linspace(points[i].x, points[i+1].x)
        y_dots = [func(x) for x in x_dots]
        pylab.plot(x_dots, y_dots, label=f"S{i+1}")
    for point in points:
        pylab.scatter(point.x, point.y, c='r')
    pylab.xlabel('X', fontsize=16)
    pylab.ylabel('Y', fontsize=16)
    pylab.xticks(fontsize=12)
    pylab.yticks(fontsize=12)
    pylab.grid()
    pylab.legend(fontsize=12)
    pylab.show()


def draw_spline_by_func(func):
    x_dots = np.linspace(-1, 2)
    y_dots = [func(x) for x in x_dots]
    pylab.plot(x_dots, y_dots, label="""analyzed function""")

    # half_x = np.arange(-1, 2.5, 0.5)
    # half_points = []
    # for x in half_x:
    #     half_points.append(Point(x, func(x)))
    # A, B, C, D = get_spline(half_points)
    # funcs = build_all_interpolated_funcs(half_points, A, B, C, D)
    # for i, func in enumerate(funcs):
    #     x_dots = np.linspace(half_points[i].x, half_points[i+1].x)
    #     y_dots = [func(x) for x in x_dots]
    #     pylab.plot(x_dots, y_dots, linestyle='dotted', c="g")
    # for point in half_points:
    #     pylab.scatter(point.x, point.y, c='r')

    quad_x = np.arange(-1, 2.2, 0.25)
    quad_points = []
    for x in quad_x:
        quad_points.append(Point(x, func(x)))
    A, B, C, D = get_spline(quad_points)
    funcs = build_all_interpolated_funcs(quad_points, A, B, C, D)
    for i, func in enumerate(funcs):
        x_dots = np.linspace(quad_points[i].x, quad_points[i + 1].x)
        y_dots = [func(x) for x in x_dots]
        pylab.plot(x_dots, y_dots, linestyle='dotted', c="y")
    for point in quad_points:
        pylab.scatter(point.x, point.y, c='b')

    pylab.xlabel('X', fontsize=16)
    pylab.ylabel('Y', fontsize=16)
    pylab.xticks(fontsize=12)
    pylab.yticks(fontsize=12)
    pylab.grid()
    pylab.legend(fontsize=12)
    pylab.show()

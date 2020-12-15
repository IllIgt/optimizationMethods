import pylab
import numpy as np
from scipy.misc import derivative


def analyzed_func(x):
    return x*x + 5*x


def alter_analyzed_func(x):
    return (16/x)+(4*x)


def auto_computed_func(x):
    return (x*x*x)+((x*x*x*x)/4)


def calculated_first_diff(x):
    return 2*x+5


def draw(func):
    x_dots = np.linspace(-15, 15)
    y_dots = [func(x) for x in x_dots]
    y_second_diff_dots = [derivative(func, x, n=2) for x in x_dots]
    y_self_calculated_diff = [calculated_first_diff(x) for x in x_dots]
    pre_calculated_min = -2.5
    pylab.plot(x_dots, y_dots, label="""analyzed function""")
    pylab.plot(x_dots, y_second_diff_dots, 'black', label="""second_diff""", linestyle='--')
    pylab.plot(x_dots, y_self_calculated_diff, "r", label="""first_diff""")
    pylab.plot(
        [pre_calculated_min, pre_calculated_min], [0, func(pre_calculated_min)],
        linestyle='--',
        linewidth=2,
        color='black'
    )
    pylab.scatter(pre_calculated_min, 0, c='r')
    pylab.annotate("-2.5", xy=(pre_calculated_min, 0))
    pylab.xlabel('X', fontsize=16)
    pylab.ylabel('Y', fontsize=16)
    pylab.xticks(fontsize=12)
    pylab.yticks(fontsize=12)
    pylab.grid()
    pylab.legend(fontsize=12)
    pylab.show()

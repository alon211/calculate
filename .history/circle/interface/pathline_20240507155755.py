import numpy as np
def configPar(accur)
def circlePath(radius,T,center_x,center_y):
    angle = (T - radius * 10) * (2 * np.pi / (100 - radius * 10))
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return T
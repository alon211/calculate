import numpy as np
def configPar(accuracy,radius,T,center_x,center_y):
    dynameter
def circlePath(radius,T,center_x,center_y):
    angle = (T - radius) * (2 * np.pi / (100 - radius))
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return T
import numpy as np
def circlePath(radius,Tcenter_x,center_y):
    angle = (frame - radius * 10) * (2 * np.pi / (100 - radius * 10))
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
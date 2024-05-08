import numpy as np
def configPar(accuracy,in_radius,ex_T,center_x,center_y):
    dynameter=1/accuracy #倍率
    
    
def circlePath(radius,T,center_x,center_y):
    angle = (T - radius) * (2 * np.pi / (100 - radius))
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return x,y
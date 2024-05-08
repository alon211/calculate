import numpy as np
def configPar(accuracy,in_radius,ex_radius,T,center_x,center_y):
    dynameter=1/accuracy #倍率
    
# 单轴运动   
def linePath(distance,v,T1,start_x,end_x):
    # T1间隔的时间单位，需要和v的时间单位一直
    # 计算沿X轴移动的时间
    time_move_x = distance / v
    trajectory_points=[]
    for t in np.arange(0, time_move_x, T1):
        x = time_move_x + v * t
        trajectory_points.append(x)
def di        
def circlePath(radius,T,center_x,center_y):
    angle = (T - radius) * (2 * np.pi / (100 - radius))
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return x,y
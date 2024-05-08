import matplotlib.pyplot as plt

import numpy as np


# 设置圆的参数
# radius = 1  # 内半径
# ex_radius= 10 # 外半径
# center_x, center_y = 5, 6  # 圆心坐标

act_angle=0

LINE=10
CIRCLE=20
act_n=0 #当前运行的圈数
circle_act_n=0  #实际运行的圈数字
action=0
act_line=0
act_angle=0
last_action=0
def createCanvas():
    # 创建图形和轴
    fig, ax = plt.subplots()
    # ax.set_xlim(0, (ex_radius+center_x)+0.1)
    # ax.set_ylim(0, (ex_radius+center_y)+0.1)

    # 创建一个点，表示圆上的位置
    point, = ax.plot([], [], 'bo')

    # 创建一个线对象，用于绘制轨迹
    trajectory_line, = ax.plot([], [], 'b-', lw=2)  # 轨迹线
    return fig,point,trajectory_line,ax

# 初始化函数，设定绘图元素
def init(ax,point,trajectory_line,ex_radius,center_x, center_y):
    ax.set_xlim(0, (ex_radius+center_x)+0.1)
    ax.set_ylim(0, (ex_radius+center_y)+0.1)
    point.set_data([], [])
    trajectory_line.set_data([], [])
    return point, trajectory_line

# 更新函数，用于动画的每一帧
def update(frame,line_n,point,tool_r, trajectory_line,radius,center_x, center_y,accurancy,max_frames):
    act_radius=radius+tool_r*act_n #当前半径=内圆半径+工具半径*圈数
    if frame < act_radius+act_radius*act_n :  
        action=LINE
    elif frame >= act_radius+act_radius*act_n and frame<act_radius+act_radius*(act_n+1):
        action=CIRCLE
        
    if action==LINE:
        if last_action!=action:
                act_line=0
        else:
            x = center_x +act_line*accurancy
    elif action==CIRCLE:
        
    if frame < radius :  # 假设每帧移动0.1个单位
        x = center_x + frame*accurancy
        y = center_y
        act_angle=0
    # 绘制圆形轨迹
    else:
        act_angle=accurancy+act_angle
        angle = act_angle * (2 * np.pi / (360.0/accurancy))
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)

    # 更新点的位置
    point.set_data(x, y)
    if frame==max_frames:
        ani.event_source.stop()
    # 更新轨迹线的数据
    if frame >= radius :
        old_data = trajectory_line.get_data()
        trajectory_line.set_data(np.append(old_data[0], x), np.append(old_data[1], y))
    last_action=action
    return point, trajectory_line

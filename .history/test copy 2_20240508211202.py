import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math
# 预设参数
radius = 1  # 内半径 正代表从圆心右边开始，负代表从圆心左边开始
ex_radius = 10 # 外半径
center_x, center_y = 5, 6  # 圆心坐标
lineToX=True  #默认沿着X方向走半径后画圆
tool_d=0.2  #工具直径
accurancy=0.1  #精度
interval=100  #动画间隔时间ms
##################################
LINE=10
CIRCLE=20
line_n=math.ceil(ex_radius-radius)/tool_d #测算line直线需要移动几次 SCL用法 CEIL_REAL(REAL_VAR); // 同样会得到2
print(f'直线需要移动{line_n}次')
max_frames=int((line_n*360+ex_radius-center_x)/accurancy)
last_action=0
action=0
act_line=0.0
act_angle=0.0
act_n=0

tool_r=tool_d/2.0
# 创建图形和轴
fig, ax = plt.subplots()
ax.set_xlim(-ex_radius+center_x, ex_radius+center_x)
ax.set_ylim(-ex_radius+center_y, ex_radius+center_y)

# 创建一个点，表示圆上的位置
point, = ax.plot([], [], 'bo')

# 创建一个线对象，用于绘制轨迹
trajectory_line, = ax.plot([], [], 'b-', lw=2)  # 轨迹线

# 初始化函数，设定绘图元素
def init():
    point.set_data([center_x], [center_y])
    trajectory_line.set_data([center_x], [center_y])
    return point, trajectory_line

# 更新函数，用于动画的每一帧
def update(frame):
    global last_action, action, act_line, act_angle, act_n, x, y
    act_radius=radius+tool_r*act_n #当前半径=内圆半径+工具半径*圈数
  
    print(f'frame:{frame}')
    print(f'act_radius:{act_radius}')
    print(f'act_n:{act_n}') 
    print(f'accurancy:{accurancy}') 
    print(f'action:{action}') 
    print(f'last_action:{last_action}')    
    print(f'frame*accurancy < act_radius+act_radius*act_n:{frame*accurancy < act_radius+act_radius*act_n}')
    if frame*accurancy < act_radius+act_radius*act_n :   #直线运动
        action=LINE
        if last_action!=action:               
                act_line = 0
                act_angle = 0
        else:
            x = center_x +act_line
            act_line=act_line+accurancy
        y = center_y
    elif frame*accurancy >= act_radius+act_radius*act_n and frame<act_radius+act_radius*(act_n+1): #圆运动
        action=CIRCLE
        if last_action!=action:               
                act_line = 0
                act_angle = 0
        else:
                act_angle=accurancy+act_angle
                angle = act_angle * (2 * np.pi / (360.0/accurancy))
                x = center_x + radius * np.cos(angle)
                y = center_y + radius * np.sin(angle)
 
 
    # # 移动到圆的边缘
    # if frame < radius * 10:  # 假设每帧移动0.1个单位
    #     x = center_x + frame / 10
    #     y = center_y
    # # 绘制圆形轨迹
    # else:
    #     angle = (frame - radius * 10) * (2 * np.pi / (100 - radius * 10))
    #     x = center_x + radius * np.cos(angle)
    #     y = center_y + radius * np.sin(angle)

    # 更新点的位置
    try:
        point.set_data(x, y)
    except Exception as e:
        pass
    point.set_data(x, y)
    if frame >= max_frames:
        ani.event_source.stop()
    # 更新轨迹线的数据
    # if frame >= radius * 10:
    old_data = trajectory_line.get_data()
    trajectory_line.set_data(np.append(old_data[0], x), np.append(old_data[1], y))
    last_action = action
    print(f'x,y:{(x,y)}') 
    print(f'line_x:{old_data[0]}') 
    print(f'line_y:{old_data[1]}') 
    
    return point, trajectory_line

# 创建动画对象
ani = FuncAnimation(fig, update, frames=np.arange(0, max_frames, 1),
                    init_func=init, blit=True,interval=interval)

# 暂停动画的函数
def pause_animation():
    ani.event_source.stop()

# 继续动画的函数
def resume_animation():
    ani.event_source.start()

# 创建 Tkinter 根窗口
root = tk.Tk()
root.title("Matplotlib in Tkinter with Control Panel")

# 设置窗口的最小大小
root.minsize(900, 900)

# 创建控制面板区域
control_panel = tk.Frame(root, width=300, bg='lightgray')
control_panel.pack(side=tk.LEFT, fill=tk.Y)

# 在控制面板中添加按钮
bpause = tk.Button(control_panel, text="pause", command=pause_animation)
bpause.pack(pady=10)
bresume = tk.Button(control_panel, text="resume", command=resume_animation)
bresume.pack(pady=10)

# 创建 FigureCanvasTkAgg 对象，将 fig 与 Tkinter 根窗口关联
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# 创建工具栏并将其添加到 Tkinter 窗口中
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# 将 canvas 放置到窗口中
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# 启动 Tkinter 事件循环
root.mainloop()

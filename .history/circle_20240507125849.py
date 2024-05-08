import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
# 设置圆的参数
radius = 1  # 内半径
ex_radius= 10 # 外半径
center_x, center_y = 5, 6  # 圆心坐标

# 创建图形和轴
fig, ax = plt.subplots()
ax.set_xlim(0, (ex_radius+center_x)+0.1)
ax.set_ylim(0, (ex_radius+center_y)+0.1)

# 创建一个点，表示圆上的位置
point, = ax.plot([], [], 'bo')

# 创建一个线对象，用于绘制轨迹
trajectory_line, = ax.plot([], [], 'b-', lw=2)  # 轨迹线

# 初始化函数，设定绘图元素
def init():
    point.set_data([], [])
    trajectory_line.set_data([], [])
    return point, trajectory_line

# 更新函数，用于动画的每一帧
def update(frame):
    # 移动到圆的边缘
    if frame < radius * 10:  # 假设每帧移动0.1个单位
        x = center_x + frame / 10
        y = center_y
    # 绘制圆形轨迹
    else:
        angle = (frame - radius * 10) * (2 * np.pi / (100 - radius * 10))
        x = center_x + radius * np.cos(angle)
        y = center_y + radius * np.sin(angle)

    # 更新点的位置
    point.set_data(x, y)

    # 更新轨迹线的数据
    if frame >= radius * 10:
        old_data = trajectory_line.get_data()
        trajectory_line.set_data(np.append(old_data[0], x), np.append(old_data[1], y))

    return point, trajectory_line

# 创建动画对象
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1),
                    init_func=init, blit=True)
# 暂停动画的函数
def pause_animation(event):
    ani.event_source.stop()

# 继续动画的函数
def resume_animation(event):
    ani.event_source.start()

# 添加按钮
axpause = plt.axes([0.7, 0.05, 0.1, 0.075])
axresume = plt.axes([0.81, 0.05, 0.1, 0.075])
bpause = Button(axpause, 'pause')
bresume = Button(axresume, '继续')

# 设置按钮的回调函数
bpause.on_clicked(pause_animation)
bresume.on_clicked(resume_animation)
plt.show()

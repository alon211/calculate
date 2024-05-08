import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# 设置圆的参数
radius = 1000  # 半径
center_x, center_y = 0, 0  # 圆心坐标

# 创建图形和轴
fig, ax = plt.subplots()
ax.set_xlim(-radius-0.1*radius, radius+0.1*radius)
ax.set_ylim(-radius-0.1*radius, radius+0.1*radius)

# 创建一个线对象，用于绘制轨迹
trajectory_line, = ax.plot([], [], 'b-', lw=2)  # 轨迹线

# 初始化函数，设定绘图元素
def init():
    trajectory_line.set_data([], [])
    return trajectory_line,

# 更新函数的工厂函数
def make_update_func(animation):
    # 更新函数，用于动画的每一帧
    def update(frame):
        # 移动到圆的边缘
        if frame < radius:
            x = center_x + frame
            y = center_y
            trajectory_line.set_data(x, y)
        # 绘制圆形轨迹
        else:
            angle = (frame - radius) * (2 * np.pi / 360)
            x = center_x + radius * np.cos(angle)
            y = center_y + radius * np.sin(angle)
            old_data = trajectory_line.get_data()
            trajectory_line.set_data(np.append(old_data[0], x), np.append(old_data[1], y))
        
        # 检查是否完成了一次完整的轨迹
        if frame == radius + 359:  # 最后一帧
            animation.event_source.stop()  # 暂停动画
        
        return trajectory_line,
    return update

# 创建动画对象
ani = FuncAnimation(fig, make_update_func(None), frames=np.arange(0, radius + 360, 1),
                    init_func=init, blit=False, repeat=True)

# 更新工厂函数以包含动画对象
update = make_update_func(ani)

# 添加重新开始按钮
def restart_animation(event):
    ani.event_source.start()  # 重新开始动画

ax_restart_button = plt.axes([0.7, 0.05, 0.1, 0.04])
restart_button = Button(ax_restart_button, 'Restart')
restart_button.on_clicked(restart_animation)

plt.show()

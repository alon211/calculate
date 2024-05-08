import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np

# 设置圆的参数
radius = 1  # 内半径
ex_radius = 10 # 外半径
center_x, center_y = 5, 6  # 圆心坐标

# 创建图形和轴
fig, ax = plt.subplots(1,1)
ax.set_xlim(0, 20)
ax.set_ylim(0, 20)

# 计算圆形轨迹的点
angle = np.linspace(0, 2 * np.pi, 100)
x = center_x + radius * np.cos(angle)
y = center_y + radius * np.sin(angle)

# 绘制轨迹
ax.plot(x, y, 'b-', lw=2)

# 创建 Tkinter 根窗口
root = tk.Tk()
root.title("Matplotlib in Tkinter with Static Trajectory")

# 设置窗口的最小大小
root.minsize(900, 900)

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
plt.show()
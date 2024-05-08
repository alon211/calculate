import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# 创建 Tkinter 根窗口
root = tk.Tk()

# 创建一个 matplotlib 图形和轴
fig, ax = plt.subplots()

# 创建 FigureCanvasTkAgg 对象，将 fig 与 Tkinter 根窗口关联
canvas = FigureCanvasTkAgg(fig, master=root)

# 将 matplotlib 绘制的图形显示在 Tkinter 窗口中
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# 启动 Tkinter 事件循环
root.mainloop()

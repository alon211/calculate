import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

# 创建 Tkinter 根窗口
root = tk.Tk()

# 创建一个 matplotlib 图形和轴
fig, ax = plt.subplots()

# 创建 FigureCanvasTkAgg 对象，将 fig 与 Tkinter 根窗口关联
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

# 创建工具栏并将其添加到 Tkinter 窗口中
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# 将 canvas 和 toolbar 放置到窗口中
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
toolbar.pack(side=tk.BOTTOM, fill=tk.X)

# 启动 Tkinter 事件循环
root.mainloop()

plt.show()
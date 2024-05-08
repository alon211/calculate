from interface.controlInterface import root
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


# 创建 FigureCanvasTkAgg 对象，将 fig 与 Tknter 根窗口关联
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

 
# 创建工具栏并将其添加到 Tkinter 窗口中
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# 将 canvas 放置到窗口中
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)



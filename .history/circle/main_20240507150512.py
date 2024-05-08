from interface.controlInterface import root,bpause,bresume
from interface.plotyInterface import module_init,fig,ax,ani
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# 暂停动画的函数
def pause_animation():
    ani.event_source.stop()

# 继续动画的函数
def resume_animation():
    ani.event_source.start()
module_init(radius=5,1)
bpause.bind("<Button-1>", pause_animation)

# 创建 FigureCanvasTkAgg 对象，将 fig 与 Tknter 根窗口关联
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()

 
# 创建工具栏并将其添加到 Tkinter 窗口中
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# 将 canvas 放置到窗口中
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# 启动 Tkinter 事件循环
root.mainloop()

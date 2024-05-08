from interface.controlInterface import root,bpause,bresume
from interface.plotyInterface import module_init,fig,init,update
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import functools
from matplotlib.animation import FuncAnimation
import numpy as np
# 暂停动画的函数
def pause_animation():
    ani.event_source.stop()

# 继续动画的函数
def resume_animation():
    ani.event_source.start()
  
    


radius = 1  # 内半径
ex_radius= 10 # 外半径
center_x, center_y = 5, 6  # 圆心坐标
init_partial = functools.partial(init, ex_radius,center_x, center_y)
update_partial = functools.partial(update, radius,center_x, center_y)
# 创建动画对象
ani = FuncAnimation(fig, update_partial, frames=np.arange(0, 100, 1),
                    init_func=init_partial, blit=True)

bpause.bind("<Button-1>", pause_animation)
bresume.bind("<Button-1>", resume_animation)

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

plt.show()
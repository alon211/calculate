from interface.controlInterface import root,bpause,bresume
from interface.plotyInterface import createCanvas,init,update
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import functools
from matplotlib.animation import FuncAnimation
import numpy as np

  
    


radius = 1  # 内半径
ex_radius= 10 # 外半径
center_x, center_y = 5, 6  # 圆心坐标

fig,point,trajectory_line,ax=createCanvas()
init_partial = functools.partial(init, ax=ax,point=point,trajectory_line=trajectory_line,ex_radius=ex_radius,center_x=center_x, center_y=)
update_partial = functools.partial(update, point=point, trajectory_line=trajectory_line,radius=,center_x=center_x, center_y=center_y)
# 创建动画对象
ani = FuncAnimation(fig, update_partial, frames=np.arange(0, 100, 1),
                    init_func=init_partial, blit=True)



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
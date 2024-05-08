from interface.controlInterface import root,bpause,bresume
from interface.plotyInterface import createCanvas,init,update
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import functools
from matplotlib.animation import FuncAnimation
import numpy as np
import math
  
 # 暂停动画的函数
def pause_animation(event):
    ani.event_source.stop()

# 继续动画的函数
def resume_animation(event):
    ani.event_source.start()   


radius = 1  # 内半径 正代表从圆心右边开始，负代表从圆心左边开始
ex_radius= 10 # 外半径
act_radius=radius #当前半径
center_x, center_y = 5, 6  # 圆心坐标
lineToX=True  #默认沿着X方向走半径后画圆
tool_d=0.2  #工具直径
(ex_radius-radius)/tool_d 
fig,point,trajectory_line,ax=createCanvas()
init_partial = functools.partial(init, ax=ax,point=point,trajectory_line=trajectory_line,ex_radius=ex_radius,center_x=center_x, center_y=center_y)
update_partial = functools.partial(update, point=point, trajectory_line=trajectory_line,radius=radius,center_x=center_x, center_y=center_y)
# 创建动画对象
ani = FuncAnimation(fig, update_partial, frames=np.arange(0, 100, 1),
                    init_func=init_partial, blit=True)

pause_animation_partial = functools.partial(pause_animation,ani=ani)
resume_animation_partial = functools.partial(resume_animation,ani=ani)
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
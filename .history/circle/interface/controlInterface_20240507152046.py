import tkinter as tk
__all__=['root','control_panel', 'bpause', 'bresume']
# 暂停动画的函数
def pause_animation(ani):
    ani.event_source.stop()

# 继续动画的函数
def resume_animation():
    ani.event_source.start()
# 创建 Tkinter 根窗口
root = tk.Tk()
root.title("Matplotlib in Tkinter with Control Panel")

# 设置窗口的最小大小
root.minsize(900, 900)

# 创建控制面板区域
control_panel = tk.Frame(root, width=300, bg='lightgray')
control_panel.pack(side=tk.LEFT, fill=tk.Y)

# 在控制面板中添加按钮
bpause = tk.Button(control_panel, text="pause")
bpause.pack(pady=10)

bresume = tk.Button(control_panel, text="resume")
bresume.pack(pady=10)


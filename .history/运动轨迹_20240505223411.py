import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp
# 定义被积函数
def f(x):
    return 2 * x

# 计算定积分的值
def integral_f(x):
    # 计算定积分的值
    integral_result, _ = quad(f, 0, x)
    # 计算积分曲线上的y值（积分结果在整个区间上是一个常数）
    # integral_y_values = integral_result * np.ones_like(x)
    return integral_result

# 创建等间距的x值数组
x_values = np.arange(0, 100, 0.1)

# 计算对应的y值（原函数）
y_values = f(x_values)


# 使用列表推导式计算每个x值的积分累积值
Jerk = [integral_f(x) for x in x_values]



# 定义符号变量 x
x = sp.Symbol('x')

# 定义被积函数 f(x)
f = 2*x

# 求解不定积分
Jerk = sp.integrate(f, x)
print(f'Jerk(t)={Jerk}')
a = sp.integrate(Jerk, x)
print(f'a(t)={a}')
v = sp.integrate(a, x)
print(f'v(t)={v}')
s = sp.integrate(v, x)
print(f's(t)={v}')

# 绘制原函数曲线和积分线
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='Original Function: $f(x) = 2x$', color='blue')
plt.plot(x_values, integral_y_values, label='Integral from 0 to 100', color='red', linestyle='--')
plt.fill_between(x_values, 0, integral_y_values, alpha=0.2, color='gray')  # 填充积分区域
plt.title('Integral of $f(x) = 2x$ from 0 to 100')
plt.xlabel('x')
plt.ylabel('y and Integral')
plt.legend()
plt.grid(True)
#plt.axis([0, 100, 0, 200])  # 设置坐标轴范围
plt.show()

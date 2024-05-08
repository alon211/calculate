import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy as sp
# 定义被积函数
def f1(x):
    return 2 * x

# 计算定积分的值
def integral_f(x,formula):
    f=eval(formula)
    # 计算定积分的值
    integral_result, _ = quad(f, 0, x)
    # 计算积分曲线上的y值（积分结果在整个区间上是一个常数）
    # integral_y_values = integral_result * np.ones_like(x)
    return integral_result




# 定义符号变量 x
x = sp.Symbol('x')

# 定义被积函数 f(x)
f = 2*x

# 求解不定积分
Jerk_formula = sp.integrate(f, x)
print(f'Jerk(t)={Jerk_formula}')
a_formula = sp.integrate(Jerk_formula, x)
print(f'a(t)={a_formula}')
v_formula = sp.integrate(a_formula, x)
print(f'v(t)={v_formula}')
s_formula = sp.integrate(v_formula, x)
print(f's(t)={s_formula}')


# 创建等间距的x值数组
x_values = np.arange(0, 100, 0.1)

# 计算对应的y值（原函数）
y_values = f1(x_values)


# 使用列表推导式计算每个x值的积分累积值
Jerk = [integral_f(x,'2*x') for x in x_values]
a = [integral_f(x,Jerk_formula) for x in x_values]
v = [integral_f(x,a_formula) for x in x_values]
s = [integral_f(x,v_formula) for x in x_values]


# 绘制原函数曲线和积分线
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label='Original Function: $f(x) = 2x$', color='blue')
plt.plot(x_values, Jerk, label='$a(x) = x**2$', color='red', linestyle='--')
plt.plot(x_values, a, label='$a(x) = x**3/3$', color='green')
plt.plot(x_values, v, label='$v(x) = x**4/12$', color='yellow')
plt.plot(x_values, s, label=f'$s(x) = {s_formula}$', color='black')
plt.fill_between(x_values, 0, Jerk, alpha=0.2, color='gray')  # 填充积分区域
plt.title('Integral of $f(x) = 2x$ from 0 to 100')
plt.xlabel('x')
plt.ylabel('y and Integral')
plt.legend()
plt.grid(True)
#plt.axis([0, 100, 0, 200])  # 设置坐标轴范围
plt.show()


# 需要输入的参数
delta_L_mm=0.0
cycle_time_ms=0.0
Vmax_r_min =0.0
Vset_r_min=0.0
Tset_Acc_ms=0.0
Tset_ms=0.0
Sset_mm=0.0
# 转速单位r/min转换为r/ms,导程单位mm，转速通过导程转为mm/ms
delta_L_mm=6.0 #导程
cycle_time_ms=2  #最短通讯周期
Vmax_r_min =3000.0 #最高转速
Vmax_r_s = Vmax_r_min/60.0
Vmax_r_ms = Vmax_r_s/1000.0
Vmax_mm_ms = Vmax_r_ms*delta_L_mm
deviation_max=2*Vmax_mm_ms #精度最大偏差 2个通讯周期


Vset_r_min=1500.0     #设定转速
Vset_r_s = Vset_r_min/60.0
Vset_r_ms = Vset_r_s/1000.0
Vset_mm_ms = Vset_r_ms*delta_L_mm #设定转速的精度最大偏差 2个通讯周期

Sset_mm=10.0 #设定行程

# 以速度给定方式,加减速相等方式
Tset_Acc_ms=5.0

Tset_AccMax_ms=Sset_mm*2.0/Vset_mm_ms  #根据三角形求出最长加速时间

Tact_Acc_ms=0.0  #实际加减速时间

if Tset_Acc_ms>Tset_AccMax_ms:
  Tact_Acc_ms=Tset_AccMax_ms
else:
  Tact_Acc_ms=Tset_Acc_ms

Tact_Uniform_ms=Tset_Acc_ms-Tact_Acc_ms*2.0  #匀速阶段

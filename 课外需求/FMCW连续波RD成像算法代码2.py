import numpy as np
import matplotlib.pyplot as plt

from 课外需求.FMCW连续波RD成像算法代码 import generate_fmcw_signal, simulate_received_signal, range_doppler_processing, \
    targets

# FMCW雷达系统的基本参数
c = 3e8  # 光速（米/秒）
f0 = 77e9  # 载波频率（赫兹）
B = 200e6  # 带宽（赫兹）
Tchirp = 1e-6  # 调频持续时间（秒）
fs = 2 * B  # 采样频率（赫兹）
PRF = 1e3  # 脉冲重复频率（赫兹）
doppler_resolution = PRF  # 多普勒分辨率（赫兹）

# 定义模拟时间向量（1秒）
# 优化示例：减少信号长度
t = np.arange(0, 0.1, 1/fs)  # 将时间长度减少为0.1秒

# 继续使用相同的信号生成和处理方法
transmitted_signal = generate_fmcw_signal(t, f0, B, Tchirp)
received_signal = simulate_received_signal(targets, transmitted_signal, fs, c)

# 进行范围-多普勒处理
range_estimates, doppler_estimates = range_doppler_processing(transmitted_signal, received_signal, fs, B, Tchirp)

# 绘制图形输出
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(range_estimates, np.abs(np.fft.fft(received_signal)))
plt.title('范围估计')
plt.xlabel('距离 (m)')
plt.ylabel('幅度')

plt.subplot(1, 2, 2)
plt.plot(doppler_estimates, np.abs(np.fft.fft(received_signal)))
plt.title('多普勒估计')
plt.xlabel('多普勒频率 (Hz)')
plt.ylabel('幅度')

plt.tight_layout()
plt.show()

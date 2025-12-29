import numpy as np
import matplotlib.pyplot as plt

# FMCW雷达系统的基本参数
c = 3e8  # 光速（米/秒）
f0 = 77e9  # 载波频率（赫兹）
B = 200e6  # 带宽（赫兹）
Tchirp = 1e-6  # 调频持续时间（秒）
fs = 2 * B  # 采样频率（赫兹）
PRF = 1e3  # 脉冲重复频率（赫兹）
doppler_resolution = PRF  # 多普勒分辨率（赫兹）

# 定义模拟时间向量（1秒）
t = np.arange(0, 1, 1 / fs)

# 模拟目标的距离（单位：米）
targets = np.array([50, 100, 150, 200])


# 生成FMCW信号
def generate_fmcw_signal(t, f0, B, Tchirp):
    # 调频的频率随时间变化
    chirp_slope = B / Tchirp  # 频率变化的斜率
    instantaneous_frequency = f0 + chirp_slope * t  # 瞬时频率
    return np.cos(2 * np.pi * instantaneous_frequency * t)  # 生成调频信号


# 生成发射信号（FMCW信号）
transmitted_signal = generate_fmcw_signal(t, f0, B, Tchirp)


# 模拟接收信号，考虑多个不同的目标
def simulate_received_signal(targets, transmitted_signal, fs, c):
    received_signal = np.zeros_like(transmitted_signal)  # 初始化接收信号
    for target in targets:
        delay = 2 * target / c  # 计算往返延迟
        delay_samples = int(delay * fs)  # 将延迟转换为采样点
        shifted_signal = np.roll(transmitted_signal, delay_samples)  # 按延迟平移信号
        received_signal += shifted_signal  # 将多个目标的信号叠加
    return received_signal


# 计算接收到的信号
received_signal = simulate_received_signal(targets, transmitted_signal, fs, c)


# 执行范围-多普勒处理
def range_doppler_processing(transmitted_signal, received_signal, fs, B, Tchirp):
    # 范围估计（对时间域信号进行FFT）
    range_fft = np.fft.fft(received_signal * np.conj(transmitted_signal), axis=0)
    range_freqs = np.fft.fftfreq(len(range_fft), d=1 / fs)  # 频率轴
    range_estimates = np.abs(range_freqs) * c / (2 * B)  # 范围估计公式

    # 多普勒估计（由目标的运动引起的频率偏移）
    doppler_fft = np.fft.fft(received_signal, axis=0)
    doppler_freqs = np.fft.fftfreq(len(doppler_fft), d=1 / fs)  # 频率轴
    doppler_estimates = doppler_freqs * c / (2 * f0)  # 多普勒估计公式

    return range_estimates, doppler_estimates


# 计算范围和多普勒估计
range_estimates, doppler_estimates = range_doppler_processing(transmitted_signal, received_signal, fs, B, Tchirp)

# 绘制范围-多普勒图像
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.plot(range_estimates, np.abs(range_fft))
plt.title('范围估计')
plt.xlabel('距离 (m)')
plt.ylabel('幅度')

plt.subplot(1, 2, 2)
plt.plot(doppler_estimates, np.abs(doppler_fft))
plt.title('多普勒估计')
plt.xlabel('多普勒频率 (Hz)')
plt.ylabel('幅度')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
data = [2.08, 2.22, 2.71, 2.70, 2.36, 2.24, 2.31, 2.62, 2.68, 2.89, 2.75, 2.79, 2.69, 2.72, 2.76,
        2.98, 3.17, 3.14, 2.70, 2.58, 2.79, 2.91, 2.68, 2.61, 3.77, 16.06, 26.36, 40.19, 64.24, 80.23,
        87.58, 88.73, 87.09, 86.58, 86.33, 85.77, 85.69, 86.15, 85.50, 84.72, 84.72, 84.86, 84.74, 84.70,
        84.36, 84.23, 84.47, 84.74, 84.15, 83.81, 83.88, 85.40, 85.23]

# 時間のデータ（120ms間隔の時間軸）
time = [i * 0.12 for i in range(len(data))]  # 120ms = 0.12秒
filtered_data = [d for d in data if d > 0]
filtered_time = [t for d, t in zip(data, time) if d > 0]

# グラフの描画
plt.figure(figsize=(12, 6))
plt.plot(time, data, linestyle='-', color='b', label='data')

# グラフのタイトルとラベル
plt.xlabel('Time (s)')

# 軸の範囲設定
plt.xlim(min(filtered_time), max(filtered_time))
plt.ylim(min(data) -5, max(data) +5)
plt.grid(True, axis='y')
plt.legend()
plt.show()
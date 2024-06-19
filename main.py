import src.file as fl
import src.draw as dr
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def moving_average(data, window_size):
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        average = sum(window) / window_size
        moving_averages.append(average)
    return moving_averages

file_path = 'docs/track2.csv'
rd = fl.CSVreader(file_path)
odometry_list, ground_truth_list, x_error, y_error, z_error, vector_error, pos_list = rd.get_item()

# ts = rd.get_ts()
# time_series_data = pd.Series(vector_error, index=ts)
# arima_model = ARIMA(time_series_data, order=(1, 1, 1))
# arima_result = arima_model.fit()
# forecast_steps = 10
# arima_forecast = arima_result.forecast(steps=forecast_steps)

draw = dr.Draw()
draw.append('Drone Trajectory', odometry_list)
draw.append('Planning Trajectory' ,ground_truth_list, color='green')
fig = draw.get_fig()

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(range(len(x_error)), x_error, color='r', label='x-error (m)')
ax2.plot(range(len(y_error)), y_error, color='g', label='y-error (m)')
ax2.plot(range(len(z_error)), z_error, color='b', label='z-error (m)')
ax2.set_ylabel('error (m)')
ax2.legend()
ax2.set_ylim(bottom=-0.5, top=1)

total_error:list = []
for i in range(len(x_error)):
    total_error.append(abs(x_error[i]) + abs(y_error[i]) + abs(z_error[i]))

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(range(len(total_error)), total_error, color='g', label='|e_x| + |e_y| + |e_z|')
ax3.plot(range(len(vector_error)), vector_error, color='black', label='Ground-truth error')

for _dt in pos_list:
    format_number = lambda num: int(num) if num % 1 == 0 else round(num, 1)
    num_idx = _dt[0]-2
    if num_idx < 0:
        num_idx = 0
    ax3.annotate(f"\u2022 ({format_number(_dt[1].x)},{format_number(_dt[1].y)},{format_number(_dt[1].z)})", (_dt[0]-5, vector_error[num_idx]), rotation=90, color='r', weight='bold')

ax3.set_ylabel('error (m)')
ax3.legend()
ax3.set_ylim(bottom=-0.5, top=1)

window_size = 10
smoothed_data = moving_average(vector_error, window_size)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(range(len(smoothed_data)), smoothed_data, color='#FF0000', label='Moving Average')
ax4.plot(range(len(vector_error)), vector_error, color='#666666', label='Ground-truth error')
ax4.set_ylabel('error (m)')
ax4.set_ylim(bottom=-0.5, top=1)
ax4.legend()

draw.draw()

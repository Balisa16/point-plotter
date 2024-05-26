import src.file as fl
import src.draw as dr
import numpy as np

file_path = 'docs/track.csv'
rd = fl.CSVreader(file_path)
odometry_list, ground_truth_list, x_error, y_error, z_error, vector_error, pos_list = rd.get_item()

draw = dr.Draw()
draw.append('Drone Trajectory', odometry_list)
draw.append('Planning Trajectory' ,ground_truth_list, color='green')
fig = draw.get_fig()

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(range(len(x_error)), x_error, color='r', label='x-error')
ax2.plot(range(len(y_error)), y_error, color='g', label='y-error')
ax2.plot(range(len(z_error)), z_error, color='b', label='z-error')
ax2.set_xlabel('index')
ax2.set_ylabel('x-error (m)')
ax2.legend()
ax2.set_ylim(bottom=-1, top=1)

total_error:list = []
for i in range(len(x_error)):
    total_error.append(abs(x_error[i]) + abs(y_error[i]) + abs(z_error[i]))

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(range(len(total_error)), total_error, color='g', label='|x| + |y| + |z|')
ax3.plot(range(len(vector_error)), vector_error, color='black', label='ground-truth error')

for index, (position_index, _) in enumerate(pos_list):
    ax3.text(position_index, vector_error[index], '\u2022', fontdict=dict(color='r', weight='bold'), va='center')


ax3.set_ylabel('')
ax3.legend()
ax3.set_ylim(bottom=-1, top=1)

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(range(len(z_error)), z_error, color='g')
ax4.set_xlabel('index')
ax4.set_ylabel('z-error (m)')
ax4.set_ylim(bottom=-1, top=1)

draw.draw()

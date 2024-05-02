import src.file as fl
import src.draw as dr

file_path = 'docs/track.csv'
rd = fl.CSVreader(file_path)
odometry_list, ground_truth_list = rd.get_item()
draw = dr.Draw()
draw.append('Drone Trajectory', odometry_list)
draw.append('Planning Trajectory' ,ground_truth_list, color='green')
draw.draw()

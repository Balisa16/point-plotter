import src.file as fl
import src.draw as dr

file_path = 'docs/Track-2.csv'
rd = fl.CSVreader(file_path)
ts, x, y, z, qw, qx, qy, qz = rd.get_item()
draw = dr.Draw(ts, x, y, z, qw, qx, qy, qz)
draw.draw()

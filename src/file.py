import csv

class PosOrient:
    def __init__(self, ts, x, y, z, qw, qx, qy, qz):
        self.ts = ts
        self.x = x
        self.y = y
        self.z = z
        self.qw = qw
        self.qx = qx
        self.qy = qy
        self.qz = qz

class CSVreader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.header = "None"
        try:
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                
                # Read and print headers
                self.header = next(csv_reader)
                
                # Read and print data
                for row in csv_reader:
                    self.data.append(row)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_data(self):
        return self.data
    
    def get_header(self):
        return self.header

    def get_item(self):
        ts = []
        x = []
        y = []
        z = []
        # qw = []
        # qx = []
        # qy = []
        # qz = []
        for row in self.data:
            ts.append(row[3])
            x.append(float(row[4]))
            y.append(float(row[5]))
            z.append(float(row[6]))
            # qw.append(row[7])
            # qx.append(row[8])
            # qy.append(row[9])
            # qz.append(row[10])
        return ts, x, y, z
    def get_pos_orient(self):
        ret_val = []
        for row in self.data:
            ret_val.append(PosOrient(
                            float(row[3]),
                            float(row[4]),
                            float(row[5]),
                            float(row[6]),
                            float(row[7]),
                            float(row[8]),
                            float(row[9]),
                            float(row[10])))
        return ret_val

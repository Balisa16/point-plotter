import csv

def read_and_print_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            
            # Read and print headers
            headers = next(csv_reader)
            print("Headers:", headers)
            
            # Read and print data
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

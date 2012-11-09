'''
Created on Nov 9, 2012

@author: Ash
'''

def read_data(file_name, header):
    f = open(file_name)
    if header: f.readline()  # ignore header
    samples = []
    for line in f:
        line = line.strip().split(",")
        samples.append(line)
    return samples

def write_delimited_file(file_path, data, header=None, delimiter=","):
    f_out = open(file_path, "w")
    if header is not None:
        f_out.write(delimiter.join(header) + "\n")
    for line in data:
        if isinstance(line, str):
            f_out.write(line + "\n")
        else:
            f_out.write(delimiter.join(line) + "\n")
    f_out.close()
 

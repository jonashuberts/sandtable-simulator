# utils.py

import math
import os
from constants import *

# Function to convert theta-rho to Cartesian coordinates
def polar_to_cartesian(theta, rho):
    x = rho * math.cos(theta)
    y = rho * math.sin(theta)
    return (x, y)

# Read theta-rho coordinates from a file
def read_coordinates(filename):
    coordinates = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) >= 2:
                    theta = float(parts[0])
                    rho = float(parts[1])
                    coordinates.append((theta, rho))
    except IOError:
        print(f"Error reading file: {filename}")
    return coordinates

# Function to get a list of input files in the specified folder
def get_input_files(folder):
    files = []
    for filename in os.listdir(folder):
        if filename.endswith('.thr'):
            files.append(os.path.join(folder, filename))
    return files

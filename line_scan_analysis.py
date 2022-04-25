import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import os
import glob
import csv

# each spreadsheet is a different cell that we analyzed
# get the directory where you have the cells
user_input = input('Enter a directory containing your plot profiles \n')
print(f'Accessing {user_input}')
assert os.path.exists(user_input), "I did not find the directory at, "+str(user_input)

# find all the spreadsheets to go through


for root, dirs, files in os.walk(user_input):
    for name in files:
        if (name.startswith('Scene')) and (os.path.splitext(name)[-1]=='.csv'):
            # read in a spreadsheet
            with open(user_input, 'r') as csv_file:
                csvreader = csv.reader(csv_file)




# calculate the percent distance and percent gray value

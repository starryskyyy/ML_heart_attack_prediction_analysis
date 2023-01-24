# importing libraries
import numpy as np
import pandas as pd

# reading both csv files and display 5 first rows to make sure that data imported correctly
heart = pd.read_csv('heart.csv')
print(heart.head())

o2Saturation = pd.read_csv('o2Saturation.csv')
print(o2Saturation.head())


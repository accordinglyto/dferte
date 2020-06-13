from numpy import genfromtxt
import matplotlib.pyplot as plt
import mpl_finance
import numpy as np
import uuid
import os

# Input your csv file here with historical data



buy_dir = '../data/train/buy/'
sell_dir = '../data/train/sell/'

val_num = 370
train_num = 1295

for i in range(0,val_num):
 files = os.listdir("../data/train/sell")
 os.rename("../data/train/sell/"+files[i], "../data/validation/sell/"+files[i])

files = os.listdir("../data/train/sell")
n_files = len(files)
for i in range(0,n_files-train_num):
 os.remove(sell_dir + files[i])

for i in range(0,val_num):
 files = os.listdir("../data/train/buy")
 os.rename("../data/train/buy/"+files[i], "../data/validation/buy/"+files[i])

files = os.listdir("../data/train/buy")
n_files = len(files)
for i in range(0,n_files-train_num):
 os.remove(buy_dir + files[i])

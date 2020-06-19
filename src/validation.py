from numpy import genfromtxt
import matplotlib.pyplot as plt
import mpl_finance
import numpy as np
import uuid
import os

# Input your csv file here with historical data


buy_dir = "../data/train/buy/"
sell_dir = "../data/train/sell/"

val_num = 370
train_num = 0

# for i in range(0,val_num):
#  files = os.listdir("../data/train/sell")
#  os.rename("../data/train/sell/"+files[i], "../data/validation/sell/"+files[i])

s_files = os.listdir("../data/train/sell")
s_n_files = len(s_files)
b_files = os.listdir("../data/train/buy")
b_n_files = len(b_files)

if b_n_files < s_n_files:
    train_num = b_n_files

    for i in range(0, s_n_files - train_num):
        os.remove(sell_dir + s_files[i])

elif b_n_files > s_n_files:
    train_num = s_n_files
    for i in range(0, b_n_files - train_num):
        os.remove(buy_dir + b_files[i])


# for i in range(0,val_num):
#  files = os.listdir("../data/train/buy")
#  os.rename("../data/train/buy/"+files[i], "../data/validation/buy/"+files[i])

# files = os.listdir("../data/train/buy")
# n_files = len(files)


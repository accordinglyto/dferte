from numpy import genfromtxt
import matplotlib.pyplot as plt
import mpl_finance
import numpy as np
import uuid
import matplotlib

# Input your csv file here with historical data

ad = genfromtxt("../financial_data/BPI-copy.csv", delimiter=",", dtype=str)
pd = ad

buy_dir = "../data/train/buy/"
sell_dir = "../data/train/sell/"


def convolve_sma(array, period):
    return np.convolve(array, np.ones((period,)) / period, mode="valid")


def graphwerk(start, finish):
    open = []
    high = []
    low = []
    close = []
    volume = []
    decision = []
    date = []
    for x in range(finish - start):

        # Below filtering is valid for eurusd.csv file. Other financial data files have different orders so you need to find out
        # what means open, high and close in their respective order.
        open.append(float(pd[start][1]))
        high.append(float(pd[start][2]))
        low.append(float(pd[start][3]))
        close.append(float(pd[start][4]))
        volume.append(float(pd[start][5]))
        decision.append(str(pd[start][6]))
        date.append(pd[start][0])

        start = start + 1
    close_next = float(pd[finish][4])

    # sma = convolve_sma(close, 5)
    # smb = list(sma)
    # diff = sma[-1] - sma[-2]

    # for x in range(len(close)-len(smb)):
    # smb.append(smb[-1]+diff)

    fig = plt.figure(num=1, figsize=(1, 1), dpi=50, facecolor="w", edgecolor="k")
    # fig2 = plt.figure(num=1, figsize=(1, 1), dpi=50, facecolor='w', edgecolor='k')

    dx = fig.add_subplot(111)
    # dx.axis("off")

    # dx2 = fig.add_subplot(414)
    # dx2.axis("off")

    mpl_finance.candlestick2_ochl(
        dx, open, close, high, low, width=1.5, colorup="g", colordown="r", alpha=0.5
    )

    # pad = 0.60
    # yl = dx.get_ylim()
    # print(yl)
    # dx.set_ylim(yl[0]-(yl[1]-yl[0])*pad,yl[1])
    # print(dx.get_ylim())

    # mpl_finance.volume_overlay(dx2, open, close, volume, width=0.4, alpha=1)

    plt.autoscale()
    # plt.plot(smb, color="blue", linewidth=10, alpha=0.5)
    plt.axis("off")

    comp_ratio = close_next / close[-1]
    print(comp_ratio)
    if decision[-1] == "sell":
        print("previous value is bigger")
        print("last value: " + str(close[-1]))
        print("next value: " + str(close_next))
        print("sell")
        plt.savefig(sell_dir + str(uuid.uuid4()) + ".jpg", bbox_inches="tight")
    else:
        print("previous value is smaller")
        print("last value: " + str(close[-1]))
        print("next value: " + str(close_next))
        print("buy")
        plt.savefig(buy_dir + str(uuid.uuid4()) + ".jpg", bbox_inches="tight")
    # if close[-1] >= close_next:
    #         print('previous value is bigger')
    #         print('last value: ' + str(close[-1]))
    #         print('next value: ' + str(close_next))
    #         print('sell')
    #         plt.savefig(sell_dir + str(uuid.uuid4()) +'.jpg', bbox_inches='tight')
    # else:
    #         print('previous value is smaller')
    #         print('last value: '+ str(close[-1]))
    #         print('next value: ' + str(close_next))
    #         print('buy')
    #         plt.savefig(buy_dir + str(uuid.uuid4())+'.jpg', bbox_inches='tight')

    # plt.show()
    open.clear()
    close.clear()
    volume.clear()
    high.clear()
    low.clear()
    plt.cla()
    plt.clf()


iter_count = int(len(pd))
print(iter_count)
iter = 0


for x in range(len(pd)):  # (len(pd)-4):
    graphwerk(iter, iter + 1)
    iter = iter + 1

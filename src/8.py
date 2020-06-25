from numpy import genfromtxt
import matplotlib.pyplot as plt
import mpl_finance
import numpy as np
import uuid
import matplotlib

# Input your csv file here with historical data

ad = genfromtxt(f"../financial_data/BPI.csv", delimiter=",", dtype=str)


def convolve_sma(array, period):
    return np.convolve(array, np.ones((period,)) / period, mode="valid")


def graphwerk(start, finish):
    open = []
    high = []
    low = []
    close = []
    volume = []
    # decision = []
    date = []

    c_open = []
    c_high = []
    c_low = []
    c_close = []
    c_volume = []
    c_date = []
    c_start = start + 18

    for x in range(finish - start - 6):
        c_open.append(float(pd[c_start][1]))
        c_high.append(float(pd[c_start][2]))
        c_low.append(float(pd[c_start][3]))
        c_close.append(float(pd[c_start][4]))
        c_volume.append(float(pd[c_start][5]))
        c_date.append(pd[c_start][0])
        c_start = c_start + 1

    for x in range(finish - start):

        # Below filtering is valid for eurusd.csv file. Other financial data files have different orders so you need to find out
        # what means open, high and close in their respective order.
        open.append(float(pd[start][1]))
        high.append(float(pd[start][2]))
        low.append(float(pd[start][3]))
        close.append(float(pd[start][4]))
        volume.append(float(pd[start][5]))
        # decision.append(str(pd[start][6]))
        date.append(pd[start][0])

        start = start + 1

    decision = "sell"
    min_forecast = min(c_low)
    max_forecast = max(c_high)

    if close[-1] * 1.03 < max_forecast:
        decision = "buy"
    # for z in all_prices:
    # if close[-1] * 1.03 < z:
    #     decision = "buy"

    sma = convolve_sma(close, 5)
    smb = list(sma)
    diff = sma[-1] - sma[-2]

    for x in range(len(close) - len(smb)):
        smb.append(smb[-1] + diff)

    fig = plt.figure(num=1, figsize=(3, 3), dpi=50, facecolor="w", edgecolor="k")
    dx = fig.add_subplot(111)
    # mpl_finance.volume_overlay(ax, open, close, volume, width=0.4, colorup='b', colordown='b', alpha=1)
    mpl_finance.candlestick2_ochl(
        dx, open, close, high, low, width=1.5, colorup="g", colordown="r", alpha=0.5
    )
    plt.autoscale()
    # plt.plot(smb, color="blue", linewidth=10, alpha=0.5)
    plt.axis("off")

    if decision == "sell":
        print("last value: " + str(close[-1]))
        print(
            "range of values in next 13 bars: "
            + str(min_forecast)
            + "-"
            + str(max_forecast)
        )
        print("sell")
        plt.savefig(sell_dir + str(uuid.uuid4()) + ".jpg", bbox_inches="tight")
    else:
        print("last value: " + str(close[-1]))
        print(
            "range of values in next 13 bars: "
            + str(min_forecast)
            + "-"
            + str(max_forecast)
        )
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


# output = []
# with open("STOCKbluechip.csv") as f:
#     output = [str(s) for line in f.readlines() for s in line[:-1].split(",")]

# for stock in output:

pd = ad

buy_dir = "../data/train/buy/"
sell_dir = "../data/train/sell/"

iter = 0

for x in range(len(pd)):
    graphwerk(iter, iter + 18)
    iter = iter + 2

from helper import formatday, formatdatetime

import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

xtick_locator = AutoDateLocator()
xtick_formatter = AutoDateFormatter(xtick_locator)

# Plot settings
plt.figure(figsize=(14,8))

def year_messages_plot(dailymessagecounts):
    # df = pd.DataFrame(dailymessagecounts)

    num_days = len(dailymessagecounts)
    x = range(num_days)
    datelabels = []

    p1key = list(dailymessagecounts[0].keys())[0]
    p2key = list(dailymessagecounts[0].keys())[1]
    p1_counts = []
    p2_counts = []

    for i in range(num_days):
        datelabels.append(formatdatetime(i))

        countsobj = dailymessagecounts[i]
        p1_counts.append(countsobj[p1key])
        p2_counts.append(countsobj[p2key])


    ax = plt.axes()
    ax.xaxis.set_major_locator(xtick_locator)
    ax.xaxis.set_major_formatter(xtick_formatter)

    # plt.plot(datelabels, p1_counts, label = p1key)
    plt.plot(datelabels, p2_counts, label = p2key)
    plt.plot(datelabels, p1_counts, label = p1key, alpha = 0.75)

    plt.xlabel("Dates from Mar 26, 2019 - Mar 26, 2020")
    plt.ylabel("Messages sent (including photos, emojis, stickers, etc)")

    plt.title("Messages over the last year")

    plt.legend()

    plt.show()

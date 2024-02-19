
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]

viewers =  [63693, 28270, 17845, 12544, 11632, 9756, 9192, 5176, 4750, 3847]

plt.figure()
ax = plt.subplot()
plt.bar(range(len(viewers)), viewers, color='purple')
ax.set_xticks(range(10))
ax.set_xticklabels(games, rotation=30)
plt.title('Games Viewers')
plt.xlabel('Games')
plt.ylabel('Views')
plt.savefig('games_viewers.png')
plt.show()
plt.clf()

# Pie Chart: League of Legends Viewers' Whereabouts

labels = ["US", "CA", "DE", "N/A", "GB", "TR", "BR", "AU", "SE", "NL", "Others"]

countries = [28109, 4323, 3642, 2589, 2318, 1449, 1297, 1180, 1062, 956, 16752]

colors = ['lightskyblue', 'gold', 'lightcoral', 'gainsboro', 'royalblue',
          'lightpink', 'darkseagreen', 'sienna', 'khaki', 'gold', 'violet',
          'yellowgreen']

plt.figure()
plt.pie(countries,
        labels=labels,
        colors=colors,
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        shadow=True,
        startangle=345,
        autopct='%1.0f%%',
        pctdistance=1.35
)
plt.axis('equal')
plt.title('Viewers countries')
plt.savefig('countries_viewers.png')
plt.show()
plt.clf()

# Line Graph: Time Series Analysis

hour = range(24)

viewers_hour = [30, 17, 34, 29, 19, 14, 3, 2, 4, 9, 5, 48, 62, 58, 40, 51, 69, 55, 76, 81, 102, 120, 71, 63]
y_upper = [round(x*1.15,2) for x in viewers_hour]
y_lower = [round(x*0.85,2) for x in viewers_hour]

plt.figure()
ax = plt.subplot()
plt.plot(hour, viewers_hour)
plt.fill_between(hour, y_upper, y_lower, alpha=0.2)
ax.set_xticks(range(24))
plt.legend(['2015-01-01'], loc=4)
plt.title("Time Series")
plt.xlabel("Hour")
plt.ylabel("Viewers")
plt.savefig('time_series.png')
plt.show()
plt.clf()

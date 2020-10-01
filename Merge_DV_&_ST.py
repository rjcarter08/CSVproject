import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

highs = []
dates = [] 
lows = [] 

for row in csv_file: 
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)




x = datetime.strptime('2018-07-01', '%Y-%m-%d')


import matplotlib.pyplot as plt


open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file2, delimiter=",")

header_row2 = next(csv_file)

highs2 = []
dates2 = [] 
lows2 = [] 

for row in csv_file:
    try:
        high2 = int(row[4]) 
        low2 = int(row[5]) 
        current_date2 = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError: 
        print(f"Missing data for {current_date2}")
    else:   
        highs2.append(high2)
        lows2.append(low2)
        dates2.append(current_date2)



x2 = datetime.strptime('2018-07-01', '%Y-%m-%d')

import matplotlib.pyplot as plt
fig, axs = plt.subplots(2) 
fig.suptitle('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US', fontsize=10)
fig.autofmt_xdate()
axs[0].plot(dates, highs, c="red", alpha=0.5)
axs[0].plot(dates, lows, c="blue", alpha=0.5)
axs[0].fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
axs[0].title.set_text('SITKA AIRPORT, AK US')
axs[0].xaxis.set_ticklabels([])
axs[1].plot(dates2, highs2, c="red", alpha=0.5)
axs[1].plot(dates2, lows2,c="blue", alpha=0.5)
axs[1].fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
axs[1].title.set_text('DEATH VALLEY, CA US')



plt.show()



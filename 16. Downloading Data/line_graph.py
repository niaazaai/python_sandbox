from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('./16. Downloading Data/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()
   
reader = csv.reader(lines)
header_row = next(reader)

# Extract high and low temperatures.
highs = []
lows = []
for row in reader:
    high = int(row[4])
    highs.append(high)
    lows.append(int(row[5]))



# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

from pathlib import Path
import csv

path = Path('./16. Downloading Data/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()


for rows in lines: 
    print(f":::> {rows}")


reader = csv.reader(lines)
header_row = next(reader)
print(header_row)


for index, column_header in enumerate(header_row):
    print(index, column_header)
    


# Extract high and low temperatures.
highs = []
lows = []
for row in reader:
    high = int(row[4])
    highs.append(high)
    lows.append(int(row[5]))

print(highs)
print(lows)


hours_1 = abs(int(input()))
minutes_1 = abs(int(input()))
seconds_1 = abs(int(input()))
hours_2 = abs(int(input()))
minutes_2 = abs(int(input()))
seconds_2 = abs(int(input()))
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
      - hours_1 * 3600 - minutes_1 * 60 - seconds_1)
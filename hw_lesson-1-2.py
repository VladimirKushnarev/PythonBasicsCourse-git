time_in_sec = int(input('Write time in seconds: '))

hours = time_in_sec // 3600
minutes = time_in_sec // 60 - hours * 60
seconds = time_in_sec % 60

print('Time {:02d} : {:02d} : {:02d}'.format(hours, minutes, seconds))

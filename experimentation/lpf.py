import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

def avg(l):
	return sum(l)/len(l)

time = []
data = []

with open(file_path) as csvfile:
	file = csv.reader(csvfile)

	for i in range(26):
		next(file)

	num_chans = int(len(next(file))/2)

	for row in file:
		row_times = []
		row_data = []
		for i in range(num_chans):
			row_times.append(float(row[2*i]))
			row_data.append(float(row[2*i+1]))
		time.append(row_times)
		data.append(row_data)

data = list(zip(*data))

window = 1
smoothed = []

for col in range(num_chans):
	chan_smoothed = []
	for i in range(window, len(data[0])-window, 1):
		chan_smoothed.append(avg(data[col][int(i-window/2):int(i+window/2)]))
	smoothed.append(chan_smoothed)

for i in range(num_chans):
	plt.plot(time[0:len(smoothed[i])], smoothed[i])
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Oscilliscope reading smoothed with window of "+str(window))
plt.show()
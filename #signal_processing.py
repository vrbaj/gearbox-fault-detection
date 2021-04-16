import padasip
import numpy as np
import os
from matplotlib import pyplot as plt

gearbox_load = "30"
fault_file_name = os.path.join("BrokenTooth Data", "b30hz" + gearbox_load + ".txt")
fault_dataset = np.loadtxt(fault_file_name)

healthy_file_name = os.path.join("Healthy Data", "h30hz" + gearbox_load + ".txt")
healthy_dataset = np.loadtxt(healthy_file_name)

data_series = fault_dataset

print("dataset shape: ", data_series.shape)
dataset_len = data_series.shape[0]
filter_len = 10
d = np.zeros(dataset_len - filter_len)
x = np.zeros((dataset_len - filter_len, filter_len))

data_series = padasip.standardize(data_series[:, 3])
for idx, sample in enumerate(data_series[filter_len:]):
    if True:
        d[idx] = sample
        for i in range(filter_len):
            x[idx, i] = data_series[idx + filter_len - i - 1]

adaptive_filter = padasip.filters.FilterNLMS(n=filter_len, mu=0.8, w="random")
y, e, w = adaptive_filter.run(d, x)

print("error std: ", np.std(e))
print("error mean:", np.mean(np.abs(e)))

plt.figure(0)
plt.title("error")
plt.plot(e)
plt.figure(1)
plt.title("data")
plt.plot(y)
plt.figure(2)
plt.title("original series")
plt.plot(data_series[filter_len:])
plt.show()


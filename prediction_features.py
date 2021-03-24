import padasip
import numpy as np
import os
from matplotlib import pyplot as plt

gearbox_load = ["0", "10", "20", "30", "40", "50", "60", "70", "80", "90"]
filter_len = 10
results = {"faulty error mean": [],
           "healthy error mean": [],
           "faulty error std": [],
           "healthy error std": []}

for item in gearbox_load:
    print(item)
    fault_file_name = os.path.join("BrokenTooth Data", "b30hz" + item + ".txt")
    fault_dataset = np.loadtxt(fault_file_name)

    healthy_file_name = os.path.join("Healthy Data", "h30hz" + item + ".txt")
    healthy_dataset = np.loadtxt(healthy_file_name)

    data_series = [fault_dataset, healthy_dataset]
    ser = 0
    for series in data_series:
        dataset_len = series.shape[0]
        print("dataset: ",item, " lenght>", dataset_len)
        d = np.zeros(dataset_len - filter_len)
        x = np.zeros((dataset_len - filter_len, filter_len))
        series = padasip.standardize(series[:, 0])
        for idx, sample in enumerate(series[filter_len:]):
            if True:
                d[idx] = sample
                for i in range(filter_len):
                    x[idx, i] = series[idx + filter_len - i - 1]

        adaptive_filter = padasip.filters.FilterNLMS(n=filter_len, mu=0.8, w="random")
        y, e, w = adaptive_filter.run(d, x)
        if ser == 0:
            # fault
            results["faulty error mean"].append(np.mean(np.abs(e)))
            results["faulty error std"].append(np.std(np.abs(e)))
        else:
            results["healthy error mean"].append(np.mean(np.abs(e)))
            results["healthy error std"].append(np.std(np.abs(e)))
        ser += 1
print(results)
plt.figure(0)
plt.title("mean(|e|)")
plt.plot(results["healthy error mean"], "k+")
plt.plot(results["faulty error mean"], "r+")

plt.figure(1)
plt.title("stdev|e|")
plt.plot(results["healthy error std"], "k+")
plt.plot(results["faulty error std"], "r+")
plt.show()
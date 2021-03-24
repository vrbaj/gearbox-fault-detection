from matplotlib import pyplot as plt
import numpy as np
import os


gearbox_load = "60"
fault_file_name = os.path.join("BrokenTooth Data", "b30hz" + gearbox_load + ".txt")
fault_dataset = np.loadtxt(fault_file_name)
print("dataset shape: ", fault_dataset.shape)

healthy_file_name = os.path.join("Healthy Data", "h30hz" + gearbox_load + ".txt")
healthy_dataset = np.loadtxt(healthy_file_name)
for i in range(4):
    print("max healthy: ", max(healthy_dataset[:, i]))
    print("max fault: ", max(fault_dataset[:, i]))
    print("avg healthy: ", np.average(healthy_dataset[:, i]))
    print("avg fault: ", np.average(fault_dataset[:, i]))
    print("std dev healthy: ", np.std(healthy_dataset[:, i]))
    print("std dev fault: ", np.std(fault_dataset[:, i]))

plt.figure(1)
plt.plot(fault_dataset[:, 0])
plt.title("Faulty")

plt.figure(2)
plt.title("Healthy")
plt.plot(healthy_dataset[:, 0])
plt.show()



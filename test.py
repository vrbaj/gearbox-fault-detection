import os

import numpy as np
from matplotlib import pyplot as plt
import emd

FIGURE_FOLDER = "figs"

# EMD
file_name = "dataset/healthy-50-40.csv"
data = np.loadtxt(file_name, delimiter=",")

u = data[:, 1]
imf = emd.sift.sift(u)

emd.plotting.plot_imfs(imf, scale_y=True, cmap=True)
plt.tight_layout()

filepath = os.path.join(FIGURE_FOLDER, "emd_imfs.png" )
plt.savefig(filepath)
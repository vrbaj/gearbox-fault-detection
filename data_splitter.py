"""
This file create new dataset from the old one.

It splits the files into shorter segments and store them in flat directory
"""

import os, glob

import numpy as np


SEGMENT_SIZE = 1000
SOURCE_PATHS = ["BrokenTooth Data", "Healthy Data"]
OUTPUT_PATH = "dataset"


all_paths = []
for source_path in SOURCE_PATHS:
    all_paths += list(glob.glob(os.path.join(source_path, "*.txt")))

for target_path in all_paths:
    b_diagnose, name = os.path.split(target_path)
    b_load = name.split("hz")[1].split(".")[0]

    datapack = np.loadtxt(target_path)

    for n in range(SEGMENT_SIZE, datapack.shape[0], SEGMENT_SIZE):
        data = datapack[n-SEGMENT_SIZE:n]

        filename = "{}-{}-{}.csv".format(
            "broken" if "Broken" in b_diagnose else "healthy",
            b_load,
            n // SEGMENT_SIZE
        )

        file_path = os.path.join(OUTPUT_PATH, filename)

        np.savetxt(file_path, data, delimiter=",")










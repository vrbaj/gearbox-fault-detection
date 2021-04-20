"""
https://link.springer.com/content/pdf/10.1007/BF03027572.pdf

https://gitlab.com/emd-dev/emd/-/blob/master/emd/plotting.py


Times: {'AF': 47.50602674484253, 'EMD': 77.6480393409729}
"""

import os, glob
import time
import random

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import padasip as pa
import emd


def measure_time(func):

    def inner(*args, label="NO", **kwargs):
        if not label in measure_time.store:
            measure_time.store[label] = 0

        t0 = time.time()
        out = func(*args, **kwargs)
        measure_time.store[label] += time.time() - t0

        return out

    return inner

@measure_time
def process_dummy(data):
    return np.random.random()

@measure_time
def process_padasip_e(data, n, mu):
    out = []
    for column in range(0,4):
        u = data[:, column]
        x = pa.input_from_history(u, n)[:-1]
        d = u[n:]
        f = pa.filters.FilterNLMS(n=n, mu=mu, w="zeros")
        y, e, w = f.run(d, x)
        out.append(abs(e).mean())
    return out


@measure_time
def process_emd(data):
    out = []
    for column in range(0,4):
        u = data[:, column]
        imf = emd.sift.sift(u)
        # IP, IF, IA = emd.spectra.frequency_transform(imf, 100, 'hilbert')
        # means = IA.mean(axis=0) # TODO: co skutecne je to IA?
        means = abs(imf).mean(axis=0)
        out.append(means[0])
    return out


measure_time.store = {}



DATASET_PATH = "dataset"
RESULT_NAME = "results1.csv"

file_names = list(glob.glob(os.path.join(DATASET_PATH, "*.csv")))

# determine count limit
class_names = ["-".join(os.path.split(name)[-1].split("-")[0:2]) for name in file_names]
data_summary = {key: class_names.count(key) for key in set(class_names)}
limit_count = min(data_summary.values())

# real run with limit
real_file_names = [fn for fn in file_names if limit_count >= int(os.path.split(fn)[-1].split("-")[-1].split(".")[0])]
random.shuffle(real_file_names)

results_data = pd.DataFrame(columns=["class", "loading", "number"])


for file_name in real_file_names[:]:
    label = os.path.split(file_name)[-1].split(".")[0]
    out_class, out_loading, out_number = label.split("-")
    data = np.loadtxt(file_name, delimiter=",")


    af_result = process_padasip_e(data, 10, 0.5, label="AF")
    emd_result = process_emd(data, label="EMD")

    results_data = results_data.append({
        "class": out_class,
        "loading": out_loading,
        "number": out_number,
        "result_AF_1": af_result[0],
        "result_AF_2": af_result[1],
        "result_AF_3": af_result[2],
        "result_AF_4": af_result[3],
        "result_EMD_1": emd_result[0],
        "result_EMD_2": emd_result[1],
        "result_EMD_3": emd_result[2],
        "result_EMD_4": emd_result[3],
    }, ignore_index=True)


results_data.to_csv(RESULT_NAME, index=False)

print(measure_time.store)












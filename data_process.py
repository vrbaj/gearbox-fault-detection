"""

"""

import os, glob

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

DATASET_PATH = "dataset"
RESULT_NAME = "results1.csv"

file_names = list(glob.glob(os.path.join(DATASET_PATH, "*.csv")))

# determine count limit
class_names = ["-".join(os.path.split(name)[-1].split("-")[0:2]) for name in file_names]
data_summary = {key: class_names.count(key) for key in set(class_names)}
limit_count = min(data_summary.values())

# real run with limit
real_file_names = [fn for fn in file_names if limit_count >= int(os.path.split(fn)[-1].split("-")[-1].split(".")[0])]

results_data = pd.DataFrame(columns=["class", "loading", "number", "result"])


for file_name in real_file_names[:]:
    label = os.path.split(file_name)[-1].split(".")[0]
    out_class, out_loading, out_number = label.split("-")

    result = np.random.random() # TODO your function here!

    results_data = results_data.append({
        "class": out_class,
        "loading": out_loading,
        "number": out_number,
        "result": result,
    }, ignore_index=True)


results_data.to_csv(RESULT_NAME, index=False)












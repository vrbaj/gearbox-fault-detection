import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import svm


RESULT_NAME = "results1.csv"
FIGURE_FOLDER = "figs"

data = pd.read_csv(RESULT_NAME)


test_sets = [
    [1, 2, 3, 4],
    [2, 3, 4],
    [3, 4],
    [4],
    [3],
    [2],
    [1]
]

### TOTAL TEST
# y = data["class"].values
# for test in test_sets:
#     print()
#     print(test)
#     algs = ["AF", "EMD"]
#     for alg in algs:
#         cols = ["result_{}_{}".format(alg, ch) for ch in test]
#         x = data[cols].values
#         clf = svm.SVC(kernel='linear', C=1)
#         clf.fit(x, y)
#         match = clf.predict(x) == y
#         print(alg, list(match).count(False))

### CROSSVAL
table_content = ""

for test in test_sets:
    print()
    print(test)
    algs = ["AF", "EMD"]

    table_row_data = {
        "channels": ", ".join(map(str, test)),
    }

    for alg in algs:
        cols = ["result_{}_{}".format(alg, ch) for ch in test]

        n_folds = 10
        step = len(data) // n_folds
        errors = []
        for fold in range(0, n_folds):
            test_start = fold * step
            test_end = (fold + 1) * step
            test_content = range(test_start, test_end)
            data_train = data.loc[~data.index.isin(test_content)]
            data_test = data.loc[data.index.isin(test_content)]

            x = data_train[cols].values
            y = data_train["class"].values
            clf = svm.SVC(kernel='linear', C=1)
            clf.fit(x, y)

            x = data_test[cols].values
            y = data_test["class"].values
            match = clf.predict(x) == y
            errors.append(list(match).count(False))

        accuracy = (len(data) - sum(errors)) / len(data) * 100
        accuracy =  np.round(accuracy, 3)
        table_row_data[alg] = accuracy
        # print(alg, accuracy)

    table_content += r"{} & {} & {}\\".format(
        table_row_data["channels"],
        table_row_data["AF"],
        table_row_data["EMD"],
    ) + "\n"



TABLE_PREF = r"""\begin{table}[]
\begin{tabular}{c|c|c}
\hline
\textbf{}                                                               & \multicolumn{2}{c}{\textbf{Classification accuracy {[}\%{]}}}                                                                                                      \\ \cline{2-3} 
\textbf{\begin{tabular}[c]{@{}c@{}}Sensors\\ (SVM inputs)\end{tabular}} & \textbf{\begin{tabular}[c]{@{}c@{}}Proposed method\\ (NLMS error)\end{tabular}} & \textbf{\begin{tabular}[c]{@{}c@{}}Reference method\\ (EMD - IMF 1)\end{tabular}} \\ \hline
"""

TABLE_END = r"""\hline \end{tabular}
\end{table}
"""

table = TABLE_PREF + "\n" + table_content + "\n" + TABLE_END

print(table)




# y = data["class"].values


# for test in test_sets:
#     print()
#     print(test)
#     algs = ["AF", "EMD"]
#     for alg in algs:
#         cols = ["result_{}_{}".format(alg, ch) for ch in test]
#         x = data[cols].values
#         clf = svm.SVC(kernel='linear', C=1)
#         clf.fit(x, y)
#         match = clf.predict(x) == y
#         print(alg, list(match).count(False))







# print(clf.support_vectors_)
# idx = [0, 1]
# w = clf.coef_[0]
# a = -w[idx[0]] / w[idx[1]]
# xx = np.linspace(x[:,0].min(), x[:,0].max())
# yy = a * xx - (clf.intercept_[0]) / w[idx[1]]
# print(w)
# # plt.plot(xx, yy)
# plt.scatter(x[:,0], x[:,1])
# plt.show()





# metric = "result_EMD_1"
# for title in data["loading"].unique():
#
#     subdata = data[data["loading"]==title]
#     col = "class"
#     labels = subdata[col].unique()
#     groupings = [subdata[subdata[col]==label][metric].values for label in labels]
#
#     plt.boxplot(groupings, labels=labels)
#     plt.title(title)
#     plt.show()




# subdata = data
# col = "class"
#
# plt.subplot("121")
# metric = "result_AF_1"
# labels = subdata[col].unique()
# groupings = [subdata[subdata[col]==label][metric].values for label in labels]
# plt.boxplot(groupings, labels=labels)
# plt.title(metric)
#
# plt.subplot("122")
# metric = "result_EMD_1"
# labels = subdata[col].unique()
# groupings = [subdata[subdata[col]==label][metric].values for label in labels]
# plt.boxplot(groupings, labels=labels)
# plt.title(metric)
#
#
# plt.show()
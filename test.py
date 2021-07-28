import os

import numpy as np
from matplotlib import pyplot as plt
import emd
import padasip as pa
from scipy.fft import fft, fftfreq

# FIGURE_FOLDER = "figs"
#
# # ### EMD IFS
# file_name = "dataset/broken-50-40.csv"
# data = np.loadtxt(file_name, delimiter=",")
#
# u = data[:, 1]
# imf = emd.sift.sift(u)
#
# emd.plotting.plot_imfs(imf, scale_y=True, cmap=True)
# plt.tight_layout()
#
# filepath = os.path.join(FIGURE_FOLDER, "emd_imfs_b.png" )
# plt.savefig(filepath)



# ### HISTO
# column = 1
# n = 10
#
# filepath = os.path.join("BrokenTooth Data", "b30hz20.txt")
# data = np.loadtxt(filepath)
# u1 = data[:, column]
# x = pa.input_from_history(u1, n)[:-1]
# d = u1[n:]
# f = pa.filters.FilterNLMS(n=n, mu=0.5, w="zeros")
# y, e1, w = f.run(d, x)
# imf1 = emd.sift.sift(u1)[:, 0]
#
# filepath = os.path.join("Healthy Data", "h30hz20.txt")
# data = np.loadtxt(filepath)
# u2 = data[:, column]
# x = pa.input_from_history(u2, n)[:-1]
# d = u2[n:]
# f = pa.filters.FilterNLMS(n=n, mu=0.5, w="zeros")
# y, e2, w = f.run(d, x)
# imf2 = emd.sift.sift(u2)[:, 0]
#
# plt.subplot(131)
# plt.hist(u1, bins='auto', histtype='step')
# plt.hist(u2, bins='auto', histtype='step')
# plt.title("Raw data")
#
# plt.subplot(132)
# plt.hist(e1, bins='auto', histtype='step')
# plt.hist(e2, bins='auto', histtype='step')
# plt.title("Prediction error")
#
# plt.subplot(133)
# plt.hist(imf1, bins='auto', histtype='step')
# plt.hist(imf2, bins='auto', histtype='step')
# plt.title("IMF 1")
#
# plt.tight_layout()
# plt.show()


# # ### FFTs
# column = 0
# T = 1 / 30
# zoom = -1
#
# plt.subplot(211)
# filepath = os.path.join("BrokenTooth Data", "b30hz20.txt")
# data = np.loadtxt(filepath)
# u = data[:, column]
# y = u
# N = len(y)
# yf = fft(y)
# xf = fftfreq(N, T)[:N//2]
# plt.plot(xf[:zoom], 2.0/N * np.abs(yf[0:N//2][:zoom]))
# plt.title("Broken")
# plt.yscale('log')
#
# plt.subplot(212)
# filepath = os.path.join("Healthy Data", "h30hz20.txt")
# data = np.loadtxt(filepath)
# u = data[:, column]
# y = u
# N = len(y)
# yf = fft(y)
# xf = fftfreq(N, T)[:N//2]
# plt.plot(xf[:zoom], 2.0/N * np.abs(yf[0:N//2][:zoom]))
# plt.title("Healthy")
# plt.yscale('log')
#
# plt.tight_layout()
# plt.show()



# column = 3
# f = 100
# YLIM = 6000
#
# plt.subplot(211)
# filepath = os.path.join("BrokenTooth Data", "b30hz20.txt")
# data = np.loadtxt(filepath)
#
# signal = data[:, column]
# N = len(signal)
# windowed_signal = np.hamming(N) * signal
# dt = 1/f
# freq_vector = np.fft.rfftfreq(N, d=dt)
# X = np.fft.rfft(signal)
# log_X = np.log(np.abs(X))
#
# cepstrum = np.fft.rfft(log_X)
# df = freq_vector[1] - freq_vector[0]
# quefrency_vector = np.fft.rfftfreq(log_X.size, df)
#
# plt.plot(quefrency_vector, np.abs(cepstrum))
# plt.xlabel('quefrency (s)')
# plt.title('Broken')
# plt.ylim(0, YLIM)
#
#
# plt.subplot(212)
# filepath = os.path.join("Healthy Data", "h30hz20.txt")
# data = np.loadtxt(filepath)
#
# signal = data[:, column]
# N = len(signal)
# windowed_signal = np.hamming(N) * signal
# dt = 1/f
# freq_vector = np.fft.rfftfreq(N, d=dt)
# X = np.fft.rfft(signal)
# log_X = np.log(np.abs(X))
#
# cepstrum = np.fft.rfft(log_X)
# df = freq_vector[1] - freq_vector[0]
# quefrency_vector = np.fft.rfftfreq(log_X.size, df)
#
# plt.plot(quefrency_vector, np.abs(cepstrum))
# plt.xlabel('quefrency (s)')
# plt.title('Healthy')
# plt.ylim(0, YLIM)
#
#
#
# plt.tight_layout()
# plt.show()
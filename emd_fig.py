import emd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.arange(0, 1000)

x = (t / 100) + np.sin(2 * np.pi * 0.011 * t) + np.sin(2 * np.pi * 0.029 * t) + np.sin(2 * np.pi * 0.051 * t) - 5



peak_locs, peak_mags = emd.sift.get_padded_extrema(x, pad_width=0, mode='peaks')
trough_locs, trough_mags = emd.sift.get_padded_extrema(x, pad_width=0, mode='troughs')

# plt.figure()
# plt.plot(x, 'k')
# plt.plot(peak_locs, peak_mags, 'o')
# plt.plot(trough_locs, trough_mags, 'o')
# plt.xlim(0, 150)
# plt.show()

proto_imf = x.copy()
# Compute upper and lower envelopes
upper_env = emd.utils.interp_envelope(proto_imf, mode='upper')
lower_env = emd.utils.interp_envelope(proto_imf, mode='lower')

# Compute average envelope
avg_env = (upper_env+lower_env) / 2

plt.figure(figsize=(10,5))
plt.plot(x, 'k')
plt.plot(upper_env)
plt.plot(lower_env)
plt.plot(avg_env)
plt.plot(peak_locs, peak_mags, 'o')
plt.plot(trough_locs, trough_mags, 'o')
plt.xlim(0, 150)
plt.ylim(-8, -1)
plt.xlabel("Discrete time index [k]")
plt.ylabel("Value [-]")
plt.legend(['Signal', 'Upper Envelope', 'Lower Envelope', 'Average Envelope', "Local Maxima", "Local Minima"])
plt.tight_layout()
# plt.show()
plt.savefig("figs/emd_dummy_env.png")
plt.show()

imf = emd.sift.sift(x, imf_opts={'sd_thresh': 0.1})
emd.plotting.plot_imfs(imf, cmap=True, scale_y=True)
plt.tight_layout()
plt.savefig("figs/emd_dummy_imf.png")
plt.show()
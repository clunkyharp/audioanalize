import numpy as np
import matplotlib.pyplot as plt
import librosa.display

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()

hl = 512 # number of samples per time-step in spectrogram
hi = 128 # Height of image
wi = 384 # Width of image

# Loading demo track
y, sr = librosa.load(librosa.ex('trumpet'))
window = y[0:wi*hl]

S = librosa.feature.melspectrogram(y=window, sr=sr, n_mels=hi, fmax=8000,
hop_length=hl)
S_dB = librosa.power_to_db(S, ref=np.max)
img = librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr, fmax=8000, ax=ax)

plt.savefig("out.png")
#plt.show()
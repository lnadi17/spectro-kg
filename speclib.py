import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.io.wavfile as wave
import numpy.fft
from IPython.display import Audio
import sys


# returns sampling frequency and audio data in range [-1, 1]. prints audio length and sample rate
def read_wav_audio(audio_relative_path, verbose=False):
    # fs is sample rate, audio_data is data from a .wav file
    fs, audio_data = wave.read(audio_relative_path)

    # audio length in seconds
    length = len(audio_data) / fs

    if verbose:
        print("Audio length: {} seconds, Sample rate: {} Hz".format(
            round(length, 2), fs))

    # convert dtype to float32. works on common data types specified in
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
    dtype = audio_data.dtype
    if dtype != np.float32:
        type_info = np.iinfo(dtype)
        audio_data = np.interp(
            audio_data, [type_info.min, type_info.max], [-1, 1])

    return fs, audio_data


# n_width is window width and n_overlap is window overlap (in samples)
def get_window_generator(signal, n_width=1024, n_overlap=512):
    index = 0
    original_length = len(signal)

    while True:
        start_pos = (n_width - n_overlap) * index
        stop_pos = start_pos + n_width  # last index is excluded

        if start_pos > original_length:
            break

        # pad signal with zeros if stop_pos has exceeded signal length
        if stop_pos > original_length:
            delta = stop_pos - original_length
            signal = np.pad(signal, (0, delta), 'constant')

        chunk = signal[start_pos:stop_pos]
        chunk = np.multiply(chunk, np.hanning(len(chunk)))
        window = abs(np.fft.rfft(chunk))

        yield window

        index = index + 1


def get_matrix(audio_data, n_width=1024, n_overlap=512, eps=None):
    windows = get_window_generator(audio_data, n_width, n_overlap)

    # create array which will have fourier transforms in it
    fts = []
    for w in windows:
        fts.append(w)

    # transpose matrix so its columns are fourier transforms (for easier plotting)
    fts = np.array(fts).T

    # rescale matrix
    flat = fts.flatten()
    minimum = flat.min()
    maximum = flat.max()
    if eps is None:
        eps = 1
        # find minimum positive value
        for val in flat:
            if val < eps and val != 0:
                eps = val
        eps /= maximum

    for i in range(fts.shape[0]):
        fts[i] = np.interp(fts[i], [minimum, maximum], [eps, 1])
        fts[i] = 10*np.log10(fts[i])

    return fts


def plot_specgram(signal, fs,
                  n_width=1024, n_overlap=512, eps=None, figsize=None, colorbar=True, labels=True,
                  interpolation='nearest', cmap='inferno'):
    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    spectrogram_show(signal, ax, fs, 
                     eps=eps, n_width=n_width, n_overlap=n_overlap, colorbar=colorbar, labels=labels,
                     interpolation=interpolation, cmap=cmap)

    plt.show()


# calls imshow on passed axes, adds colorbar and labels if needed
def spectrogram_show(signal, ax, fs, 
                     eps=None, n_width=1024, n_overlap=512, colorbar=True, labels=True, 
                     interpolation='nearest', cmap='inferno'):
    # get spectrogram matrix from signal
    arr2d = get_matrix(signal, n_width, n_overlap, eps)
    
    # compute x and y max values
    x_max = arr2d.shape[1] * (n_width - n_overlap) / fs
    y_max = fs / 2

    im = ax.imshow(arr2d,
                   origin='lower',
                   aspect='auto',
                   extent=[0, x_max, 0, y_max],
                   interpolation=interpolation,
                   cmap=cmap)  # useful cmaps: inferno, magma, viridis

    if colorbar:
        cbar = plt.colorbar(im, ax=ax)

    if labels:
        ax.set_xlabel("Time (sec)")
        ax.set_ylabel("Frequency (Hz)")

        if colorbar:
            cbar.ax.set_ylabel('Power (dB)')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import scipy.io.wavfile as wave
import numpy.fft
from IPython.display import Audio
import sys

# returns sampling frequency and audio data in range [-1, 1]. prints audio length and sample rate 
def read_wav_audio(audio_relative_path):
    # fs is sample rate, audio_data is data from a .wav file
    fs, audio_data = wave.read(audio_relative_path)

    # audio length in seconds
    length = len(audio_data) / fs

    print("Audio length:", round(length, 2), "seconds")
    print("Sample rate:", fs, "Hz")

    # convert dtype to float32. works on common data types specified in
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.read.html
    dtype = audio_data.dtype
    if dtype != np.float32:
        type_info = np.iinfo(dtype)
        audio_data = np.interp(audio_data, [type_info.min, type_info.max], [-1, 1])

    return fs, audio_data


# n_width is window width and n_overlap is window overlap (in samples)
def get_window_generator(signal, n_width, n_overlap):
    index = 0
    original_length = len(signal)
    
    while True:
        start_pos = (n_width - n_overlap) * index
        stop_pos = start_pos + n_width # last index is excluded

        
        if start_pos > original_length:
            break

        # pad signal with zeros if stop_pos has exceeded signal length
        if stop_pos > original_length:
            delta = stop_pos - original_length
            signal = np.pad(signal, (0, delta), 'constant')

        chunk = signal[start_pos:stop_pos]
        window = abs(np.fft.rfft(chunk))

        yield window
        
        index = index + 1
        

def get_matrix(audio_data, n_width, n_overlap, eps):
    windows = get_window_generator(audio_data, n_width, n_overlap)

    # create array which will have fourier transforms in it
    fts = []
    for w in windows:
        fts.append(w)

    # transpose matrix so its columns are fourier transforms (for easier plotting)
    fts = np.array(fts).T

    # rescale matrix
    minimum = fts.min()
    maximum = fts.max()
    
    for i in range(fts.shape[0]):
        fts[i] = np.interp(fts[i], [minimum, maximum], [eps, 1])
        
    return fts
        
        
def plot_specgram(signal, fs, n_width=1024, n_overlap=512, eps=10e-5, figsize=(15, 7)):
    plt.figure(figsize=figsize)
    
    fts = get_matrix(signal, n_width, n_overlap, eps)

    # compute x and y max values
    x_max = fts.shape[1] * (n_width - n_overlap) / fs
    y_max = fs / 2

    # plot spectrogram with logarithmic scale
    plt.imshow(fts, 
               origin='lower', 
               aspect='auto', 
               extent=[0, x_max, 0, y_max], 
               interpolation='nearest', 
               norm=colors.LogNorm(vmin=fts.min(), vmax=fts.max()),
               cmap='viridis') # useful cmaps: inferno, magma, viridis

    plt.colorbar(None, use_gridspec=True)

    plt.xlabel("Time (sec)")
    plt.ylabel("Frequency (Hz)")

    # return final result
    return plt

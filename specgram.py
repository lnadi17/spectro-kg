from speclib import *


def main():
    audio_base_path = 'audio/'
    audio_file_name = 'test.wav'

    try:
        audio_file_name = sys.argv[1]
    except:
        pass

    fs, audio_data = read_wav_audio(audio_base_path + audio_file_name)

    # set up parameters
    eps = 1e-8
    n_width = 1024
    n_overlap = n_width // 2
    figsize = (15, 7)

    plot_specgram(audio_data, fs, n_width, n_overlap, eps, figsize)


if __name__ == "__main__":
    main()

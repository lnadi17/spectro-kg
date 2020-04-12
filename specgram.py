#!/usr/bin/env python
from speclib import *
import argparse


def main():
    # create parser
    parser = argparse.ArgumentParser(description='Plot a spectrogram of .wav audio files from command line interface.')
    parser.add_argument('file', help='input .wav audio file path') 
    parser.add_argument('-w', '--window-width', help='set window width. default is 1024.', 
                        type=int, default=1024)
    parser.add_argument('-o', '--overlap-width', help='set overlap width. default is half of window width.', 
                        type=int)
    parser.add_argument('-e', '--epsilon', 
                        help='set custom epsilon to which the darkest color maps. otherwise, it\'s set automatically by the program.', 
                        type=float)
    parser.add_argument('-nc', '--no-colorbar', help='remove colorbar from plot.',
                        action='store_false')
    parser.add_argument('-nl', '--no-labels', help='remove all labels from plot.',
                        action='store_false')
    parser.add_argument('-i', '--interpolation', help='set custom interpolation. default is \'nearest\'.',
                        choices=['nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'gaussian'],
                        default='nearest')
    parser.add_argument('-c', '--colormap', help='set custom colormap. default is \'inferno\'.',
                        choices=['inferno', 'viridis', 'plasma', 'magma', 'cividis', 'hot', 'gray'],
                        default='inferno')
    args = parser.parse_args()
    
    if not args.overlap_width:
        args.overlap_width = args.window_width // 2
        
    if args.overlap_width >= args.window_width:
        print("Warning: Window overlap width must be less than window width. Setting overlap width to default value.")
        args.overlap_width = args.window_width // 2

    fs, audio_data = read_wav_audio(args.file)

    plot_specgram(audio_data, fs, 
                  n_width=args.window_width, n_overlap=args.overlap_width, eps=args.epsilon,
                  colorbar=args.no_colorbar, labels=args.no_labels, interpolation=args.interpolation,
                  cmap=args.colormap)


if __name__ == "__main__":
    main()

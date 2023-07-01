# spectro-kg
This program generates a spectrogram from an input (wav format) audio file.
[დააჭირეთ აქ ქართული README-ს სანახავად.](./README_ge.md)

## Usage
To draw the spectrogram of example.wav with default parameters:
```
./specgram.py example.wav
```
Full list of commands:
```
usage: specgram.py [-h] [-w WINDOW_WIDTH] [-o OVERLAP_WIDTH] [-e EPSILON]
                   [-nc] [-nl]
                   [-i {nearest,bilinear,bicubic,spline16,spline36,gaussian}]
                   [-c {inferno,viridis,plasma,magma,cividis,hot,gray}]
                   file

Plot a spectrogram of .wav audio files from command line interface.

positional arguments:
  file                  input .wav audio file path

optional arguments:
  -h, --help            show this help message and exit
  -w WINDOW_WIDTH, --window-width WINDOW_WIDTH
                        set window width. default is 1024.
  -o OVERLAP_WIDTH, --overlap-width OVERLAP_WIDTH
                        set overlap width. default is half of window width.
  -e EPSILON, --epsilon EPSILON
                        set custom epsilon to which the darkest color maps.
                        otherwise, it's set automatically by the program.
  -nc, --no-colorbar    remove colorbar from plot.
  -nl, --no-labels      remove all labels from plot.
  -i {nearest,bilinear,bicubic,spline16,spline36,gaussian}, --interpolation {nearest,bilinear,bicubic,spline16,spline36,gaussian}
                        set custom interpolation. default is 'nearest'.
  -c {inferno,viridis,plasma,magma,cividis,hot,gray}, --colormap {inferno,viridis,plasma,magma,cividis,hot,gray}
                        set custom colormap. default is 'inferno'.
```

## Detailed Description
The program is divided into two logical parts:
* Jupyter Notebooks (notebook.ipynb, subplots.ipynb, experiments.ipynb)
* Python Scripts (speclib.py, specgram.py)

### notebook.ipynb
This notebook shows the steps leading up to the final implementation of the spectrogram. It serves as an useful tool for exploring experiments and contains the core code, and most of this code is exported to **speclib.py**.

### subplots.ipynb
This file contains a function that allows plotting multiple spectrograms side by side, as it provides a convenient way to compare multiple graphics with matplotlib's spectrogram.

### experiments.ipynb
This notebook shows the plotted spectrogram and the distribution of its values, as I was interested in comparing the two graphics based on epsilon. Any other experiments should be performed here first.

### speclib.py
This file contains all the main functions that assist in drawing the spectrogram. The code is mostly extracted from **notebook.ipynb**, and this library is imported in the remaining files.

### specgram.py
This is a Python script that can be executed from the terminal. It uses the argparse library for argument parsing and speclib.py to draw the spectrogram.

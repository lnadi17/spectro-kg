# spectro-kg
პროგრამა ქმნის სპექტროგრამას მიწოდებული (wav გაფართოების) აუდიო ფაილისგან.

[Click here for the English README](./README.md)

## გამოყენების ინსტრუქცია
საწყისი პარამეტრებით example.wav-ის სპექტროგრამის დახატვა:
```
./specgram.py example.wav
```
ბრძანებების სრული სია:
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

## დეტალური აღწერა
ამ ეტაპზე პროგრამა დაყოფილია ორ ლოგიკურ ნაწილად:
* Jupyter Notebooks (notebook.ipynb, subplots.ipynb, experiments.ipynb)
* Python Scripts (speclib.py, specgram.py)

### notebook.ipynb
აქ ნაჩვენებია ის გავლილი ნაბიჯები რომლებიც სპექტროგრამის საბოლოო იმპლემენტაციამდე მიდის. 
პროგრამის მუშაობის გასარკვევად ამის გამოყენება ჯობს, რადგან მარტივად შეიძლება 
ექპერიმენტების ჩატარება და უმეტესი კოდი **speclib.py**-ში აქედანაა გატანილი.

### subplots.ipynb
ამ ფაილში განმარტებულია ფუნქცია რომელიც რამდენიმე სპექტროგრამის ერთდროულად დახატვის საშუალებას იძლევა, 
რადგან matplotlib-ის სპექტროგრამასთან მაქსიმალურად დასაახლოვებლად ბევრი გრაფიკის ერთდროულად შედარება მიწევდა.

### experiments.ipynb
ამ ეტაპზე ნოუთბუქში გვერდიგვერდაა დახატული სპექტროგრამა და მისი მნიშვნელობების განაწილება, რადგან 
მაშინ მაინტერესებდა epsilon-ზე როგორ იყო ეს ორი გრაფიკი დამოკიდებული. 
თუმცა, სხვა ნებისმიერი ექსპერიმენტიც ჯობია ჯერ აქ ჩატარდეს.

### speclib.py
ამ ფაილში არის ყველა ის ძირითადი ფუნქცია რაც სპექტროგრამის დახატვაში დაგვეხმარება. 
კოდი უმეტესად გადმოტანილია **notebook.ipynb**-დან, დანარჩენ ფაილებში კი უკვე ეს ბიბლიოთეკაა დაიმპორტებული.

### specgram.py
ესაა python სკრიპტი, რომლის გაშვებაც შეიძლება ტერმინალიდან. იყენებს argparse ბიბლიოთეკას არგუმენტების დამუშავებისთვის 
და **speclib.py**-ს სპექტროგრამის დასახატად.

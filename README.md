# NuPIC+NLP Experimental Repository

This repository contains some NLP experiment code using [NuPIC](git@github.com:numenta/nupic.git). Current goal is to build English grammatical error detector.

## Demo

TODO: Make demo.

## Installation

### Install requirements

Some Python libraries are required. We can install them with `pip`. 
We should use Python 2.x, not 3.x. Because current NuPIC do not support Python 3.x...

```
$ pip install -r requirements.txt --user
```

### Install NLTK corpora

We use [NLTKs corpora](http://www.nltk.org/book/ch02.html) for experiment. Install corpura using `nltk.download_shell()`. Start Python interactive environment and hit this command.

```
In [1]: import nltk   
In [2]: nltk.download_shell()
NLTK Downloader
---------------------------------------------------------------------------
    d) Download   l) List    u) Update   c) Config   h) Help   q) Quit
---------------------------------------------------------------------------
Downloader> d

Download which package (l=list; x=cancel)?
  Identifier> all
    Downloading collection u'all'
       | 
       | Downloading package abc
...
       | 
     Done downloading collection all
```

## Usage

### Data pre-processing

Before learning grammatical model using corpora, we sould generate [POS](https://en.wikipedia.org/wiki/Part_of_speech) tag data files. Stay toplevel directory and hit under the command.

```
$ python src/gen_pos_list.py
```

This command takes about ~1min. Output files are in `data` directory. File format is

```
$ head -n 10 data/firefox-pos-list.csv 
Cookie,NNP
Manager,NNP
:,:
``,``
Do,VBP
n't,RB
allow,VB
sites,NNS
that,WDT
set,VBP
```

First column is raw string of corpus, second is POS tag detected by NLTK.


### Create model

Next, we make gramattical model using POS tag stream.

```
$ python src/pos_learning.py
```

This command takes about ~1.5 hour. If `model` directory already exist,
script fail to run, do `rm -rf model` before run script.


### Detect grammatical error with your sentense

start IPython console.

```
import src.pos_err_detect as pos_err_detect
pos_err_detect.posErrDetect("This is a pen.")
(('This', 'DT'), 1.0)
(('is', 'VBZ'), 0.0)
(('a', 'DT'), 0.0)
(('pen', 'NN'), 0.0)
(('.', '.'), 0.050000000000000003)
```

# NuPIC+NLP Experimental Repository

This repository contains some NLP experiment code using [NuPIC](git@github.com:numenta/nupic.git). Current goal is to build English grammar learning system.

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

We use [NLTKs corpora](http://www.nltk.org/book/ch02.html) for experiments. Install corpura using `nltk.download_shell()`. Start Python interactive environment and hit this command.

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

### Create model

Next, we make grammar model using POS tag stream.

```
$ python src/pos_learning.py
```

This command takes couple of hour. If `model` directory already exist,
script fail to run, do `rm -rf model` before run script.


### Predict POS

Start IPython console and hit command blow.

```
In [1]: from src.pos_err_detect import posErrDetect

In [2]: posErrDetect("Numenta has developed a number of applications to demonstrate the applicability of its technology.")
Out[2]: 
[('Numenta', 'NNP', 0.0),
 ('has', 'VBZ', 0.0),
 ('developed', 'VBN', 0.18147734938192225),
 ('a', 'DT', 0.098107685666041902),
 ('number', 'NN', 0.44406909339425471),
 ('of', 'IN', 0.29516224207920139),
 ('applications', 'NNS', 0.068195557070570151),
 ('to', 'TO', 0.10445303851547008),
 ('demonstrate', 'VB', 0.66406086610366322),
 ('the', 'DT', 0.22139312962178964),
 ('applicability', 'NN', 0.41146998263362755),
 ('of', 'IN', 0.31059589197778931),
 ('its', 'PRP$', 0.05848466883598074),
 ('technology', 'NN', 0.24566852690425495),
 ('.', '.', 0.11922788331520065)]
```

Each value has `[0,1]` range. It's predict probability of each word's POS.
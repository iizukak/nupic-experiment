# NuPIC+NLP Experimental Repository

This repository contains some NLP experiment code using [NuPIC](git@github.com:numenta/nupic.git). Current goal is to build POS(Part of Speech) predictor.

## Installation

### Install requirements

Some Python libraries are required. We can install them with `pip`. 
You should use Python 2.x, not 3.x. Because current NuPIC do not support Python 3.x...

```
$ pip install -r requirements.txt --user
```

### Install NLTK corpora

We use [Brown Corpus](https://en.wikipedia.org/wiki/Brown_Corpus) via [NLTK](http://www.nltk.org/book/ch02.html). Install corpura using `nltk.download_shell()`.

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

Next, we make NuPIC model using Brown corpus that POS tagged by NLTK.

```
$ python src/pos_learning.py
```

This command takes couple of hour. If `model` directory already exist,
script fail to run, do `rm -rf model` before run script.


### Predict POS

After create model. Now we can predict POS of a sentence.

```
In [1]: from src.pos_prediction import predictPOS  

In [3]: predictPOS("Numenta has developed a number of applications to demonstrate the applicability of its technology.")
Out[3]: 
[('Numenta', 'NNP', 0.17242003298048558),
 ('has', 'VBZ', 0.0),
 ('developed', 'VBN', 0.20699545397928326),
 ('a', 'DT', 0.035622404184603919),
 ('number', 'NN', 0.45799918713405025),
 ('of', 'IN', 0.27102120514372302),
 ('applications', 'NNS', 0.049628877304811303),
 ('to', 'TO', 0.0),
 ('demonstrate', 'VB', 0.45884920292902631),
 ('the', 'DT', 0.32169826979365984),
 ('applicability', 'NN', 0.52366338091042608),
 ('of', 'IN', 0.25839685244089977),
 ('its', 'PRP$', 0.060240797605142671),
 ('technology', 'NN', 0.44383397040713313),
 ('.', '.', 0.14901950388899751)]
```

`predictPOS ` is the main predict function. It's take a string input and output list of 3 item tuple. Each touple contains

```
(Input word, Tagged POS by NLTK, Accuracy)
```

It's assume that NKTL's tagging is correct.
Accuracy is NuPIC predict each tag how accuracy. It's take [0,1] range.
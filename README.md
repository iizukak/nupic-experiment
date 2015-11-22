# nupic-nlp-experiment
NuPIC Experiment Repository

## Usage

### Install requirements

Use Python `2.x` not `3.x` because of current NuPIC do not support Python `3.x`...

```
pip install -r requirements.txt --user
```

### Generate POS List files

```
python src/gen_pos_list.py
```

This command takes about ~1min.


### Create model

```
python src/pos_learning.py
```

This command takes about ~1.5 hour. If `model` directory exist,
script fail to run, do `rm -rf model` before run script.

### Detect Anomaly

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

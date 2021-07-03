# StrongStationaryTimes

## Installation

1. Create new virtual environment

```bash
$ python3 -m venv .virtualenv
```

(Do
sudo apt install python3-venv
if needed)

3. Activate virtual environment

```bash
$ source .virtualenv/bin/activate
```

4. Upgrade pip, wheel and setuptools 

```bash
$ pip install --upgrade pip
$ pip install --upgrade setuptools
$ pip install wheel
```

5. Install the `strong_stationary_times` package.

```bash
python setup.py develop
```

6. (Optional) In order to use Jupyter with this virtual environment .virtualenv
```bash
pip install ipykernel
python -m ipykernel install --user --name=myenv
```
(see https://janakiev.com/blog/jupyter-virtual-envs/ for details)

## Configuration
Nothing to do

## Content

The code is packaged in ./strong_stationary_times
Its use is given as example in the form of Jupyter notebooks in ./ipynb
In particular, two images are outputted there.

# PIL Python Scripts

Python scripts for image manipulation

## Setup

```
brew install python3
git clone git@github.com:petehawkes/pythonPIL.git
python3 -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## Usage

### Masking
```
usage: ./mask.py [-h] image

positional arguments:
  image       path to image

optional arguments:
  -h, --help  show this help message and exit
```

### Padding
```
usage: ./pad.py [-h] image padding

positional arguments:
  image       path to image      padding

optional arguments:
  -h, --help  show this help message and exit
```

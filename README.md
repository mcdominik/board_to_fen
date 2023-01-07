# board_to_fen


Python package that converts digital chessboard image into Forsyth-Edwards notation (FEN) notation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/board_to_fen)](https://pypi.org/project/board_to_fen/)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcdominik/board_to_fen)](https://github.com/mcdominik/board_to_fen)

### Installation
board_to_fen is available on PyPI:
```
$ pip3 install board_to_fen
```

### Quick Start
```python
from board_to_fen.predict import get_fen_from_image

print(get_fen_from_image(PATH_TO_CHESSBOARD_IMAGE))
```

**Note:** *The package uses tensorflow+keras and python-opencv API. 
They are pretty heavy.*

### Web version
Available at: https://board2fen.bieda.it


### Training
For training You would probably want to download the source code by cloning the repository:
```
$ git clone https://github.com/mcdominik/board_to_fen.git
```
Download training data from:<br>
I will supply url for data in the future

In the main repository dir, run
```
$ python3 ./board_to_fen/train_model.py
```

### Version history

#### v.0.0.1-13 latest
fix path (upload related) bugs 


### References:
https://www.kaggle.com/datasets/koryakinp/chess-positions

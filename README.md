# board_to_fen


Python package that converts digital chessboard image into Forsyth-Edwards notation (FEN) notation

[![Downloads](https://static.pepy.tech/personalized-badge/board-to-fen?period=total&units=none&left_color=purple&right_color=blue&left_text=downloads)](https://pepy.tech/project/board-to-fen)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/board_to_fen)](https://pypi.org/project/board_to_fen/)
[![GitHub last commit](https://img.shields.io/github/last-commit/mcdominik/board_to_fen)](https://github.com/mcdominik/board_to_fen)

### Installation
board_to_fen is available on PyPI:
```
pip3 install board_to_fen
```

### Quick Start
```python
from board_to_fen.predict import get_fen_from_image_path

print(get_fen_from_image_path(PATH_TO_CHESSBOARD_IMAGE))
```

or, if you want you can load image object by yourself:

```python
from PIL import Image
from board_to_fen.predict import get_fen_from_image

img = Image.open(PATH_TO_CHESSBOARD_IMAGE)

print(get_fen_from_image(img))
```


**Note:** *The package uses tensorflow+keras API. 
They are pretty heavy.*

### Customization

get_fen_from_image_path takes has 3 arguments:

- image_path [required]
- end_of_row '/' by default 
- black_view False by default -> set True if chessboard is provided from black player perspective


### Web version (currently may not work)
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

- january 2023
     - versions 0.0.17-25
     - added simple board validation
     - bug fixes

- february 2023
    version 0.1.0-0.1.1
     - migratation from cv2 to PIL
     - new function for direct image object load
     - add simple tests
     - bug fixes

## Warnings
- Image has to be provided in neutral angle (white or black player's perspective).
- Image has to be square (~3% tolerance depending on image resolution).
- Image can't contain paddings, board borders etc. other than 64 squares (with pieces) itself.


### References:
https://www.kaggle.com/datasets/koryakinp/chess-positions

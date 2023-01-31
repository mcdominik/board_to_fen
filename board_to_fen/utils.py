import os
import numpy as np
import cv2
import random
import re
from PIL import Image
from itertools import product


LEGEND = {
    'pawn_white' : 'P',
    'pawn_black' : 'p',
    'knight_white' : 'N',
    'knight_black' : 'n',
    'bishop_white' : 'B',
    'bishop_black' : 'b',
    'rook_white' : 'R',
    'rook_black' : 'r',
    'queen_white' : 'Q',
    'queen_black' : 'q',
    'king_white' : 'K',
    'king_black' : 'k',
    'empty':'1'
}

class Decoder_FEN():
    def __init__(self) -> None:
        pass

    def _squeeze(self, input) -> str:
        filtered = re.sub('11111111', '8', input)
        filtered = re.sub('1111111', '7', filtered)
        filtered = re.sub('111111', '6', filtered)
        filtered = re.sub('11111', '5', filtered)
        filtered = re.sub('1111', '4', filtered)
        filtered = re.sub('111', '3', filtered)
        squeezed = re.sub('11', '2', filtered)
        return squeezed

    def _simple_validator(self, squares):
        ''' ensures that model:
            - found only one white king
            - found only one black king
            - number of pieces is not greater than 32

        Args:
        figures: list of figures before decoding
        '''
        count_king_white = 0
        count_king_black = 0
        figures = 0

        for square in squares:
            if square == 'king_white':
                count_king_white+=1
            if square == 'king_black':
                count_king_black+=1
            if square != 'empty':
                figures +=1
        print(f'figures:{figures}')
        print(f'kb:{count_king_black}')
        print(f'kw:{count_king_white}')
        if ((count_king_black != 1) or (count_king_white != 1) or ((figures) > 32)):
            return 'invalid'

    def fen_decode(self, squares, end_of_row='/', black_view=False) -> str:
        if (self._simple_validator(squares) == 'invalid'):
            return 'Model can\'t find valid chessboard layout'
        long_fen = ''
        for i, square in enumerate(squares):
            if i % 8 == 0 and i>0:
                long_fen+=end_of_row
            long_fen+=LEGEND[square]
            fen = self._squeeze(long_fen)
            if black_view:
                fen = fen[::-1]
        return fen


class DataFetcher:
    def __init__(self) -> None: 
        self.CATEGORIES = ["bishop_black", "bishop_white","empty","king_black","king_white","knight_black", "knight_white","pawn_black", "pawn_white", "queen_black","queen_white", "rook_black","rook_white"]        
        self.data = []
        self.images = []
        self.labels = []

    def fetch_and_shuffle(self, data_dir):
        for category in self.CATEGORIES:
            path = os.path.join(data_dir, category)
            class_num = self.CATEGORIES.index(category)
            for filename in os.listdir(path):
                try:
                    img = cv2.imread(os.path.join(path,filename))
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    #consider division /255
                    self.data.append([img/255, class_num])
                except Exception as e:
                    pass
        random.shuffle(self.data)
        self._create_labels_and_images()

    def _create_labels_and_images(self):
        for features, label in self.data:
            self.images.append(features)
            self.labels.append(label)
        self.images = np.array(self.images).reshape(-1, 50, 50, 3)
        self.labels = np.array(self.labels)

    def get_train_test(self, split=0.85):
        pivot = int(split * len(self.images))
        train_images = self.images[:pivot]
        train_labels = self.labels[:pivot]
        test_images = self.images[pivot:]
        test_labels = self.labels[pivot:]
        return train_images, train_labels, test_images, test_labels


class Tiler:
    def __init__(self) -> None:
        self.tile_images = []
        pass

    def get_tiles(self, image_path, d=50) -> list:
        img = cv2.imread(image_path)
        img = cv2.resize(img, dsize=(400, 400), interpolation=cv2.INTER_CUBIC)
        img = Image.fromarray(img).convert('RGB')
        w, h = img.size
        grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
        for i, j in grid:
            box = (j, i, j+d, i+d)
            self.tile_images.append(img.crop(box))
        return self.tile_images

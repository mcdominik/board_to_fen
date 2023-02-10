import pytest
from board_to_fen.predict import get_fen_from_image, get_fen_from_image_path
from PIL import Image


img_path = "./test_images/test_image1.png"

class TestNetwork:
    def test_path_prediction(self):
        assert get_fen_from_image_path(img_path) == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    def test_object_prediction(self):
        img = Image.open(img_path)
        assert get_fen_from_image(img) == "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

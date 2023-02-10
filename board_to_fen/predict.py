import io
from PIL import Image
from .KerasNeuralNetwork import KerasNeuralNetwork
from .utils import Decoder_FEN, Tiler
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
from board_to_fen import saved_models


def get_fen_from_image_path(image_path, end_of_row='/', black_view=False) -> str:
    image = Image.open(image_path)
    decoder = Decoder_FEN()
    net = KerasNeuralNetwork()
    f = pkg_resources.open_text(saved_models, 'november_model')
    net.load_model(f.name)
    tiler = Tiler()
    tiles = tiler.get_tiles(img=image)
    predictions = net.predict(tiles=tiles)
    fen = decoder.fen_decode(squares=predictions, end_of_row=end_of_row, black_view=black_view)
    return fen

def get_fen_from_image(image, end_of_row='/', black_view=False) -> str:
    decoder = Decoder_FEN()
    net = KerasNeuralNetwork()
    f = pkg_resources.open_text(saved_models, 'november_model')
    net.load_model(f.name)
    tiler = Tiler()
    tiles = tiler.get_tiles(img=image)
    predictions = net.predict(tiles=tiles)
    fen = decoder.fen_decode(squares=predictions, end_of_row=end_of_row, black_view=black_view)
    return fen
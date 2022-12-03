import io
from .KerasNeuralNetwork import KerasNeuralNetwork
from .utils import Decoder_FEN, Tiler
try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources
from board_to_fen import saved_models


def get_fen_from_image(image_path, end_of_row='/', black_view=False) -> str:
    decoder = Decoder_FEN()
    net = KerasNeuralNetwork()
    f = pkg_resources.open_text(saved_models, 'november_model')
    net.load_model(f.name)
    tiler = Tiler()
    tiles = tiler.get_tiles(image_path=image_path)
    predictions = net.predict(tiles=tiles)
    fen = decoder.fen_decode(figures=predictions, end_of_row=end_of_row, black_view=black_view)
    return fen


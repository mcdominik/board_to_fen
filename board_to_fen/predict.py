import io
from PIL import Image
from .KerasNeuralNetwork import KerasNeuralNetwork
from .utils import Decoder_FEN, Tiler
import os
import tensorflow as tf
from board_to_fen import saved_models
import numpy as np

# try:
#     import importlib.resources as pkg_resources
# except ImportError:
#     # Try backported to PY<37 `importlib_resources`.
#     import importlib_resources as pkg_resources
# deprecated

os.sys.path.append("board_to_fen/KerasNeuralNetwork")
from .KerasNeuralNetwork import KerasNeuralNetwork
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(CURRENT_DIR, "saved_models")
PATH_TO_MODEL = os.path.join(MODELS_DIR, "november_model")
PATH_TO_MODEL_WEIGHTS = os.path.join(MODELS_DIR, "november_model_weights.h5")
# MODELS_DIR = "board_to_fen/saved_models/"
# PATH_TO_MODEL_WEIGHTS = os.path.join(MODELS_DIR, "november_model_weights.h5")

model = KerasNeuralNetwork()
model.load_model_from_weights(path=PATH_TO_MODEL_WEIGHTS)
# model = tf.keras.models.load_model("board_to_fen/saved_models/november_model_weights.h5")

def get_fen_from_image_path(image_path, end_of_row='/', black_view=False) -> str:
    """
    Predict FEN position from path to a chess image.

    Parameters
    ----------
    image : type
        Description
    end_of_row : str
        Indicate how to process end of chess row
    black_view : bool
        Set to True iff the board is viewed from Black's perspective.
    
    Returns:
        str: Predicted chess position in FEN notation
    """
    image = Image.open(image_path)
    decoder = Decoder_FEN()
    # net = KerasNeuralNetwork()
    tiler = Tiler()
    tiles = tiler.get_tiles(img=image)

    # f = pkg_resources.open_text(saved_models, 'november_model')  # Deprecated
    #net.load_model(f.name)
    #predictions = net.predict(tiles=tiles) # Deprecated

    # convert tiles object to tf tensor before compute predictions
    tiles_array = np.array([np.array(tile) for tile in tiles], dtype=np.float32)
    tiles_tensor = tf.convert_to_tensor(tiles_array, dtype=tf.float32)
    predictions = model.predict(tiles_tensor)
    fen = decoder.fen_decode(squares=predictions, end_of_row=end_of_row, black_view=black_view)
    return fen

def get_fen_from_image(image, end_of_row='/', black_view=False) -> str:
    """
    Predict FEN position from Image-like object, which represents a chess board.

    Parameters
    ----------
    image : PIL.Image
        image Object 
    end_of_row : str
        Indicate how to process end of chess row
    black_view : bool
        Set to True if the board is viewed from Black's perspective.

    
    Returns:
        str: Predicted chess position in FEN notation
    """
    decoder = Decoder_FEN()
    tiler = Tiler()
    tiles = tiler.get_tiles(img=image)

    tiles_array = np.array([np.array(tile) for tile in tiles], dtype=np.float32)
    tiles_tensor = tf.convert_to_tensor(tiles_array, dtype=tf.float32)

    # Predict
    predictions = model.predict(tiles_tensor)

    # Decode predictions to FEN
    fen = decoder.fen_decode(
        squares=predictions,
        end_of_row=end_of_row,
        black_view=black_view
    )
    return fen

if __name__ == "__main__":
    img_path = "./board_to_fen/test_image.jpeg"
    fen = get_fen_from_image_path(img_path)
    print(fen)
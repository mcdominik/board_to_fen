import os
from contextlib import redirect_stderr
with redirect_stderr(open(os.devnull, "w")):
    from keras import models, layers
import numpy as np


class KerasNeuralNetwork:
    def __init__(self) -> None:
        self.CATEGORIES = ["bishop_black", "bishop_white","empty","king_black","king_white","knight_black", "knight_white","pawn_black", "pawn_white", "queen_black","queen_white", "rook_black","rook_white"]
        self.predictions = []
        self.model = models.Sequential()
        self.model.add(layers.Conv2D(50, (3,3), activation='relu', input_shape=(50,50,3)))
        self.model.add(layers.MaxPooling2D((2,2)))
        self.model.add(layers.Conv2D(100,(3,3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2,2)))
        self.model.add(layers.Conv2D(100, (3,3), activation='relu'))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(100, activation='relu'))
        self.model.add(layers.Dense(13, activation='softmax'))
        self.model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    def fit(self, train_images, train_labels, test_images, test_labels, num_of_epochs=2, batch_size=32):
        self.model.fit(train_images, train_labels, epochs=num_of_epochs, verbose=1, validation_data=(test_images, test_labels), batch_size=batch_size)

    def save(self, path='.') -> None:
        self.model.save(path)

    def evaluate(self, test_images, test_labels):
        loss, accuracy = self.model.evaluate(test_images, test_labels)
        print(f"accuracy:{accuracy}")
        print(f"loss:{loss}")

    def load_model(self, path):
        self.model = models.load_model(path)
    
    def predict(self, tiles) -> list:
        for image in tiles:
            image = np.array(image)
            image = np.reshape(image, ((1, 50, 50, 3)))
            prediction = self.model.predict(image, verbose=0)
            index = np.argmax(prediction)
            self.predictions.append(self.CATEGORIES[index])
        return self.predictions
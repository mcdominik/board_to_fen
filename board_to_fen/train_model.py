import os
# silence tensorflow and keras debugging information
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from .utils import DataFetcher
from .KerasNeuralNetwork import KerasNeuralNetwork


if __name__ == "__main__":
    #fetch and prepare data
    fetcher = DataFetcher()
    fetcher.fetch_and_shuffle(data_dir='./test_splitted/')
    train_images, train_labels, test_images, test_labels = fetcher.get_train_test()

    #call and feed the neural network
    net = KerasNeuralNetwork()
    net.fit(train_images, train_labels, test_images, test_labels)
    net.evaluate(test_images, test_labels)
    net.save(path='./saved_models/another_model')





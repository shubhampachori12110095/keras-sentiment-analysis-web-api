import numpy as np

from keras_sentiment_analysis.library.ffn import WordVecGloveFFN
from keras_sentiment_analysis.library.utility.simple_data_loader import load_text_label_pairs
from keras_sentiment_analysis.library.utility.text_fit import fit_text


def main():
    random_state = 42
    np.random.seed(random_state)

    output_dir_path = './models'
    data_file_path = './data/umich-sentiment-train.txt'
    text_data_model = fit_text(data_file_path)
    text_label_pairs = load_text_label_pairs(data_file_path)

    classifier = WordVecGloveFFN()
    classifier.load_glove_model(data_dir_path='./very_large_data')
    batch_size = 64
    epochs = 20
    history = classifier.fit(text_data_model=text_data_model,
                             model_dir_path=output_dir_path,
                             text_label_pairs=text_label_pairs,
                             batch_size=batch_size, epochs=epochs,
                             test_size=0.3,
                             random_state=random_state)


if __name__ == '__main__':
    main()

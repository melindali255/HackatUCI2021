import tensorflow_hub as hub
import os
from tensorflow import keras
from collections import Counter
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split
import warnings
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 200)

pd.set_option('display.max_colwidth', 200)

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    print("hello")

    checkpoint_path = "/YouTubeSentiment/cp"

    batch_size = 32

    # Create a callback that saves the model's weights every 5 epochs
    cp_callback = keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_path, 
        verbose=1, 
        save_weights_only=True,
        save_freq=5*batch_size)

    def create_model():
        embed_size = 128
        vocab_size = 10000
        num_oov_buckets = 1000
        model = keras.models.Sequential([
        #     hub.KerasLayer("https://tfhub.dev/google/tf2-preview/nnlm-en-dim50/1",
        #  dtype=tf.string, input_shape=[], trainable=True),
            keras.layers.Embedding(vocab_size + num_oov_buckets, embed_size, input_shape=[None]),
            # keras.layers.Bidirectional(keras.layers.LSTM(50, return_sequences=True), merge_mode='concat'),
            keras.layers.Bidirectional(keras.layers.LSTM(256, return_sequences=True), merge_mode='concat'),
            keras.layers.Bidirectional(keras.layers.LSTM(256), merge_mode='concat'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.5),
            keras.layers.Dense(3, activation='softmax')
        ])
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    model = create_model()
    print(model.summary())

    # history = model.fit(train_set, epochs=10,
    #                     validation_data=val_set)

    # model.save_weights(checkpoint_path.format(epoch=0))

    # # history = model.fit(train_set, epochs=5, validation_data=(val_set))
    # history = model.fit(train_set, epochs=5, callbacks=[cp_callback], validation_data=val_set)

    def preprocess(texts):
        X = tokenizer.texts_to_sequences(texts)
        # X = table.lookup(texts)
        return X
        #  return tf.one_hot(X, max_id)

        # test_str = tf.convert_to_tensor(np.array(['You and your shit brother may have single handedly ruined YouTube.....thanks...']))
        # print(test_str)
    # test_str = np.array(['The application wasn t even placed on well  Needs to be applied with the foundation brush  the beautyblender totally soaks up the foundation and really ruins the product s payoff  Other than that ...'])
    # test_str = np.array(['The hey ruins bad suck'])

    # X_new = preprocess(test_str)
    # X_new = np.array([[x for x in X_new[0] if x < 10000]])
    # print(X_new)
    # Y_pred = model.predict(X_new)
    # print(Y_pred)

    model = create_model()

    weights_path = '/YouTubeSentiment/cp-0005.ckpt.index'
    model.load_weights(weights_path)
    Y_pred = model.predict(X_new, steps=1)
    print(Y_pred)

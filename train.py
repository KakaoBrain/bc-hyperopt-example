import argparse
import tensorflow as tf


class Trainer(object):

    def run(self, lr=0.001, dropout=0.2, epochs=5):
        mnist = tf.keras.datasets.mnist

        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train, x_test = x_train / 255.0, x_test / 255.0

        model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation=tf.nn.relu),
            tf.keras.layers.Dropout(dropout),
            tf.keras.layers.Dense(10, activation=tf.nn.softmax)
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(lr=lr),
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(x_train, y_train, epochs=epochs)
        (loss, accuracy) = model.evaluate(x_test, y_test)
        return (loss, accuracy)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=0.001,
                        help="learning rate")
    parser.add_argument("--dropout", type=float, default=0.2, help="dropout")
    parser.add_argument("--epochs", type=int, default=5, help="epochs")
    args = vars(parser.parse_args())
    print("args:", args)
    t = Trainer()
    loss, accuracy = t.run(**args)
    print('loss:', loss, ', accuracy:', accuracy)

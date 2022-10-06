import os
import tensorflow as tf
from tensorflow import keras
from PIL import Image

train, test = keras.datasets.mnist.load_data()

def save_image(filename, data):
    img = Image.new("L", (28,28))
    pix = img.load()
    for i in range(28):
        for j in range(28):
            pix[j, i] = int(data[i][j])
    img = img.resize((28*5, 28*5))
    img.save(filename)
    print(filename)


def dump(data, dhead):
    images, labels = data
    save_image("test.png", images[0])
    print(labels[0])
    count = [0] * 10
    for i in range(len(images)):
        index = labels[i]
        filename = f"{dhead}/{index}/{count[index]:04}.png"
        save_image(filename, images[i])
        count[index] += 1


if __name__ == '__main__':
    for i in range(10):
        dname = f"train/{i}"
        if os.path.isdir(dname) is False:
            os.makedirs(dname)
        dname = f"test/{i}"
        if os.path.isdir(dname) is False:
            os.makedirs(dname)
    dump(train, "train")
    dump(test, "test")

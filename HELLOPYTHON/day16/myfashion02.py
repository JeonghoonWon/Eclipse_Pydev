import tensorflow as tf
import cv2
import numpy as np

fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_labels[0])
print(test_labels[0])

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0
test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

img = cv2.imread('sandal.jfif', 1)
img_28 = cv2.resize(img,(28,28))
img_gray = cv2.cvtColor(img_28, cv2.COLOR_BGR2GRAY)
img_input = (255 - img_gray)/256
img_input2 =  np.reshape(img_input,(1, 28, 28))


predictions = model.predict(img_input2)
print(np.argmax(predictions[0]))

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2
import numpy as np


(train_images, train_labels), (test_orgin_images, test_origin_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_orgin_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(train_labels[0])
print(test_origin_labels[0])

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_origin_labels)

print(train_labels[0])
print(test_labels[0])


model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images)

cnt_o = 0
cnt_x = 0

for i,p in enumerate(predictions):
    val_p = np.argmax(p)
    val_g = test_origin_labels[i]
    if val_p == val_g :
        cnt_o += 1
    else:
        cnt_x += 1
        cv2.imwrite("diff/"+str(val_p)+"_"+str(val_g)+"_"+str(i)+".png", test_orgin_images[i])


print("cnt_o:",cnt_o)
print("cnt_x:",cnt_x)   
    
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)

cv2.waitKey(0)
cv2.destroyAllWindows()









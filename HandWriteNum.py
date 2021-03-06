import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.client import device_lib

#MNIST dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 將pixel值轉成float，同時做normalize
x_train, x_test = x_train/255.0, x_test/255.0

# MODEL
# keras 的 Sequential 把每層串起來
model = tf.keras.models.Sequential([
    #784個特徵值
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    #找出刺激強度較大的細胞，引起神經衝動
    tf.keras.layers.Dense(256, activation='relu'),
    #訓練週期中隨機丟棄20%神經元
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(0, activation='softmax'),
])

# MODEL COMPILE
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['acc'])

# train data
history = model.fit(x_train, y_train, epochs=5)
# evalutate test data
test_history = model.evaluate(x_test, y_test, verbose=2)

plt.title('Training Model Accuracy')
plt.plot(history.history['acc'], 'r')
plt.show()
plt.title('Training Model Loss')
plt.plot(history.history['loss'], 'r')
plt.show()

# 實際預測 40 筆
predictions = model.predict_classes(x_test)
print('prediction:', predictions[80:120])
print('actual    :', y_test[80:120])

# 顯示錯誤的資料圖像
X2 = x_test[115,:,:]
plt.title('Test Loss ( prediction: ' + str(predictions[115]) + ', actual: ' + str(y_test[115])+ ')')
plt.imshow(X2.reshape(28,28))
plt.show()

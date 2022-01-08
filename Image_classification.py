import tensorflow as tf 
tf.test.gpu_device_name()

import os
import tensorflow as tf
from tensorflow.keras import models  
from tensorflow.keras import layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

train_dir_path =  # Train file path
test_dir_path = # Test file path

def getAllClassNames(dir_path):
    return os.listdir(dir_path)

AllClassNames = getAllClassNames(train_dir_path)
num_of_classes = len(AllClassNames)
print(num_of_classes)
DictOfClasses = {i : AllClassNames[i] for i in range(0, len(AllClassNames))}

conv_base = VGG16(weights='imagenet', include_top=False, input_shape=(100,100,3))
conv_base.trainable = False
model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(512,activation='relu'))
model.add(layers.Dropout(0.5))  
model.add(layers.Dense(num_of_classes,activation='softmax'))

optimizer = Adam(lr=1e-2, decay=1e-2)
model.compile(optimizer=optimizer,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
           
model.summary()

# Rescale the image
datagen = ImageDataGenerator(rescale=1./255,
                             shear_range=0.4,
                             zoom_range=0.2,
                             rotation_range=50,
                             width_shift_range=0.2,
                             height_shift_range=0.2,
                             horizontal_flip=True,
                             fill_mode='nearest')
batch_size = 32

train_generator = datagen.flow_from_directory(
        train_dir_path,  # this is the target directory
        target_size=(100, 100),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='categorical')  # since we use binary_crossentropy loss, we need binary labels

test_generator = datagen.flow_from_directory(
        test_dir_path,  # this is the target directory
        target_size=(100, 100),  # all images will be resized to 150x150
        batch_size=batch_size,
        class_mode='categorical')  # since we use binary_crossentropy loss, we need binary labels
    
# Train for 100 epcohs including back propogation.
history = model.fit_generator(train_generator,
                          epochs = 100,
                          validation_data = test_generator,
                          verbose=1)

# Add the test image to a file.
import cv2
import os
x_test=[]
y_test=[]
n = 0
os.chdir("/content/drive/My Drive/abc/test/Apple Red Delicious")
for i in os.listdir():
  img = cv2.imread(i)
  x_test.append(img)
  y_test.append(n)
os.chdir("/content/drive/My Drive/abc/test/Eggplant")
n+=1
for i in os.listdir():
  img = cv2.imread(i)
  x_test.append(img)
  y_test.append(n)
os.chdir("/content/drive/My Drive/xyz/test/Pepper Green")
n+=1
for i in os.listdir():
  img = cv2.imread(i)
  x_test.append(img)
  y_test.append(n)


# Preedict, compare and chek the accuracy by printing the confusion matrix.
x_test=np.array(x_test)
y_test=np.array(y_test)
from keras.utils import to_categorical
y_test = to_categorical(y_test)
y_pred = model.predict(x_test)
yt = np.argmax(y_test, axis = 1)
yp = np.argmax(y_pred, axis = 1)

import sklearn.metrics as metrics
from sklearn.metrics import confusion_matrix
print("Confusion Matrix: ")
print(confusion_matrix(yt, yp))  
print ("Accuracy : ",metrics.accuracy_score(yt,yp)*100)

# serialize model to JSON
os.chdir("/content/drive/My Drive")
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("final.h5")
print("Saved model to disk")

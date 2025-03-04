# Importing necessary libraries
import tensorflow as tf
from tensorflow import keras
import tensorflow_hub as hub  # For pre-trained models
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.image as img
import PIL.Image as Image
import cv2
import os
import numpy as np
import pathlib
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define dataset directories
# Define dataset directories (Windows-style paths with raw strings)
dataset_dir = r"C:\Users\Balir\Downloads\GrainPalette\Data\Rice_Image_Dataset"
test_dataset_dir = r"C:\Users\Balir\Downloads\GrainPalette\Data\Rice_Test_Dataset"  # Ensure this folder exists
 # Separate test dataset

# Define parameters
img_size = (224, 224)
batch_size = 32
num_labels = 5  # Number of classes

# Data Augmentation and Loading Data
datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    validation_split=0.2  # 20% for validation
)

train_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    dataset_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Define Test Generator (separate dataset)
test_datagen = ImageDataGenerator(rescale=1.0/255.0)

test_generator = test_datagen.flow_from_directory(
    test_dataset_dir,  # Ensure test images are in a separate folder
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

# ---- Model Definition ----
mobilenet_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"
mobile_net = hub.KerasLayer(mobilenet_url, input_shape=(224, 224, 3), trainable=False)

model = keras.Sequential([
    mobile_net,
    keras.layers.Dense(num_labels, activation='softmax')
])

# Model summary
model.summary()

# Compile the model
model.compile(
    optimizer="adam",
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
    metrics=["accuracy"]
)

# ---- Training the Model ----
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=10
)

# ---- Evaluating the Model on Validation Set ----
val_loss, val_accuracy = model.evaluate(val_generator)
print(f"Validation Accuracy: {val_accuracy * 100:.2f}%")

# ---- Evaluating the Model on Test Set ----
test_loss, test_accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

# ---- Generate Classification Report ----
y_pred = model.predict(test_generator, verbose=1)
y_pred_bool = np.argmax(y_pred, axis=1)
y_true = test_generator.classes
print(classification_report(y_true, y_pred_bool))

# ---- Plot Training Performance ----
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.title("Accuracy Over Epochs")

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.title("Loss Over Epochs")
plt.show()

# ---- Preview Sample Images ----
fig, ax = plt.subplots(ncols=5, figsize=(20, 5))
fig.suptitle("Rice Categories")

sample_images, _ = next(train_generator)  # Get a batch of images
sample_labels = list(train_generator.class_indices.keys())

for i in range(5):
    ax[i].imshow(sample_images[i])
    ax[i].set_title(sample_labels[i])
    ax[i].axis("off")

plt.show()

# ---- Save the Model ----
model.save("rice.h5")
print("Model saved as rice.h5")

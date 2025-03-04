import tensorflow as tf

# Load the old .h5 model
model = tf.keras.models.load_model('rice.h5', custom_objects={'KerasLayer': tf.keras.layers.Layer})

# Save in TensorFlow SavedModel format
model.save('rice_saved_model', save_format='tf')

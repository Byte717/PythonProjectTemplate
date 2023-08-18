import tensorflow as tf


gpus = tf.config.list_logical_devices('GPU')

print(gpus)
tf.debugging.set_log_device_placement(True)

with tf.device('/GPU:0'):
    pass
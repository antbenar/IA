from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.applications.inception_v3 import *
import numpy as np

model = InceptionV3(weights='imagenet')

#img = image.load_img('images/dog.jpg', target_size=(299, 299))
#img = image.load_img('images/calamardo.jpg', target_size=(299, 299))
#img = image.load_img('images/house.jpg', target_size=(299, 299))
#img = image.load_img('images/watch.jpg', target_size=(299, 299))
#img = image.load_img('images/triceraptos.jpg', target_size=(299, 299))
img = image.load_img('images/jhony.jpg', target_size=(299, 299))

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

y = model.predict(x)
for index, res in enumerate(decode_predictions(y,top=5)[0]):
    print('{}. {}: {:.3f}%'.format(index + 1, res[1], 100 * res[2]))
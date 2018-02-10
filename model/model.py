
from sklearn.datasets import load_files
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np
from glob import glob

#python -m pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.12.0-py2-none-any.whl


def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def paths_to_tensor(img_paths):
    list_of_tensors = [path_to_tensor(img_path) for img_path in tqdm(img_paths)]
    return np.vstack(list_of_tensors)

def process_data():
	# pre-process the data for Keras
	train_tensors=None
	valid_tensors=None
	test_tensors=None
	
	train_tensors = paths_to_tensor(train_files).astype('float32')/255
	valid_tensors = paths_to_tensor(valid_files).astype('float32')/255
	test_tensors = paths_to_tensor(test_files).astype('float32')/255

def build_model():
	model = Sequential()
	# TODO: add layers
	return model

def fit_model():
	model = build_model()

	model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

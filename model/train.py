from sklearn.datasets import load_files
from keras import applications
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.callbacks import ModelCheckpoint
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np
from glob import glob
import h5py 
import PIL

from model import *

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

def load_dataset(path):
	NUM_FAMILIES = 1 # change to number of subfolders
	data = load_files(path)
	fish_files = np.array(data['filenames'])
	fish_targets = np_utils.to_categorical(np.array(data['target']), NUM_FAMILIES)
	return fish_files, fish_targets

def augment_dataset():
	#TODO
	pass

def train_model():
	# load the train, test, and validation datasets
	train_files, train_targets = load_dataset('../fishImages_mock/train')
	valid_files, valid_targets = load_dataset('../fishImages_mock/valid')
	#import pdb;pdb.set_trace()

	# convert images to 4D tensor
	train_tensors = paths_to_tensor(train_files).astype('float32')/255
	valid_tensors = paths_to_tensor(valid_files).astype('float32')/255

	# get the model architecture
	model = build_model()
	model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
	
	# fit with a checkpointer which saves the best performing model under filepath
	checkpointer = ModelCheckpoint(filepath='saved_models/weights.best.from_scratch.hdf5', 
	                               verbose=1, save_best_only=True)
	epochs = 5
	model.fit(train_tensors, train_targets, 
	          validation_data=(valid_tensors, valid_targets),
	          epochs=epochs, batch_size=20, callbacks=[checkpointer], verbose=1)


if __name__ == '__main__':
	train_model()
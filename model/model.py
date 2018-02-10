
from sklearn.datasets import load_files
from keras import applications
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Sequential
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np
from glob import glob

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

def build_model():
	# Use VGG16 model trained on Image Net and finetune the top layer
	base_model = applications.VGG16(weights='imagenet', include_top=False)
	
	for layer in base_model:
		#Freeze imagenet trained layers
		layer.trainable = False
	top_model = Sequential()
	top_model.add(Flatten(input_shape=model.output_shape[1:]))
	top_model.add(Dense(256, activation='relu'))
	top_model.add(Dropout(0.5))
	top_model.add(Dense(1, activation='sigmoid'))

	# stick them together
	model = Model(inputs=base_model.iniput, outputs=top_model)

	return model


def load_dataset(path):
	NUM_FAMILIES = 100 # change to number of subfolders
	data = load_files(path)
	fish_files = np.array(data['filenames'])
	fish_targets = np_utils.to_categorical(np.array(data['target']), NUM_FAMILIES)
	return fish_files, fish_targets


def train_model():
	# load the train, test, and validation datasets
	train_files, train_targets = load_dataset('fishImages/train')
	valid_files, valid_targets = load_dataset('fishImages/valid')
	test_files, test_targets = load_dataset('fishImages/test')

	# convert images to 4D tensor
	train_tensors = paths_to_tensor(train_files).astype('float32')/255
	valid_tensors = paths_to_tensor(valid_files).astype('float32')/255
	test_tensors = paths_to_tensor(test_files).astype('float32')/255

	# get the model architecture
	model = build_model()

	model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
	
	# fit with a checkpointer which saves the best performing model under filepath
	checkpointer = ModelCheckpoint(filepath='saved_models/weights.best.from_scratch.hdf5', 
	                               verbose=1, save_best_only=True)
	epochs = 5
	model.fit(train_tensors, train_targets, 
	          validation_data=(valid_tensors, valid_targets),
	          epochs=epochs, batch_size=20, callbacks=[checkpointer], verbose=1)



if '__name__' == '__main__':
	build_model()

	
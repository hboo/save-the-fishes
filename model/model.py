
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
import h5py 


def build_model():
	# Use VGG16 model trained on Image Net and finetune the top layer
	base_model = applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
	print('Model loaded')
	import pdb;pdb.set_trace()
	#for layer in base_model:
		#Freeze imagenet trained layers
	#	layer.trainable = False
	top_model = Sequential()
	top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
	top_model.add(Dense(256, activation='relu'))
	top_model.add(Dropout(0.5))
	top_model.add(Dense(1, activation='sigmoid'))

	# stick them together
	base_model.add(top_model)
	return base_model




if __name__ == '__main__':
	build_model()


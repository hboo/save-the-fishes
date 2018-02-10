
from sklearn.datasets import load_files
from keras import applications
from keras.utils import np_utils
from keras.layers import Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.models import Model
from keras.preprocessing import image
from tqdm import tqdm
import numpy as np
from glob import glob
import h5py 

def build_model(num_classes):
	# Use VGG16 model trained on Image Net and finetune the top layer
	base_model = applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
	print('Model loaded')
	#import pdb;pdb.set_trace()
	for layer in base_model.layers:
		#Freeze imagenet trained layers
		layer.trainable = False
	last = base_model.output
	top_model = Flatten()(last)
	top_model = Dense(256, activation='relu')(top_model)
	top_model = Dense(num_classes, activation='sigmoid')(top_model)

	model = Model(base_model.input, top_model)

	model.summary()
	return model

if __name__ == '__main__':
	build_model()


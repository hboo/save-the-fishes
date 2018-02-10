from glob import glob
import argparse
from model import *
from train import path_to_tensor
import numpy as np

parser = argparse.ArgumentParser(description='Learn some fish')
parser.add_argument('image')
args = parser.parse_args()

def predict(image):
	model = build_model(15)
	model.load_weights('saved_models/weights.best.from_scratch_2.hdf5')
	tensor = path_to_tensor(image).astype('float32')/255
	prediction = model.predict(tensor)
	res = np.argmax(prediction)

	print(prediction)
	print(res)

if __name__ == '__main__':
	predict(args.image)


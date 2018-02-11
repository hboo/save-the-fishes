from glob import glob
import argparse
from model import *
from train import path_to_tensor
import numpy as np

from fish_info import FISH_INFO

parser = argparse.ArgumentParser(description='Learn some fish')
parser.add_argument('image')
args = parser.parse_args()

def get_fish_name(index):
	path = '../static/fishes/train/*/'
	fish_names = [x.split('/')[-1].replace('train', '').replace('\\', '') for x in glob(path)]
	return fish_names[index]

def predict(image):
	model = build_model(15)
	model.load_weights('saved_models/weights.best.from_scratch_2.hdf5')
	tensor = path_to_tensor(image).astype('float32')/255
	res = np.argmax(model.predict(tensor))

	name = get_fish_name(res) 
	print(name)
	print(FISH_INFO[name])

if __name__ == '__main__':
	predict(args.image)


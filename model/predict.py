from glob import glob

from model import *

def predict():
	fish_names = [item[20:-1] for item in sorted(glob("../static/fishes/train/*/"))]
	print(fish_names)
	model = build_model()
	model.load_weights('saved_models/weights.best.from_scratch.hdf5')


from glob import glob

def predict():
	fish_names = [item[20:-1] for item in sorted(glob("../fishImages_mock/train/*/"))]
	print(fish_names)

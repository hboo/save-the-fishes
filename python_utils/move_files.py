import os

ROOT = '/Users/cindy/Desktop/save-the-fishes/static/train'
DEST = '/Users/cindy/Desktop/save-the-fishes/static/validate'

for directory in os.listdir(ROOT):
    src_files = os.path.join(ROOT, directory, os.listdir(os.path.join(ROOT, directory))[0])
    dest_files = os.path.join(DEST, directory, os.listdir(os.path.join(ROOT, directory))[0])
    print 'Moving %s to %s' % (src_files, dest_files)
    os.rename(src_files, dest_files)

"""
Code adopted from pix2pixHD:
https://github.com/NVIDIA/pix2pixHD/blob/master/data/image_folder.py
"""
import os
from random import shuffle, sample
from pathlib import Path

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP', '.tiff'
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)


def make_dataset(dir, dataset_size = None):
    images = []
    assert os.path.isdir(dir), f'{dir} is not a valid directory'
    dataset_paths = list(Path(dir).glob('**/*'))
    print(dataset_paths[:5])
    shuffle(dataset_paths) # randomly shuffle images from whole dataset
    print(dataset_paths[:5])
    for path in dataset_paths: 
        if dataset_size is not None and len(images) > dataset_size - 1:
            break
        if path.suffix in IMG_EXTENSIONS:
            images.append(path)
    # for root, _, fnames in sorted(os.walk(dir)):
    #     for fname in fnames:
    #         if is_image_file(fname):
    #             path = os.path.join(root, fname)
    #             images.append(path)
    return images


def make_dataset_from_paths_list(paths_file):
    assert os.path.exists(paths_file), f'{paths_file} is not a valid file'
    with open(paths_file, "r") as f:
        paths = f.readlines()
    paths = [p.strip() for p in paths]
    paths = [p for p in paths if is_image_file(p)]
    return paths
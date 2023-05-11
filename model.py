
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

import pathlib

data_dir = pathlib.Path('images')
freshwater = data_dir / 'freshwater'
saltwater = data_dir / 'saltwater'

image_count = len(list(data_dir.glob('*/*/*.png')))
print(image_count)

freshwater_fish = list(freshwater.glob('Fish/*'))
print(freshwater_fish)
Image.open(str(freshwater_fish[0])).show()










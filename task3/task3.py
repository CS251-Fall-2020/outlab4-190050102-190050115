from PIL import Image
import numpy as np
import argparse
from matplotlib import pyplot as plt
from scipy.cluster.vq import kmeans2

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input File")
parser.add_argument("--k", help='Kmeans Contraints')
parser.add_argument("--output", help="Output File")
args = parser.parse_args()

image = Image.open(args.input)

image = np.asarray(image)
len = image.shape[0]
wid = image.shape[1]
channel = image.shape[2]

data = image.reshape(image.shape[0]*image.shape[1], image.shape[2])
data = data.astype('float')


k = int(args.k)
centroid, label = kmeans2(data, k, minit='++')


image_out = image.copy()
for i, _ in enumerate(data):
    image_out[i//512][i%512] = centroid[label[i]]


image = Image.fromarray(image_out, mode='RGB')

image.save(args.output)

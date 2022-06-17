import cv2
import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import glob

# read all images from file
paths = glob.glob('../detect/exp*/*.PNG',recursive=True)

orig = np.array([np.asarray(Image.open(img))  for img in paths])
plt.figure(figsize=(14,15))

for i, img in enumerate(orig[0:16]):

    plt.subplot(3,3,i+1)

    plt.xticks([])

    plt.yticks([])

    plt.grid(False)

    plt.imshow(img)

plt.suptitle("Detection images", fontsize=30)
plt.savefig("detect-image.png")

plt.show()

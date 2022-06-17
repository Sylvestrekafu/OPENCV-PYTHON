import cv2
import matplotlib.pyplot as plt

"""
Une image couleur est constituée de trois cannaux Rouge  ou Red( R), Vert ou Green  (G or V) et Bleue ou Blu (B)
Chacun des canal est représenté en niveau de gris ou en 8 bit

"""

image= cv2.imread("sylvestre.jpg") # read original image ou lecture de l'image originale
image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert the image from BGR channels to RGB channels

imageB =cv2.imread("sylvestre.jpg", 0) # represents Blue channel
imageG =cv2.imread("sylvestre.jpg", 1) # represents Green channel
imageR =cv2.imread("sylvestre.jpg", 2) #represents Red channel
plt.subplot(221),plt.imshow(image), plt.title("RGB image"), plt.axis("off")
plt.subplot(222),plt.imshow(imageB, cmap="gray"), plt.title(" Blue channel"), plt.axis("off")
plt.subplot(223),plt.imshow(imageG, cmap="gray"), plt.title("Green channel"), plt.axis("off")
plt.subplot(224),plt.imshow(imageR, cmap="gray"), plt.title("Red channel"), plt.axis("off")
plt.savefig("imagefromchannels.png")

plt.show()

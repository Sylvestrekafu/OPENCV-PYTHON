import cv2
import matplotlib.pyplot as plt


image =cv2.imread("sylvestre.jpg", cv2.IMREAD_UNCHANGED)
#extract blue channel
blue_channel =image[:,:,0]
#extract green channel
green_channel = image[:,:,1]
#extract red channel
red_channel =image[:,:,2]
plt.subplot(221),plt.imshow(image), plt.title("BGR image"),plt.axis("off")
plt.subplot(222),plt.imshow(blue_channel, cmap="gray"), plt.title("blue channel"), plt.axis("off")
plt.subplot(223),plt.imshow(green_channel, cmap="gray"), plt.title("green channel"), plt.axis("off")
plt.subplot(224),plt.imshow(red_channel, cmap="gray"), plt.title("red red_channel"), plt.axis("off")
plt.show()

import cv2
import matplotlib.pyplot as plt
from matplotlib.pyplot import *
#read image as grey scale
original =cv2.imread("sylvestre.jpg")
original=cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
image = cv2.imread("sylvestre.jpg", cv2.IMREAD_GRAYSCALE)
image1= cv2.imread("sylvestre.jpg")
image1=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# show image
#cv2.imshow("original image", original)
#cv2.imshow("gray", image1)
#cv2.imshow("gray scale", image)


# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# threshold the image
_, th = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY) #  binary threshold
_, th1 = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY_INV) # inverse binary threshold
_, th2 = cv2.threshold(image1, 128, 255, cv2.THRESH_OTSU) # OTSU threshold
#cv2.imshow("threshold", th) # show threshold image
#cv2.imshow("threshold inverse", th1) # show inverse binary threshold
#cv2.imshow("Otsu threshold", th2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Display image
plt.figure(figsize=(15,15))
plt.subplot(331), plt.imshow(original), plt.title("original image"), plt.axis("off")
plt.subplot(332), plt.imshow(image, cmap="gray"), plt.title("gray image"), plt.axis("off")
plt.subplot(333), plt.imshow(image1,cmap="gray"), plt.title("convert image  from BGR to Gray"), plt.axis("off")
plt.subplot(334), plt.imshow(th, cmap="gray"), plt.title("binary image"), plt.axis("off")
plt.subplot(335), plt.imshow(th1, cmap="gray"), plt.title("inverse binary image"), plt.axis("off")
plt.subplot(336), plt.imshow(th2, cmap="gray"), plt.title("Otsu threshold"), plt.axis("off")
plt.savefig("result.png")
plt.show()
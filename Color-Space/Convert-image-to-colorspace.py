import  cv2
import matplotlib.pyplot as plt
# Read and convert image
image = cv2.imread("sylvestre.jpg") # reda image in BGR channels
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert image from BGR channels to RGB channels
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert image from BGR channels to RGB channels
imageHSV= cv2.cvtColor(imageRGB, cv2.COLOR_RGB2HSV) # convert image from RGB channels to HSV chanenels
imageLab = cv2.cvtColor(imageRGB, cv2.COLOR_RGB2Lab) # convert image from RGB channels to Lab channels
imageLUV = cv2.cvtColor(imageRGB, cv2.COLOR_RGB2LUV)
imageYCrCb =cv2.cvtColor(imageRGB, cv2.COLOR_RGB2YCrCb)

# Displays

plt.subplot(331), plt.imshow(image), plt.title("BGR image"), plt.axis("off")
plt.subplot(332), plt.imshow(imageRGB), plt.title("RGB image"), plt.axis("off")
plt.subplot(333), plt.imshow(imageGray, cmap="gray"), plt.title("Gray image"), plt.axis("off")
plt.subplot(334), plt.imshow(imageHSV), plt.title("HSV image"), plt.axis("off")
plt.subplot(335), plt.imshow(imageLab), plt.title("Lab image"),plt.axis("off")
plt.subplot(336), plt.imshow(imageLUV), plt.title("LUV image"),plt.axis("off")
plt.subplot(337), plt.imshow(imageYCrCb), plt.title("YCrCb image"),plt.axis("off")
plt.savefig("color-space-image.png")
plt.show()


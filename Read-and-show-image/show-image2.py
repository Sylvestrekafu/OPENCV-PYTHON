import  cv2
import  matplotlib.pyplot as plt

# read image
image =cv2.imread("sylvestre.jpg")
image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert image from BGR to RGB channels

# show or display image using matplotlib
plt.imshow(image)
plt.show()
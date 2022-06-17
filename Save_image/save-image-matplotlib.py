import  cv2
import  matplotlib.pyplot as plt
from matplotlib.pyplot import *

image =cv2.imread("sylvestre.jpg") # read image

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert image from BGR channels to RGB channels

# Display or show image
plt.figure(figsize=(14,15))
plt.imshow(image)
plt.savefig("saveimage-matplotlib.png")
plt.show()
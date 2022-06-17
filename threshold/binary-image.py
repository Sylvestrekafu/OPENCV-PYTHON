import cv2
#read image as grey scale
original =cv2.imread("sylvestre.jpg")
image = cv2.imread("sylvestre.jpg", cv2.IMREAD_GRAYSCALE)
image1= cv2.imread("sylvestre.jpg")
image1=cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# show image
cv2.imshow("original image", original)
cv2.imshow("gray", image1)
cv2.imshow("gray scale", image)


# define a threshold, 128 is the middle of black and white in grey scale
thresh = 128

# threshold the image
_, th = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY) #  binary threshold
_, th1 = cv2.threshold(image1, 128, 255, cv2.THRESH_BINARY_INV) # inverse binary threshold
_, th2 = cv2.threshold(image1, 128, 255, cv2.THRESH_OTSU) # OTSU threshold
cv2.imshow("threshold", th) # show threshold image
cv2.imshow("threshold inverse", th1) # show inverse binary threshold
cv2.imshow("Otsu threshold", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()
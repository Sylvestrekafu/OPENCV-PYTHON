import cv2

image =cv2.imread("sylvestre.jpg") # read image using cv2.imread()
imsave =cv2.imwrite("imagesave-opencv.png", image) # save  image using cv2.imwrite()
if imsave:
    print("L'image est enregistrée avec succès.")
cv2.waitKey(0)
cv2.destroyAllWindows()
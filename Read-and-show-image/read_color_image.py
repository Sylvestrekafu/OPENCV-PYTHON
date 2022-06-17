import cv2 # import OpenCV
import matplotlib.pyplot as plt

"""
Vous pouvez lire l'image dans un tableau numpy en utilisant la bibliothèque opencv.
Le tableau contient des données au niveau des pixels. Et selon l'exigence,
vous pouvez modifier les données de l'image au niveau du pixel en mettant à jour les valeurs du tableau.
Pour lire une image en Python avec OpenCV, on utilise la fonction cv2.imread(). 
imread() renvoie une matrice 2D ou 3D basée sur le nombre de canaux de couleur présents dans l'image.
"""

image = cv2.imread("sylvestre.jpg") # read image or lire l'image avec la fonction cv.imread()
#Lire l'image couleur or Read Color Image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert the image from BGR to RGB

# display image
plt.imshow(image), plt.title("color-image")
plt.savefig("colorimage.png")
plt.show()

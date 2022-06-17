# Camera calibration
import cv2
import numpy as np
import os
import glob

# Définir les dimensions du damier
CHECKERBOARD = (6,9)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Création d'un vecteur pour stocker les vecteurs de points 3D pour chaque image en damier
objpoints = []
# Création d'un vecteur pour stocker les vecteurs de points 2D pour chaque image de damier
imgpoints = [] 


# Définition des coordonnées du monde pour les points 3D
objp = np.zeros((1, CHECKERBOARD[0]*CHECKERBOARD[1], 3), np.float32)
objp[0,:,:2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None

# Extraction du chemin d'une image individuelle stockée dans un répertoire donné
images = glob.glob('./images/*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Trouvez les coins de l'échiquier
    # Si le nombre désiré de coins est trouvé dans l'image, alors ret = vrai.
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH+
    	cv2.CALIB_CB_FAST_CHECK+cv2.CALIB_CB_NORMALIZE_IMAGE)
    
    """
    Si le nombre désiré de coins est détecté,
    nous affinons les coordonnées des pixels et les affichons 
    sur les images du damier
    """
    if ret == True:
        objpoints.append(objp)
        # Affiner les coordonnées des pixels pour des points 2d donnés.
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        
        imgpoints.append(corners2)

        # Dessiner et afficher les coins
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2,ret)
    
    cv2.imshow('img',img)
    cv2.waitKey(0)

cv2.destroyAllWindows()

h,w = img.shape[:2]

"""
Effectuer l'étalonnage de la caméra en 
transmettant la valeur des points 3D connus (objpoints)
et les coordonnées correspondantes des pixels des 
coins détectés (imgpoints)
"""
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)

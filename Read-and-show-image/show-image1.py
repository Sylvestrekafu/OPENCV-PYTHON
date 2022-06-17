import cv2
# Display image using opencv
"""
cv2.waitKey(0) est important pour maintenir l'exécution du programme python à cette instruction,
afin que la fenêtre d'image reste visible. Si vous ne fournissez pas cette instruction,
cv2.imshow() s'exécute en une fraction de seconde et le programme ferme toutes les fenêtres qu'il a ouvertes,
ce qui rend presque impossible de voir l'image sur la fenêtre.
"""

image =cv2.imread("sylvestre.jpg") #read image

cv2.imshow("image", image)#show image
cv2.waitKey(0)  # waits untils a key is pressed or attend qu'une touche soit pressée ou appuyer
#cv2.destroyAllWindows() # destroys the window showing image or détruit la fenêtre montrant l'image
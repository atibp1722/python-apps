import cv2

# read named image in grayscale
img = cv2.imread("galaxy.jpg", 0)
# resize the image
resized_image = cv2.resize(img, (800, 500))
# open resized image in new window
cv2.imshow("Viewer", resized_image)
cv2.waitKey(2000)
# close all windows
cv2.destroyAllWindows()

input("Press enter to exit")
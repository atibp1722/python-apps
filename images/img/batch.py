import cv2
import glob

# all files ending with jpg
images = glob.glob("*.jpg")
# iterate all image files found
for image in images:
    # read into grayscale and size them 100x100
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    # show new image in window
    cv2.imshow("Viewer", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # save new image
    cv2.imwrite("resized"+image, re)

input("Press enter to exit")
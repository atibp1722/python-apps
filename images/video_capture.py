import cv2, time

# statrt using the device webcam
video = cv2.VideoCapture(0)
# track number of frames
a = 0
# continuosly capture frames
while True:
    # increase frame counter
    a = a+1
    # check frame for image
    check, frame = video.read()
    # print status and array
    print(check)
    print(frame)
    # convert to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    # show frame
    cv2.imshow("Video", gray)
    # loop exit condition
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

print(a)
# stop webcam 
video.release()
# close all windows
cv2.destroyAllWindows()
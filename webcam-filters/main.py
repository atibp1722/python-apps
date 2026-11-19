import cv2
import tkinter as tk
import numpy as np
from tkinter import ttk, filedialog
from threading import Thread

curr_filter = "normal"
# frame to save
curr_frame = None
# device webcam
cap = cv2.VideoCapture(0)

# function to apply filter to image
def applyFilter(frame, filtername):
    # convert image to grauscale
    if filtername == "Grayscale":
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif filtername == "Blur":
        # smooth image using Gaussian blur
        return cv2.GaussianBlur(frame, (15, 15), 0)
    elif filtername == "Edge":
        # detect image boundary and highlight edges
        return cv2.Canny(frame, 100, 200)
    elif filtername == "Cartoon":
        # form a cartoon image
        color = cv2.bilateralFilter(frame, 9, 250, 250)
        # making image look vintage
        return (color // 64) * 64
    return frame

# function to keep webcam running for image capture
def startCamera():
    global curr_filter, cap
    while True:
        # read frame
        ret, frame = cap.read()
        if not ret:
            break
        frame = applyFilter(frame, curr_filter)
        # if 2D convert back to original 
        if len(frame.shape) == 2:
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Camera filters", frame)
        # exit when 1 pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    # close all after exit
    cv2.destroyAllWindows()

# filter when button clicked
def changeFilter(filterName):
    global curr_filter
    curr_filter = filterName

# function to save a frame 
def saveImage():
    global curr_frame
    if curr_frame is not None:
        # save frame as jpg or png
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        if file_path:
            cv2.imwrite(file_path, curr_frame)

# tkinter gui
root = tk.Tk()
root.title("Webcam Filters")
root.geometry("350x500")
lable = tk.Label(root, text="Select filter options", font=("Arial", 14))
lable.pack(pady = 10)
# list for filter option
filters = ["Normal", "Grayscale", "Blur", "Edge", "Cartoon"]
# iterate and create button for each filter
for f in filters:
    btn = ttk.Button(root, text=f, command=lambda f=f: changeFilter(f))
    btn.pack(pady = 7)
save = ttk.Button(root, text="Save", command=saveImage)
save.pack(pady=10)
# run webcam as independent thread
Thread(target=startCamera, daemon=True).start()
root.mainloop() 
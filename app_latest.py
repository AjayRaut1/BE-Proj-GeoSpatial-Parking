import streamlit as st
import cv2
import csv
import numpy as np

# Variable declaration
class spots:
    loc = 0

def drawRectangle(img, a, b, c, d, lowThreshold, highThreshold, min_pixels, max_pixels):
    # cutting images
    sub_img = img[b:b + d, a:a + c]

    # extracting edges
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)

    # counting white pixels
    pix = cv2.countNonZero(edges)

    if min_pixels <= pix <= max_pixels:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

def callback(foo):
    pass

# dumping spot coordinates into list
with open('data/rois.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

# converting values to integer
rois = [[int(float(j)) for j in i] for i in rois]

def app():
    st.title("Parking Spot Detector")

    # Create sliders for parameters
    lowThreshold = st.slider("Threshold 1", 0, 700, 186, step=1)
    highThreshold = st.slider("Threshold 2", 0, 700, 122, step=1)
    min_pixels = st.slider("Min Pixels", 0, 1500, 100, step=1)
    max_pixels = st.slider("Max Pixels", 0, 1500, 323, step=1)

    # Live feed
    stop_processing = False
    camera_key = 0  # Adding a unique key for the camera input widget
    while True:
        frame = st.camera_input("Camera")
        frame = st.camera_input("Camera", key=f"camera_input_{camera_key}")
        camera_key += 1  # Increment key after each frame
        
        if frame is None:
            st.warning("No camera input detected.")
            continue

        # Setting number of spots to 0
        spots.loc = 0

        # Convert the frame to OpenCV format
        img = cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR)

        for i in range(len(rois)):
            drawRectangle(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3], lowThreshold, highThreshold, min_pixels, max_pixels)

        # Adding the number of available spots
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Available spots: ' + str(spots.loc), (10, 30), font, 1, (0, 255, 0), 3)

        # Display the processed frame
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), channels="RGB")

        # Check if the user wants to stop
        if st.button("Stop Processing"):
            stop_processing = True
            break

    if stop_processing:
        st.warning("Processing stopped.")

if __name__ == "__main__":
    app()

import streamlit as st
import cv2
import csv
import numpy as np
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av

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

class VideoTransformer(VideoProcessorBase):
    def __init__(self):
        self.lowThreshold = 186
        self.highThreshold = 122
        self.min_pixels = 100
        self.max_pixels = 323

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # Setting number of spots to 0
        spots.loc = 0

        for i in range(len(rois)):
            drawRectangle(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3], self.lowThreshold, self.highThreshold, self.min_pixels, self.max_pixels)

        # Adding the number of available spots
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Available spots: ' + str(spots.loc), (10, 30), font, 1, (0, 255, 0), 3)

        return av.VideoFrame.from_ndarray(img, format="bgr24")

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

    # Start the webcam stream
    webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=VideoTransformer)
    
    if webrtc_ctx.video_processor:
        webrtc_ctx.video_processor.lowThreshold = lowThreshold
        webrtc_ctx.video_processor.highThreshold = highThreshold
        webrtc_ctx.video_processor.min_pixels = min_pixels
        webrtc_ctx.video_processor.max_pixels = max_pixels

if __name__ == "__main__":
    app()

# importing
import cv2
import csv

# selecting video source
VIDEO_SOURCE = 0

# recording
cap = cv2.VideoCapture(VIDEO_SOURCE)
suc, image = cap.read()

# save first frame
cv2.imwrite("frame0.jpg", image)
img = cv2.imread("frame0.jpg")

# get the regions of interest
r = cv2.selectROIs('ROI Selector', img, showCrosshair=False, fromCenter=False)

# convert to list
rlist = r.tolist()
print(rlist)

# writing list to csv file
with open('data/rois.csv', 'w', newline='') as outf:
  csvw = csv.writer(outf)
  csvw.writerows(rlist)

# THE END
cap.release()
cv2.destroyAllWindows()

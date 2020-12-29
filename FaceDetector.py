import argparse
import json
import os
import cv2
from os import listdir
from os.path import isfile, join

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("P")
    args = parser.parse_args()
    return args

args = parse_args()
# Code reference : https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81
json_list = []
#load the files in the given folder
onlyfiles = [f for f in listdir('{}'.format(args.P)) if isfile(join('{}'.format(args.P), f))]
# Load the cascade
face_cascade = cv2.CascadeClassifier('.\ModelFiles\haarcascade_frontalface_default.xml')
# Read the input image
for i in range(len(onlyfiles)):
    img = cv2.imread('{}\{}'.format(args.P,onlyfiles[i]),0)
    faces = face_cascade.detectMultiScale(img, 1.05, 5)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        element = {"iname": "{}".format(onlyfiles[i]), "bbox": [int(x),int(y),int(w),int(h)]}
        json_list.append(element)

#the result json file name
output_json = "results.json"

#print(json_list)
#dump json_list to result.json
with open(output_json, 'w') as f:
    json.dump(json_list, f)


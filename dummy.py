import cozmo
import time
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

def stupid(robot: cozmo.robot.Robot):
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True

    for count in range(25):
        while not robot.world.latest_image:
            time.sleep(1.0)

        imageFromCozmo = robot.world.latest_image.raw_image
        image = cv2.cvtColor(np.array(imageFromCozmo),cv2.COLOR_RGB2GRAY)

        maskArea = np.array([[(125, 200),(175,100), (450, 100), (500, 225)]], dtype=np.int32)

        blank = np.zeros_like(image)

        mask = cv2.fillPoly(blank, maskArea, 255)

        maskedImage = cv2.bitwise_and(image, mask)

        image_canny = cv2.Canny(maskedImage,50,200,apertureSize=3)

        rho = 2
        theta = np.pi/180
        threshold = 50
        minLine = 50
        maxLine = 8


        #I'm not sure about these lines or what they do exactly
        lines = cv2.HoughLinesP(image_canny, rho, theta, threshold, np.array([]), minLineLength=minLine, maxLineGap=maxLine)
        #lines = cv2.HoughLines(image_canny,1,np.pi/180,200)

        try:
            if lines[0,0,0] < 150: # turn left slightly
                robot.drive_wheels(10, 15)
            elif lines[1,0,0] > 450: # turn right slightly
                robot.drive_wheels(15, 10)

            else: # go straight
                robot.drive_wheels(10, 10)
        except:
            print("didnt find any")

        #these code isn't required, just allows you to view the camera feed and prints out the line its following
        plt.imshow(image_canny)
        plt.imshow(image,cmap="gray")
        plt.show()
        cv2.waitKey(3)
        print(lines)

#if you wanted to use cozmo built in viewer you would do the following
#cozmo.run_program(stupid, use_viewer = True)
cozmo.run_program(stupid)

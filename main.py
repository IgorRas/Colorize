import cv2
import sys
import PySimpleGUI as sg
import numpy as np


def select_image():
    filename = sg.popup_get_file('file to open', no_window=True)
    return filename


im_gray = cv2.imread(select_image(), cv2.IMREAD_GRAYSCALE)
im_gray_3channel = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_RAINBOW)

fin = np.concatenate((im_gray_3channel, im_color), axis=1)

while True:
    cv2.imshow("Result", fin)
    cv2.waitKey(0)
    sys.exit()

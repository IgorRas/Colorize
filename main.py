import cv2
import sys
import PySimpleGUI as sg
import numpy as np
import os
from PIL import Image


def select_image():
    filename = sg.popup_get_file('file to open', no_window=True)
    return filename


def images():
    directory = 'images'
    for filename in os.listdir(directory):
        pathoriginal = os.path.join(directory, filename)
        if os.path.isfile(pathoriginal):
            if pathoriginal[-3:] == 'jpg':
                os.remove(pathoriginal)


def select_type():
    layout = [
        [sg.Text('Typ:')],
        [sg.Radio('AUTUMN ', "RADIO1", default=True),
         sg.Radio('BONE', "RADIO1", default=False),
         sg.Radio('JET', "RADIO1", default=False),
         sg.Radio('WINTER', "RADIO1", default=False),
         sg.Radio('RAINBOW', "RADIO1", default=False),
         sg.Radio('OCEAN', "RADIO1", default=False),
         sg.Radio('SUMMER', "RADIO1", default=False),
         sg.Radio('SPRING', "RADIO1", default=False),
         sg.Radio('COOL', "RADIO1", default=False),
         sg.Radio('HSV', "RADIO1", default=False),
         sg.Radio('PINK', "RADIO1", default=False),
         sg.Radio('HOT', "RADIO1", default=False),
         sg.Radio('PARULA', "RADIO1", default=False),
         sg.Radio('MAGMA', "RADIO1", default=False),
         sg.Radio('INFERNO', "RADIO1", default=False),
         sg.Radio('PLASMA', "RADIO1", default=False),
         sg.Radio('VIRIDIS', "RADIO1", default=False),
         sg.Radio('CIVIDIS', "RADIO1", default=False),
         sg.Radio('TWILIGHT', "RADIO1", default=False),
         sg.Radio('TWILIGHT_SHIFTED', "RADIO1", default=False),
         sg.Radio('TURBO', "RADIO1", default=False),
         sg.Radio('DEEPGREEN', "RADIO1", default=False)],
        [sg.Submit()]
    ]
    n_window = sg.Window('Podaj dane', layout)
    event, values = n_window.read()
    n_window.close()
    return values


images()
values = select_type()
value = 0
for i in range(21):
    value += int(values[i])*i

im_gray = cv2.imread(select_image(), cv2.IMREAD_GRAYSCALE)
im_gray_3channel = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR)
im_color = cv2.applyColorMap(im_gray, value)

fin = np.concatenate((im_gray_3channel, im_color), axis=1)

while True:
    cv2.imshow("Result", fin)
    cv2.waitKey(0)
    sys.exit()

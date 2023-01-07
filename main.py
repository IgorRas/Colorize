import cv2
import PySimpleGUI as sg
import numpy as np
import sys


# wybranie obrazu do obróbki
def select_image():
    filename = sg.popup_get_file('file to open', no_window=True) # ścieżka do wybranego obrazu
    return filename


# utworzenie ui do wybrania opcji oraz jej wybranie
def select_type():
    layout = [ # lista dostępnych opcji koloryzacji
        [[sg.Radio('AUTUMN ', "RADIO1", default=True, size=(15, 4)), sg.Image('images/colorscale_autumn.png')],
         [sg.Radio('BONE', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_bone.png')],
         [sg.Radio('JET', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_jet.png')],
         [sg.Radio('WINTER', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_winter.png')],
         [sg.Radio('RAINBOW', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_rainbow.png')],
         [sg.Radio('OCEAN', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_ocean.png')],
         [sg.Radio('SUMMER', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_summer.png')],
         [sg.Radio('SPRING', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_spring.png')],
         [sg.Radio('COOL', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_cool.png')],
         [sg.Radio('HSV', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_HSV.png')],
         [sg.Radio('PINK', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_pink.png')],
         [sg.Radio('HOT', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_hot.png')],
         [sg.Radio('PARULA', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_parula.png')],
         [sg.Radio('MAGMA', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_magma.png')],
         [sg.Radio('INFERNO', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_inferno.png')],
         [sg.Radio('PLASMA', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_plasma.png')],
         [sg.Radio('VIRIDIS', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_viridis.png')],
         [sg.Radio('CIVIDIS', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_cividis.png')],
         [sg.Radio('TWILIGHT', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_twilight.png')],
         [sg.Radio('TWILIGHT_SHIFTED', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_twilight_shifted.png')],
         [sg.Radio('TURBO', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_turbo.png')],
         [sg.Radio('DEEPGREEN', "RADIO1", default=False, size=(15, 4)), sg.Image('images/colorscale_deepgreen.png')]],
        [sg.Submit()]
    ]
    n_window = sg.Window('Podaj dane', layout)
    event, values = n_window.read()
    n_window.close()
    if values[0] is None:
        sys.exit()
    return values # zwraca wybraną listę booli z wartością 1 dla wybranej opcji


# obróbka wybranego obrazu zgodnie z wybraną opcją
def main():
    values = select_type()
    value = 0
    for i in range(0, 44, 2):
        value += int(int(values[i])*i/2) # konwersja listy booli na liczbę odpowiadającej wybranej opcji

    im_gray = cv2.imread(select_image(), cv2.IMREAD_GRAYSCALE) # początkowy wczytany obraz
    im_gray_3channel = cv2.cvtColor(im_gray, cv2.COLOR_GRAY2BGR) # konwersja kopii oryginału na typ obrazu z trzema kanałami koloru
    im_color = cv2.applyColorMap(im_gray, value) # koloryzacja zgodna z wybraną opcją

    fin = np.concatenate((im_gray_3channel, im_color), axis=1) # kolarz porównujący oryginał z koloryzowanym
    return fin


# wyświetlenie wyniku
while True:
    cv2.imshow("Result", main())
    cv2.setWindowProperty("Result", cv2.WND_PROP_TOPMOST, 1)
    cv2.waitKey(0)

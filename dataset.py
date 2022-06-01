import time
from tkinter.filedialog import Open
from numpy import append
import pyautogui
import pyperclip
from PIL import Image, ImageChops
import pytesseract
import cv2
import openpyxl
import numpy

pyautogui.PAUSE = 1
#abre o windows
pyautogui.press ("win")
pyautogui.PAUSE = 2.5
pyautogui.hotkey ("enter")
pyautogui.PAUSE = 2.5

#pyperclip.copy('https://www.tiktok.com/search/user?lang=pt-BR&q=itau&t=1651634256929')
pyperclip.copy('https://www.tiktok.com/@itau?lang=pt-BR')
pyautogui.hotkey("ctrl","v")
pyautogui.PAUSE = 4
pyautogui.press("enter")
pyautogui.PAUSE = 4
time.sleep(3)

#printa o local desejado da tela
pyautogui.screenshot('logoItau.png',region=(262.5,192,119,124))

#im2 = pyautogui.screenshot('imagemItau.jpg')


#pyautogui.click(483,269) || clica na posição passada como parametro (comentado)
pyautogui.PAUSE = 2.5

#converte a imagem colorida para um novo arquivo , no caso , para Cinza
img = Image.open('logoItau.png') #.convert('L')
img.save('logoItau.png')
time.sleep(7)
###########################################################

pyautogui.PAUSE = 1
#abre o windows
pyautogui.press ("win")
pyautogui.PAUSE = 2.5
pyautogui.hotkey ("enter")
pyautogui.PAUSE = 2.5

#pyperclip.copy('https://www.tiktok.com/search/user?lang=pt-BR&q=itau&t=1651634256929')
pyperclip.copy('https://www.tiktok.com/@itauana_cdo')
pyautogui.hotkey("ctrl","v")
pyautogui.PAUSE = 4
pyautogui.press("enter")
pyautogui.PAUSE = 4
time.sleep(3)

#printa o local desejado da tela
pyautogui.screenshot('logoItauana.png',region=(262.5,192,119,124))

#im2 = pyautogui.screenshot('imagemItau.jpg')


#pyautogui.click(483,269) || clica na posição passada como parametro (comentado)
pyautogui.PAUSE = 2.5

#converte a imagem colorida para um novo arquivo , no caso , para Cinza
img = Image.open('logoItauana.png') #.convert('L')
img.save('logoItauana.png')

time.sleep(7)
##############################################################

pyautogui.press ("win")
pyautogui.PAUSE = 2.5
pyautogui.hotkey ("enter")
pyautogui.PAUSE = 2.5

#pyperclip.copy('https://www.tiktok.com/search/user?lang=pt-BR&q=itau&t=1651634256929')
pyperclip.copy('https://www.tiktok.com/@itaucol')
pyautogui.hotkey("ctrl","v")
pyautogui.PAUSE = 4
pyautogui.press("enter")
pyautogui.PAUSE = 4
time.sleep(3)

#printa o local desejado da tela
pyautogui.screenshot('itaucol.png',region=(262.5,192,119,124))

#im2 = pyautogui.screenshot('imagemItau.jpg')


#pyautogui.click(483,269) || clica na posição passada como parametro (comentado)
pyautogui.PAUSE = 2.5

#converte a imagem colorida para um novo arquivo , no caso , para Cinza
img = Image.open('itaucol.png') #.convert('L')
img.save('itaucol.png')
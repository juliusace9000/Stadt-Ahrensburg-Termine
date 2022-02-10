from concurrent.futures import thread
import time
from bib import getTermine
from PIL import Image
from PIL import ImageChops
from bot import notification
import threading
import os
time.sleep(10)

c = 0
while True:
    try:
        os.remove("2.png")
        os.rename("1.png", "2.png")
    except:
        try:
            os.rename("1.png", "2.png")
        except:
            notification("Problem mit den Bildern")
    try:
        img1 = Image.open("2.png").convert('RGB')
    except:
        notification("großes Problem mit den Bildern")
    getTermine()
    print("erfolg")
    img2 = Image.open("1.png").convert('RGB')
    diff = ImageChops.difference(img1, img2)
    if diff.getbbox():
        print("Bilder sind unterschiedlich")
        notification("Neuer Termin online!!\n https://reservation.frontdesksuite.com/ahrensburg/ahrensburg/Home/Index?pageId=10963985-24b5-4b55-9b81-a2f9c895905e&culture=de&uiCulture=de")
    else:
        print("Bilder sind gleich")
    time.sleep(60)
    c+=1
    if c%10==0:
        notification("Bot läuft noch!")
        c=1

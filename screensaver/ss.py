#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pyautogui
import io
import sys
#from pathlib import Path
import os
import time
import datetime

def image2bytes(image) -> bytes:
    img = image

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr

def writeFileBytes(fileName : str, b : bytes) -> None:
    with open(fileName, 'wb') as temp:
        temp.write(b)

def saveScreenshot(path : str):
    m1 = pyautogui.screenshot()
    ma = image2bytes(m1)
    writeFileBytes(path, ma)

def getImageName():
    now = datetime.datetime.now()
    res = ""
    res += str(now.hour) + "_"
    res += str(now.minute) + "_"
    res += str(now.second) + ".png"
    return res

if __name__ == "__main__":
    STDIMGNAME = "_10.png"
    dir = sys.argv[1]
    dir = os.path.abspath(dir)
    while(True):
        out1 = os.path.join(dir, getImageName())
        out2 = os.path.join(dir, STDIMGNAME)

        saveScreenshot(out1)
        saveScreenshot(out2)
        time.sleep(10)

import time
import pyautogui as pag
import cv2 as cv
import numpy as np

def getScreenShot() -> cv.Mat:
    screen = pag.screenshot()
    screen = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    return screen

def object_match(src: cv.Mat, template: cv.Mat) -> list:
    result: list = []
    img_rgb = src 
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.99
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        result.append([pt[0] + w / 2, pt[1] + h / 2])
    return result

def clickMouseButton(x: int, y: int, btn: str) -> bool:
    if not pag.onScreen(x, y):
        return False
    pag.click(x, y, button=btn)
    return True

def pipeline():
    pag.alert("把Microsoft To Do的窗口全屏，然后按确定")
    while True:
        index: list = object_match(getScreenShot(), cv.imread('Pic/item.png'))[0]
        clickMouseButton(index[0], index[1], "Right")
        time.sleep(0.5)
        index = object_match(getScreenShot(), cv.imread("Pic/trashBin.png"))[0]
        clickMouseButton(index[0], index[1], "Left")
        clickMouseButton(index[0], index[1], "Left")
        time.sleep(0.5)
        index = object_match(getScreenShot(), cv.imread("Pic/delete.png"))[0]
        clickMouseButton(index[0], index[1], "Left")
        time.sleep(0.5)
    
pipeline()

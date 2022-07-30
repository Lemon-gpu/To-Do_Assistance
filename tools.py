import pyautogui as pag
import cv2 as cv
import numpy as np
import datetime

def getScreenShot() -> cv.Mat:
    screen = pag.screenshot()
    screen = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    return screen

def objectMatch(src: cv.Mat, template: cv.Mat) -> list:
    result: list = []
    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(src, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.99
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        result.append([pt[0] + w / 2, pt[1] + h / 2])
    return result

def clickMouseButton(x: int, y: int, btn: str) -> bool:
    if not pag.onScreen(x, y):
        return False
    pag.click(x, y, button=btn)
    if btn.lower() == "left":
        pag.click(x, y, button=btn)
    return True

def getToday() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d")
    
def init():
        pag.alert("把Microsoft To Do的窗口全屏，然后按确定")
    
init()
import atexit
import pyautogui as pag
import cv2 as cv
import numpy as np
import datetime

def getScreenShot() -> cv.Mat: #获取屏幕截图
    screen = pag.screenshot()
    screen = cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    return screen

def objectMatch(src: cv.Mat, template: cv.Mat, threshold: float = 0.99) -> list: #匹配图像
    result: list = []
    src = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(src, template, cv.TM_CCOEFF_NORMED)
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        result.append([pt[0] + w / 2, pt[1] + h / 2])
    return result

def clickMouseButton(x: int, y: int, btn: str, times: int = 1) -> bool: #点击鼠标
    if not pag.onScreen(x, y):
        return False
    pag.click(x, y, button=btn, clicks=times)
    return True

def getToday() -> str: #获取今天的日期
    return datetime.datetime.now().strftime("%Y-%m-%d")
    
def constructor(): #构造函数
    pag.alert("把Microsoft To Do的窗口全屏，然后按确定")

@atexit.register #退出时调用
def destructor(): #析构函数
    pag.alert("已完成")

    
constructor()
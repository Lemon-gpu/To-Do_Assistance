from tools import *
import pyautogui as pag
import time

def rename():
    index = objectMatch(getScreenShot(), cv.imread('Pic/template.png'))[0]
    clickMouseButton(index[0], index[1], "Right")
    time.sleep(0.5)

    index = objectMatch(getScreenShot(), cv.imread("Pic/copy.png"))[0]
    clickMouseButton(index[0], index[1], "Left")
    time.sleep(0.5)

    index = objectMatch(getScreenShot(), cv.imread("Pic/templateCopy.png"))[0]
    clickMouseButton(index[0], index[1], "Left")
    time.sleep(0.5)

    index = objectMatch(getScreenShot(), cv.imread("Pic/templateCopy.png"))[0]
    clickMouseButton(index[0], index[1], "Right")
    time.sleep(0.5)

    index = objectMatch(getScreenShot(), cv.imread("Pic/Rename.png"))[0]
    clickMouseButton(index[0], index[1], "Left")
    time.sleep(0.5)

    pag.typewrite(getToday(), interval=0.1)
    time.sleep(0.5)

    pag.press("enter")

def addToToday():
    indexs = objectMatch(getScreenShot(), cv.imread('Pic/circle.png'))
    for index in indexs:
        clickMouseButton(index[0], index[1], "Right")
        clickMouseButton(index[0], index[1], "Right")
        time.sleep(0.5)

        todayList = objectMatch(getScreenShot(), cv.imread("Pic/today.png"))
        for today in todayList:
            if today[0] < 100:
                continue
            clickMouseButton(today[0], today[1], "Left")
            time.sleep(0.5)
        time.sleep(0.5)

def pipeline():
    rename()
    addToToday()
    pag.alert("已完成")

pipeline()


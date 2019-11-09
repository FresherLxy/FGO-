import time
import pyautogui
import random
import easygui
def OpenGame(): #第一次进游戏需要将页面打开至选择助战
    pyautogui.click(516,1057)
    time.sleep(1)
    pyautogui.hotkey('F11')
    time.sleep(1) #将页面放大
def choicesupport():
    while True:
        supportlocation = pyautogui.locateOnScreen("D:\PycharmFeil\FGOAutoBattle\斯卡蒂图标.png",grayscale = False)
        time.sleep(3)
        pyautogui.scroll(-500)
        time.sleep(1)
        if supportlocation != None:
            pyautogui.scroll(500)
            time.sleep(1)
            break
    supportx,supporty = pyautogui.center(supportlocation)
    pyautogui.click(supportx,supporty)
    time.sleep(2)
    pyautogui.click(1786,1017)
def recognize(): #识别画面是否可以点击技能
    while True:
        Battlestart = pyautogui.locateOnScreen("D:\PycharmFeil\FGOAutoBattle\游戏界面截图.png")
        if Battlestart != None:
            break
    time.sleep(2)
def BattleOne():
    battleone = {"99,865":"1",'955,644':'2.5',"727,866":"2.5",'1062,863':'1',"956,644":"2.5",'1793,471':'1',"1497,470":"1",'957,644':'2.3'}
    for i in battleone:  #使用循环和字典实现点击与延迟
        x,y = eval(i)
        pyautogui.click(x+random.randint(20,30),y+random.randint(10,20))
        time.sleep(eval(battleone[i]))
def Battletwo():
    battletwo = {'391,870':'0.5','955,644':'2.5'}
    for h in battletwo:
        i,j = eval(h)
        pyautogui.click(i+random.randint(10,25),j+random.randint(10,25))
        time.sleep(eval(battletwo[h]))
def Battlethree():
    battlethree = {'1341,871':'0.5','955,644':'2.5','248,863':'2.5','582,867':'2.5','1197,865':'2.5'}
    for l in battlethree:
        m,n = eval(l)
        pyautogui.click(m+random.randint(10,15),n+random.randint(10,15))
        time.sleep(eval(battlethree[l]))
def Clickcard():
    card = {'1710,913':'2',"964,308":"0.25",'959,725':'0.25',"1349,764":"0.25"}
    for d in card:
        e,f = eval(d)
        pyautogui.click(e+random.randint(10,20),f+random.randint(10,20))
        time.sleep(eval(card[d]))
def finishgame():
    while True:
        finish = pyautogui.locateOnScreen('D:\PycharmFeil\FGOAutoBattle\结束战斗.png')
        time.sleep(3)
        if finish != None:
            pyautogui.click(x = random.randint(100,900),y = random.randint(100,700),clicks = 3, interval = 1)
            time.sleep(1)
            break
    pyautogui.click(1792,1006)
    time.sleep(10)
def clickcheckpoint():
    pyautogui.click(1435+random.randint(20,40),309+random.randint(10,40))
    time.sleep(2)
def main():
    choicesupport()
    recognize()
    BattleOne()
    Clickcard()
    recognize()
    Battletwo()
    Clickcard()
    recognize()
    Battlethree()
    Clickcard()
    finishgame()
    clickcheckpoint()
number = input('请输入你想运行的次数')
OpenGame()
for i in range(eval(number)):
    main()

import time
import pyautogui
import random #带入随机数主要是防检测
def OpenGame(): #最大化模拟器
    pyautogui.click(516,1057)
    time.sleep(1)
    pyautogui.hotkey('F11')
    time.sleep(1)
def choicesupport(): #使用pyautogui.locateOnScreen识别选择斯卡蒂助战
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
def BattleOne(): #使用字典与循环实现点击技能
    #从左至右分别是斯卡蒂一技能，伯爵图标，伯爵黄金率，斯卡蒂（助战）一技能，伯爵图标，御主技能，充能，伯爵
    battleone = {"99,865":"1",'955,644':'2.5',"727,866":"2.5",'1062,863':'1',"956,644":"2.5",'1793,471':'1',"1497,470":"1",'957,644':'2.3'}
    for i in battleone:
        x,y = eval(i)
        pyautogui.click(x+random.randint(20,30),y+random.randint(10,20))
        time.sleep(eval(battleone[i]))
def Battletwo():
    #从左至右分别是斯卡蒂三技能，伯爵图标
    battletwo = {'391,870':'0.5','955,644':'2.5'}
    for h in battletwo:
        i,j = eval(h)
        pyautogui.click(i+random.randint(10,25),j+random.randint(10,25))
        time.sleep(eval(battletwo[h]))
def Battlethree():
    #从左至右分别是斯卡蒂（助战）三技能，伯爵图标，斯卡蒂二技能，伯爵一技能，斯卡蒂（助战）二技能
    battlethree = {'1341,871':'0.5','955,644':'2.5','248,863':'2.5','582,867':'2.5','1197,865':'2.5'}
    for l in battlethree:
        m,n = eval(l)
        pyautogui.click(m+random.randint(10,15),n+random.randint(10,15))
        time.sleep(eval(battlethree[l]))
def Clickcard():
    #从左至右分别是伯爵宝具卡，第三张卡，第四张卡
    card = {'1710,913':'2',"964,308":"0.25",'959,725':'0.25',"1349,764":"0.25"}
    for d in card:
        e,f = eval(d)
        pyautogui.click(e+random.randint(10,20),f+random.randint(10,20))
        time.sleep(eval(card[d]))
def finishgame(): #使用pyautogui.locateOnScreen识别结束战斗结算页面，点击进入下一步
    while True:
        finish = pyautogui.locateOnScreen('D:\PycharmFeil\FGOAutoBattle\结束战斗.png')
        time.sleep(3)
        if finish != None:
            pyautogui.click(x = random.randint(100,900),y = random.randint(100,700),clicks = 3, interval = 1)
            time.sleep(1)
            break
    pyautogui.click(1792,1006)
    time.sleep(10) #战斗结算页面转回选择关卡页面的等待时间，如果提前结束改这儿
def clickcheckpoint(): #选择上一次战斗的关卡
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
number = input('请输入你想运行的次数') #关卡战斗几次（不能超过体力的最大值，没有设置自动恰苹果）
OpenGame()
for i in range(eval(number)):
    main()

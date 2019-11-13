import easygui
import random
import time
import pyautogui
import datetime
teamsetting = easygui.indexbox(msg = '选择你的队伍',title = '队伍设置',choices = ['满破宝石+极地服/初始服','满破宝石+2004','满破宝石+不用衣服','宝石+梅林+换人服','宝石+充能服','50%NP礼装+孔明+换人'])
numberofbattle = easygui.integerbox(msg = '请输入你想循环的次数',title = '战斗次数')
#伯爵+wcba+满破宝石+初始服/极地服
skillspositiononeturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1040,840':'1',"971,640":'3'}
skillspositiononeturntwo = {'360,840':'1',"970,650":"3"}
skillspositiononeturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3',"1790,470":"1",'1480,480':'1',"972,651":"3"}
#伯爵+wcba+满破宝石+2004
skillspositiontwoturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1040,840':'1',"971,640":'3'}
skillspositiontwoturntwo = {'360,840':'1',"970,650":"3"}
skillspositiontwoturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3',"1790,470":"1",'1360,470':'1',"972,651":"3"}
#伯爵+wcba+满破宝石+不使用衣服
skillspositionthreeturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1040,840':'1',"971,640":'3'}
skillspositionthreeturntwo = {'360,840':'1',"970,650":"3"}
skillspositionthreeturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3'}
#伯爵+wcba+宝石+梅林+换人服
skillspositionfourturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1041,842':'3',"1790,470":"1",'1630,460':'1',"800,520":"0.5",'1100,520':'0.5',"960,950":"10",'1040,840':'1',"971,640":'3'}
skillspositionfourturntwo = {'360,840':'1',"970,650":"3"}
skillspositionfourturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3'}
#伯爵+wcba+宝石+充能服
skillspositionfiveturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1390,840':'1',"971,640":'3',"1790,470":"1",'1480,480':'1',"972,561":"3"}
skillspositionfiveturntwo = {'360,840':'1',"970,650":"3"}
skillspositionfiveturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3'}
#伯爵+wcba+孔明+宝石+换人
skillspositionsixturnone = {'70,840':'1',"970,640":"3","700,840":"3",'1041,842':'1',"969,949":"3",'1180,841':'3',"1319,840":"3","1790,470":"1",'1630,460':'1',"800,520":"0.5",'1100,520':'0.5',"960,950":"10",'1040,840':'1',"971,640":'3'}
skillspositionsixturntwo = {'360,840':'1',"970,650":"3"}
skillspositionsixturnthree = {'220,840':'3',"550,840":"3",'1190,840':'3',"1320,840":"1",'970,650':'3'}
whichteam1 = {}
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
    global whichteam1
    for i in whichteam1:
        x,y = eval(i)
        pyautogui.click(x+random.randint(20,30),y+random.randint(10,20))
        time.sleep(eval(whichteam1[i]))
    time.sleep(1)
def Battletwo():
    #从左至右分别是斯卡蒂三技能，伯爵图标
    global whichteam2
    for h in whichteam2:
        i,j = eval(h)
        pyautogui.click(i+random.randint(10,25),j+random.randint(10,25))
        time.sleep(eval(whichteam2[h]))
    time.sleep(1)
def Battlethree():
    #从左至右分别是斯卡蒂（助战）三技能，伯爵图标，斯卡蒂二技能，伯爵一技能，斯卡蒂（助战）二技能
    global whichteam3
    for l in whichteam3:
        m,n = eval(l)
        pyautogui.click(m+random.randint(10,15),n+random.randint(10,15))
        time.sleep(eval(whichteam3[l]))
    time.sleep(1)
def Clickcard():
    #从左至右分别是伯爵宝具卡，第三张卡，第四张卡
    card = {'1710,913':'2',"964,308":"0.25",'959,725':'0.25',"1349,764":"0.25"}
    for d in card:
        e,f = eval(d)
        pyautogui.click(e+random.randint(10,20),f+random.randint(10,20))
        time.sleep(eval(card[d]))
    time.sleep(1)
def finishgame(): #使用pyautogui.locateOnScreen识别结束战斗结算页面，点击进入下一步
    while True:
        finish = pyautogui.locateOnScreen('D:\PycharmFeil\FGOAutoBattle\结束战斗.png')
        time.sleep(3)
        if finish != None:
            pyautogui.click(x = random.randint(100,900),y = random.randint(100,700),clicks = 3, interval = 1)
            time.sleep(1)
            break
    pyautogui.click(1792,1006)
def clickcheckpoint(): #选择上一次战斗的关卡
    while True:
        point = pyautogui.locateOnScreen('D:\PycharmFeil\FGOAutoBattle\选择关卡界面截图.png')
        time.sleep(3)
        if point != None:
            break
    pyautogui.click(1435+random.randint(20,40),309+random.randint(10,40))
    time.sleep(5)
def main():
    global whichteam1
    global whichteam2
    global whichteam3
    global starttime
    global endingtime
    if teamsetting == 0:
        whichteam1 = skillspositiononeturnone
        whichteam2 = skillspositiononeturntwo
        whichteam3 = skillspositiononeturnthree
        starttime = datetime.datetime.now()
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
        endingtime = datetime.datetime.now()
    elif teamsetting == 1:
        whichteam1 = skillspositiontwoturnone
        whichteam2 = skillspositiontwoturntwo
        whichteam3 = skillspositiontwoturnthree
        starttime = datetime.datetime.now()
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
        endingtime = datetime.datetime.now()
    elif teamsetting == 2:
        whichteam1 = skillspositionthreeturnone
        whichteam2 = skillspositionthreeturntwo
        whichteam3 = skillspositionthreeturnthree
        starttime = datetime.datetime.now()
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
        endingtime = datetime.datetime.now()
    elif teamsetting == 3:
        whichteam1 = skillspositionfourturnone
        whichteam2 = skillspositionfourturntwo
        whichteam3 = skillspositionfourturnthree
        starttime = datetime.datetime.now()
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
        endingtime = datetime.datetime.now()
    elif teamsetting == 4:
        whichteam1 = skillspositionfiveturnone
        whichteam2 = skillspositionfiveturntwo
        whichteam3 = skillspositionfiveturnthree
        starttime = datetime.datetime()
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
        endingtime = datetime.datetime()
    elif teamsetting == 5:
        whichteam1 = skillspositionsixturnone
        whichteam2 = skillspositionsixturntwo
        whichteam3 = skillspositionsixturnthree
        starttime = datetime.datetime.now()
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
        endingtime = datetime.datetime.now()
    print(endingtime-starttime)
OpenGame()
for i in range(numberofbattle):
    main()

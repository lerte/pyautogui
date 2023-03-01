import os
import time
import pyautogui
from playsound import playsound

alarm = os.path.dirname(__file__)+'/alarm.mp3'
print(alarm)

while True:
  location = pyautogui.locateOnScreen('ore.png', confidence=0.9)
  if location:
    print('发现矿石{}',location)
    pyautogui.alert(text='发现矿石', title='消息提示')
    playsound(alarm)
    time.sleep(5)
  else:
    print('没有找到，继续寻找中...')
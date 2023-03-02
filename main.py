import time
import winsound
import pyautogui

while True:
  location = pyautogui.locateOnScreen('ore.png', confidence=0.9)
  if location:
    print('发现矿石{}',location)
    # pyautogui.alert(text='发现矿石', title='消息提示')
    winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
    time.sleep(5)
  else:
    print('没有找到，继续寻找中...')
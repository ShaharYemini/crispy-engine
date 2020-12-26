from random import randint
from time import sleep

import win32api
import win32con
from selenium import webdriver

VK_CODE = {'shift': 0x10,
           'caps_lock': 0x14,
           'browser_refresh': 0xA8,
           '0': 0x30,
           '1': 0x31,
           '2': 0x32,
           '3': 0x33,
           '4': 0x34,
           '5': 0x35,
           '6': 0x36,
           '7': 0x37,
           '8': 0x38,
           '9': 0x39,
           'a': 0x41,
           'b': 0x42,
           'c': 0x43,
           'd': 0x44,
           'e': 0x45,
           'f': 0x46,
           'g': 0x47,
           'h': 0x48,
           'i': 0x49,
           'j': 0x4A,
           'k': 0x4B,
           'l': 0x4C,
           'm': 0x4D,
           'n': 0x4E,
           'o': 0x4F,
           'p': 0x50,
           'q': 0x51,
           'r': 0x52,
           's': 0x53,
           't': 0x54,
           'u': 0x55,
           'v': 0x56,
           'w': 0x57,
           'x': 0x58,
           'y': 0x59,
           'z': 0x5A,
           '+': 0xBB,
           ',': 0xBC,
           '-': 0xBD,
           '.': 0xBE,
           '/': 0xBF,
           ';': 0xBA,
           '[': 0xDB,
           '\\': 0xDC,
           ']': 0xDD,
           "'": 0xDE,
           '`': 0xC0}


def press(s):
    for let in s:
        if let == "@":
            win32api.keybd_event(VK_CODE['shift'], 0, 0, 0)
            win32api.keybd_event(VK_CODE["2"], 0, 0, 0)
            sleep(.05)
            win32api.keybd_event(VK_CODE["2"], 0, win32con.KEYEVENTF_KEYUP, 0)
            win32api.keybd_event(VK_CODE['shift'], 0, win32con.KEYEVENTF_KEYUP, 0)
            continue
        win32api.keybd_event(VK_CODE[let], 0, 0, 0)
        sleep(.05)
        win32api.keybd_event(VK_CODE[let], 0, win32con.KEYEVENTF_KEYUP, 0)


def click(x, y):
    x = int(x)
    y = int(y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def password():
    string = {let for let in "1234567890qwertyuiopasdfghjkl;zxcvbnnm" if randint(0, 3) > 2}
    pwd = "".join(list(string))
    return pwd



def duo(invention_address):
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument("--start-maximized")

    # Register the drive ------------------------------ENTER HERE YOUR PATH TO CHROME DRIVER
    chrome_browser = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    width = chrome_browser.get_window_size()["width"]
    height = chrome_browser.get_window_size()["height"]
    print(width)
    print(height)
    chrome_browser.get('https://www.minuteinbox.com/')
    fmail = chrome_browser.find_element_by_id("email")
    mail = fmail.text
    # ---------------- YOUR INVITE LINK HERE
    chrome_browser.get(invention_address)
    sleep(5)
    width_ratio = width/1936
    height_ratio = height/1056
    for j in range(10):
        click(randint(int(width_ratio*300), int(width_ratio*1600)), randint(int(height_ratio*300), int(height_ratio*700)))
    sleep(5)
    click(width_ratio*1000, height_ratio*450)
    click(width_ratio*1000, height_ratio*700)
    sleep(5)
    click(width_ratio*1500, height_ratio*180)
    sleep(5)
    click(width_ratio*1000, height_ratio*400)
    press(str(randint(20, 99)))  # age
    click(width_ratio*1000, height_ratio*490)
    press(mail)  # email
    click(width_ratio*1000, height_ratio*540)
    press(password())  # password
    click(width_ratio*1000, height_ratio*610)
    sleep(3)
    chrome_browser.close()


address = input("feed duolingo invention address:\n")
address = "https://invite.duolingo.com/BDHTZTB5CWWKTNLCRB536V33GE"
duo(address)
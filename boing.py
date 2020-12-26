import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

# Register the drive
chrome_browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe',
                                      options=options)  # Change the path as per your local dir.
chrome_browser.get('https://web.whatsapp.com/')

# Sleep to scan the QR Code
time.sleep(25)

# Select for the title having user name
#user = chrome_browser.find_element_by_xpath('//span[@title="כיתה י\'- מתמטיקה 5 יח"ל"]')
#user.click()

message_box = chrome_browser.find_elements_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')

for i in range(1000):

    # Typing message into message box
    message_box[1].send_keys('עכשיו אתה מבין על מה אני מדבר?')

    # Click on send button
    button = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    button.click()

    message_box[1].send_keys('נראה שעדיין לא.')

    # Click on send button
    button = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
    button.click()

    #time.sleep(5)

chrome_browser.close()

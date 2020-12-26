from random import randint
from selenium import webdriver
# pip install selenium

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/Desktop/new folder/driver/User Data')
# options.add_argument('--profile-directory=Default')


# Register the drive ------------------------------ENTER HERE YOUR PATH TO CHROME DRIVER 'C:/Program Files (x86)/chromedriver.exe'
chrome_browser = webdriver.Chrome(executable_path='C:/Users/USER/Desktop/new folder/driver/chromedriver.exe', options=options)
chrome_browser.get('https://web.whatsapp.com/')

# Select for the title having user name
while True:
    try:
        # Find groups chat button by its title --------------------------------------ENTER CHAT NAME
        group = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format("🦅 רייבנקלו 🦅"))
        break
    except:
        chrome_browser.implicitly_wait(1)

# lick the group chat button
group.click()

# Wait the browser to load
chrome_browser.implicitly_wait(10)
pastlist = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1RAno message-in focusable-list-item"))
past = pastlist[-2]
while True:
    #try:
        # Find the last message by the HTML ------------------------------------------ENTER MESSAGE CLASS NAME
        last = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1RAno message-in focusable-list-item"))[-1]
        # ------------------------------ENTER TEXT CLASS NAME
        txt = last.find_element_by_class_name("_1VzZY selectable-text invisible-space copyable-text")
        # If you have to detect errors:
        # print(txt.text)
        if past.text not in last.text:  # and randint(1, 5) > 4:
            # Take the message text and erase \n s
            mes = "".join(last.text.split("\n"))
            add = "אני לא חושב ש"
            # Find the message box by HTML -----------------------------------------------------ENTER MESSAGE BOX CLASS NAME HERE
            message_box = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1awRl copyable-text selectable-text"))[-1]
            # Type message into message box
            message_box.send_keys(add+mes)

            # Find send button by HTML -----------------------------------ENTER SEND BUTTON CLASS NAME HERE
            button = chrome_browser.find_element_by_xpath('//button[@class="{}"]'.format("_2Ujuu"))
            # Click on send button
            button.click()

            past = last
    #except:
     #   raise Exception
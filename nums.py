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
        group = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format("ספירה עד אינסוף עם בוטים"))
        break
    except:
        chrome_browser.implicitly_wait(1)

# lick the group chat button
group.click()

# Wait the browser to load
chrome_browser.implicitly_wait(10)

num = 0
past = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1RAno message-in focusable-list-item"))[-2]
while True:
    try:
        # Find the last message by the HTML ------------------------------------------ENTER MESSAGE CLASS NAME
        last = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1RAno message-in focusable-list-item"))[-1]
        # ------------------------------ENTER TEXT CLASS NAME
        txt = last.find_element_by_class_name("_1Oy25")
        # If you have to detect errors:
        # print(txt.text)
        # This will be true only if you are not the last to send a number.
        if past.text != last.text:
            # Take the message text
            num = txt.text
            # Clean for characters that are not numbers
            num = "".join(filter(lambda n: n in [str(x) for x in range(10)], list(num)))
            # convert the text into an integer
            num = int(num)
            # You know..
            num += 1
            # Find the message box by HTML -----------------------------------------------------ENTER MESSAGE BOX CLASS NAME HERE
            message_box = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1awRl copyable-text selectable-text"))[-1]
            # Type message into message box
            message_box.send_keys(num)

            # Find send button by HTML -----------------------------------ENTER SEND BUTTON CLASS NAME HERE
            button = chrome_browser.find_element_by_xpath('//button[@class="{}"]'.format("_2Ujuu"))
            # Click on send button
            button.click()

            past = last
    except:
        pass

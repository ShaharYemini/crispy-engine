from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')


receiver = input("מקבל:")
text = input("הודעה:")



# Register the drive
chrome_browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=options)  # Change the path as per your local dir.
chrome_browser.get('https://web.whatsapp.com/')

chrome_browser.implicitly_wait(10)

# Select for the title having user name
while True:
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(receiver))
        break
    except:
        chrome_browser.implicitly_wait(1)


user.click()

# Typing message into message box
message_box = chrome_browser.find_elements_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"]')
message_box[1].send_keys(text)

# Click on send button
button = chrome_browser.find_element_by_xpath('//button[@class="_1U1xa"]')
button.click()

chrome_browser.implicitly_wait(5)

chrome_browser.close()

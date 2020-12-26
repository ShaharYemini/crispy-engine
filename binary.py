from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument('--user-data-dir=C:/Users/USER/AppData/Local/Google/Chrome/User Data/Default')
#options.add_argument('--profile-directory=Default')

#Register the drive
chrome_browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe', options=options)  # Change the path as per your local dir.
chrome_browser.get('https://web.whatsapp.com/')

# Select for the title having user name
while True:
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format("סופרים בבינארית עד אינסוף"))
        break
    except:
        chrome_browser.implicitly_wait(1)


user.click()

# finding the last message
last = chrome_browser.find_elements_by_xpath('//div[@class="_1RAno message-in focusable-list-item"]')[-1]
txt = last.find_element_by_class_name("_1Oy25")
print(txt.text)
num = txt.text.split()

b = "0b"
for i in num:
    b += i
# print(b)
binary = int(b, 2)
# print(binary)
binary += 1
next = bin(binary)
next = str(next)
next = next[2:]
# print(next)

toType = ""
for i in range(len(next)):
    if i % 4 == 0:
        toType += " "
    toType += next[i]

while len(toType)%5 > 0:
    toType += "0"

# print(toType)
text = toType[1:]
# print(text)

# Typing message into message box
message_box = chrome_browser.find_elements_by_xpath('//div[@class="_1awRl copyable-text selectable-text"]')
message_box[-1].send_keys(text)

# Click on send button
button = chrome_browser.find_element_by_xpath('//button[@class="_2Ujuu"]')
button.click()

chrome_browser.implicitly_wait(10)

chrome_browser.close()
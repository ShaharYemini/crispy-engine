from selenium import webdriver
import pickle

special = "ניקוד"

with open("names.txt", "rb") as f:
    names = pickle.load(f)
    f.close()

print(names)

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/Desktop/new folder/driver/User Data')
options.add_argument('--profile-directory=Default')


# Register the drive
chrome_browser = webdriver.Chrome(executable_path='C:/Users/USER/Desktop/new folder/driver/chromedriver.exe', options=options)  # Change the path as per your local dir.
chrome_browser.get('https://web.whatsapp.com/')

chrome_browser.implicitly_wait(10)

# Select for the title having user name
while True:
    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format("הוגוורטס🦉"))
        break
    except:
        print(Exception)
        chrome_browser.implicitly_wait(1)


user.click()

# chrome_browser.execute_script("window.scrollBy(0, 1080)")

messages = chrome_browser.find_elements_by_xpath('//div[@class="{}"]'.format("_1RAno message-in focusable-list-item"))

# print(messages)

for mes in messages:
    if special in mes.text:
        res = mes.find_element_by_class_name("zLEDC")
        print(res.text)
        names.append(res.text)


chrome_browser.implicitly_wait(10)
print(names)

with open("names.txt", "wb") as f:
    for name in names:
        pickle.dump(name, f)

chrome_browser.close()
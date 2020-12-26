from selenium import webdriver

chrome_browser = webdriver.Chrome(executable_path='C:/Program Files (x86)/chromedriver.exe')  # Change the path as per your local dir.
chrome_browser.get('https://mail.google.com//')

chrome_browser.implicitly_wait(8)

name_box = chrome_browser.find_element_by_xpath('//div[@class="whsOnd zHQkBf"]')
name_box.send_keys("yem.shahar")
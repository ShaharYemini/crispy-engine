from selenium import webdriver
# pip install selenium

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/USER/Desktop/new folder/driver/User Data')
# options.add_argument('--profile-directory=Default')


# Register the drive ------------------------------ENTER HERE YOUR PATH TO CHROME DRIVER 'C:/Program Files (x86)/chromedriver.exe'
chrome_browser = webdriver.Chrome(executable_path='C:/Users/USER/Desktop/new folder/driver/chromedriver.exe', options=options)
chrome_browser.get('https://web.whatsapp.com/')
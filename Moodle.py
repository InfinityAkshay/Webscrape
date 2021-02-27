from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

username = input("Enter Username: ")
password = input("Enter Password: ")

path = "C:\Program Files (x86)\chromedriver.exe"
driver = wd.Chrome(path)

driver.get("https://moodle.iitd.ac.in/login/index.php")

ufield = driver.find_element_by_id("username")
ufield.send_keys(username)
pfield = driver.find_element_by_id("password")
pfield.send_keys(password)
captcha = driver.find_element_by_id("page-login-index").text.split("\n")[9].split()
cfield = driver.find_element_by_id("valuepkg3")

if "subtract" in captcha:
    captcha = str(int(captcha[-4])-int(captcha[-2]))
elif "add" in captcha:
    captcha = str(int(captcha[-4])+int(captcha[-2]))
elif "first" in captcha:
    captcha = captcha[-4]
elif "second" in captcha:
    captcha = captcha[-2]

cfield.send_keys(captcha)
cfield.send_keys(Keys.RETURN)

from selenium import webdriver as wd
from selenium.webdriver.chrome.options import Options  
import os
import shutil

chromeoptions = Options()  
chromeoptions.add_argument("--headless")
contest_num=input("Enter Contest Number: ")

dire=os.getcwd()+'\\'+contest_num
try:
    os.mkdir(dire)
except OSError:
    shutil.rmtree(dire)
    os.mkdir(dire)

path = "C:\Program Files (x86)\chromedriver.exe"
driver = wd.Chrome(path,chrome_options=chromeoptions)
j = "A"
stop = False

while not stop:
    driver.get("https://codeforces.com/problemset/problem/"+contest_num+"/"+j)
    s= lambda X: driver.execute_script("return document.body.parentNode.scroll" + X)
    driver.set_window_size(s("Width"),s("Height"))
    if j != driver.find_element_by_class_name("title").text[0]:
        stop = True
    else:
        inputs=driver.find_elements_by_class_name("input")
        outputs=driver.find_elements_by_class_name("output")
        os.mkdir(dire+"\\"+j)
        driver.find_element_by_tag_name("body").screenshot(dire+"\\"+j+"\problem.png")
        for i in range(len(inputs)):
            file = open(dire+"\\"+j+"\input"+str(i+1)+".txt","w")
            file.write(inputs[i].text[11:])
            file = open(dire+"\\"+j+"\output"+str(i+1)+".txt","w")
            file.write(outputs[i].text[12:])
        j=chr(ord(j)+1)
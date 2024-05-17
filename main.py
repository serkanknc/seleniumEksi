from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

url = "https://eksisozluk.com/13-mayis-2024-kamuda-tasarruf-tedbirleri--7822008?p="

browser = webdriver.Chrome()
browser.maximize_window()
pageCount = 1

entries = []
entryCount = 1


while pageCount<=10:
    randomPage = random.randint(1,90)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    time.sleep(0.3)

    elements = browser.find_elements(By.CLASS_NAME,"content")

    for element in elements:
        entries.append(element.text)

    pageCount +=1

with open("entries.txt","w",encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount)+ ".entry\n" + entry + "\n")
        entryCount+=1
    file.close()

browser.close()


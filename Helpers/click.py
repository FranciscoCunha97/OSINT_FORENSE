from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
service = Service(executable_path=ChromeDriverManager().install())

browser = webdriver.Chrome(service=service)
#print("Word:")
#word = input()


url = "https://www.abola.pt/Pesquisa/sporting"

#browser.get(url)

#time.sleep(2)
#button1 = browser.find_element("link text", 'Consentir')
#button1.click()
browser.get(url)

for x in range(5):

    time.sleep(2)

    button = browser.find_element("link text", 'Mais Resultados')
    button.click()

    time.sleep(3)

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #time.sleep(2)

time.sleep(10)

browser.close()
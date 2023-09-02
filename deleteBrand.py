from selenium import webdriver 
import time 
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--start-maximized")   
driver = webdriver.Edge(options=options)

driver.get("https://puppies-closet.com/evidencija/login.php")

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.CLASS_NAME, "loginbutton")
username = "deatabakovic"
password = "deatabakovic123"

username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()

mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=typeProducer']")
mainNavigation.click()

time.sleep(2)

openBr = driver.find_element(By.CLASS_NAME, "tabLabel")
openBr.click()
time.sleep(1)

enterBrand = driver.find_element(By.NAME, "equiptype")
enterBrand.click()
enterBrand.send_keys("Dell")
time.sleep(1)

saveBrand = driver.find_element(By.NAME, "saveEquipType")
saveBrand.click()
time.sleep(1)

openBrand = driver.find_element(By.CLASS_NAME, "tabLabel")
openBrand.click()
time.sleep(1)

trElementi = driver.find_elements(By.TAG_NAME, "tr")
for trElement in trElementi:
    if "Dell" in trElement.text:
        deleteBrand = trElement.find_element(By.CSS_SELECTOR, "button[class='button red']")
        deleteBrand.click()
        break
    

time.sleep(2)

deleteC = driver.find_element(By.ID, "del")
deleteC.click()

time.sleep(3)
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
time.sleep(2)

mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=equipment']")
mainNavigation.click()

wait = WebDriverWait(driver, 10)
role_dropdown = wait.until(EC.presence_of_element_located((By.ID, "type_id")))


role_dropdown = driver.find_element(By.ID, "type_id")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Mobitel")


role_dropdown = driver.find_element(By.ID, "producer_id")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Samsung")


invNum = driver.find_element(By.NAME, "inventoryNumber")
invNum.send_keys("6666")


serNum = driver.find_element(By.NAME, "serialNumber")
serNum.send_keys("64564")

sacuvaj = driver.find_element(By.NAME, "save")
sacuvaj.click()

time.sleep(3)

driver.quit()
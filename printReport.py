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

time.sleep(2)
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.CLASS_NAME, "loginbutton")
username = "deatabakovic"
password = "deatabakovic123"
time.sleep(2)
username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()
time.sleep(2)

movetoReports = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=reports']")
movetoReports.click()

time.sleep(2)
selectOffice = driver.find_element(By.ID, "org_id")
selectOffice.click()

time.sleep(2)
role_dropdown = driver.find_element(By.ID, "org_id")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Odsjek 2")

time.sleep(2)
printReport = driver.find_element(By.NAME, "orgReport")
printReport.click()

time.sleep(2)
driver.quit()
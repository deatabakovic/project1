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

mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=employees']")
mainNavigation.click()  

time.sleep(2)

ime = "samra"
prezime = "jusic"
mail = "samrajusic@gmail.com"
brojtelefona = "061999333"

firstname = driver.find_element(By.NAME, "firstname")
lastname = driver.find_element(By.NAME, "lastname")
email = driver.find_element(By.NAME, "email")
phone = driver.find_element(By.NAME, "phone")

firstname.send_keys(ime)
lastname.send_keys(prezime)
email.send_keys(mail)
phone.send_keys(brojtelefona)

time.sleep(2)

role_dropdown = driver.find_element(By.ID, "office_id")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("1009")

time.sleep(2)

role_dropdown = driver.find_element(By.ID, "organization_id")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Odsjek 8")

time.sleep(2)

sacuvaj = driver.find_element(By.NAME, "save")
sacuvaj.click()

time.sleep(2)

driver.quit()
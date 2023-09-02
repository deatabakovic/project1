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

mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=users']")
mainNavigation.click()  

time.sleep(2)

ime = 'Amra'
prezime = 'Salkic'
korisnik = 'amrasalkic'
sifra = 'amrasalkic123'

ime_korisnika = driver.find_element(By.NAME, "firstname")
prezime_korisnika = driver.find_element(By.NAME, "lastname")
korisnicko_ime = driver.find_element(By.NAME, "username")
korisnicka_lozinka = driver.find_element(By.NAME, "pass")

ime_korisnika.send_keys(ime)
prezime_korisnika.send_keys(prezime)
korisnicko_ime.send_keys(korisnik)
password.send_keys(sifra)

role_dropdown = driver.find_element(By.ID, "role")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Korisnik")

sacuvaj = driver.find_element(By.NAME, "saveUser")
sacuvaj.click()
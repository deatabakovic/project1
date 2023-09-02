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

mainNavigation = driver.find_element(By.CSS_SELECTOR, "a[href='index.php?page=users']")
mainNavigation.click()  

time.sleep(2)

ime = 'sale'
prezime = 'sakic'
korisnik = 'salesakic'
sifra = 'salesakic123'

name = driver.find_element(By.NAME, "firstname")
lastname = driver.find_element(By.NAME, "lastname")
username = driver.find_element(By.NAME, "username")
password = driver.find_element(By.NAME, "pass")

name.send_keys(ime)
lastname.send_keys(prezime)
username.send_keys(korisnik)
password.send_keys(sifra)

role_dropdown = driver.find_element(By.ID, "role")
role_select = Select(role_dropdown)
role_select.select_by_visible_text("Korisnik")

sacuvaj = driver.find_element(By.NAME, "saveUser")
sacuvaj.click()


sviElementi = driver.find_elements(By.TAG_NAME, "tr")
for element in sviElementi:
    if ime in element.text and prezime in element.text and korisnik in element.text:
        nasKorisnik = element.find_elements(By.TAG_NAME, "td")
        podaci = []
        for podatak in nasKorisnik:
            podaci.append(podatak.text)
        print(f"Korisnik {podaci[1]} {podaci[2]} je uspjesno dodat pod rednim brojem {podaci[0]} kao {podaci[4]}")

time.sleep(2)

deleteUser= element.find_element(By.CSS_SELECTOR, "button[class='button red']")
deleteUser.click()

time.sleep(2)

deleteConfirm = driver.find_element(By.ID, "del")
deleteConfirm.click()

time.sleep(2)

driver.quit()




findUser= driver.find_element(By.TAG_NAME, "tr", value= "1")
deleteUser = driver.find_element(By.ID, "del")
deleteUser.click()
deleteConfirm = driver.find_element(By.ID, "del")
deleteConfirm.click()




driver.quit()
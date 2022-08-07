from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import warnings
from threading import Thread
from time import sleep, perf_counter


def logInTest(driver):
    # Instancias del modulo de sing up
    myLogInButton = driver.find_element(By.ID, "login").click()
    time.sleep(1)
    
    # Instancias del sign up (Informacion Personal)
    myUserName = driver.find_element(By.ID, "user-login")
    myPassword = driver.find_element(By.ID, "user-password")
    btnIngresar = driver.find_element(By.ID, "ingresar")
    time.sleep(1)
    myUserName.click()
    myUserName.send_keys("admin@1.")
    time.sleep(2)
    myPassword.click()
    myPassword.send_keys('admin@1.')
    time.sleep(2)
    btnIngresar.click()
    time.sleep(2)

    
    

def rellenarForm(driver):
    myName = driver.find_element(By.ID, "appointment-name")
    myEmail = driver.find_element(By.ID, "appointment-email")
    myPhone = driver.find_element(By.ID, "appointment-tel")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    myName.click()
    myName.send_keys("Jose")
    myEmail.click()
    myEmail.send_keys("retana@gmail.com")
    myPhone.click()
    myPhone.send_keys("8")
    time.sleep(2)

    enrollMe = driver.find_element(By.ID, "enrollMe-button")
    enrollMe.click()
    time.sleep(2)

def buscarMarketplace(driver):
    driver.find_element(By.ID, "botton-marketplace").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(6)

def buscarPlataformas(driver):
    myMarketplace = driver.find_element(By.ID, "botton-marketplace").click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    



def testResponsive(driver):
    driver.set_window_size(1024, 600)
    time.sleep(4)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(4)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)

def botonCreador(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.find_element(By.ID, "link").click()
    time.sleep(6)

def botonMapa(driver):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(4)
    driver.find_element(By.ID, "mapa").click()
    time.sleep(6)




def main():
    caps = DesiredCapabilities.CHROME
    source = 'file:///C:/Users/joser/Downloads/Proyecto_Calidad-master/index.html' # URL
    PATH = 'C:\\Users\\joser\\Downloads\\Proyecto_Calidad-master\\ChromeDriver\\chromedriver.exe' # Ubicación del WebDriver
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(PATH, desired_capabilities=caps)
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    driver.get(source)


    #logInTest(driver)
    #rellenarForm(driver)
    #buscarMarketplace(driver)
    #buscarPlataformas(driver)
    #testResponsive(driver)
    #botonCreador(driver)
    #botonMapa(driver)

    driver.close()

warnings.filterwarnings("ignore")
main()
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import datetime

driver = webdriver.Chrome()
driver.get("PUT YOUR PATH OF THE HTML FILE HERE WITH C:// INSTEAD OF C:\ ")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "psInpBx")))
wait.until(EC.presence_of_element_located((By.ID, "inpBtn")))
timeOfStart = datetime.datetime.now()

for iteration in range(0, 30000):
    bzog = iteration
    val = '%04d' % bzog
    inBx = driver.find_element(By.ID, "psInpBx")
    inBx.send_keys(val)
    inBtn = driver.find_element(By.ID, "inpBtn")
    inBtn.click()
    try:
        WebDriverWait(driver, 0.2, poll_frequency=0.01).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        if alert.text == "YEAAHH!! YOU DID IT!!!!":
            print("Passcode cracked successfully")
            print('%04d' % bzog)
            totalTime = datetime.datetime.now() - timeOfStart
            print("Time to crack: " + str(totalTime))
            time.sleep(0.5)
            driver.quit()
            break
        elif alert.text == "stop, you are violating the law":
            alert.accept()
            inBx.clear()
            time.sleep(10.1)
    except TimeoutException:
        print("Timeout reached")
        inBx.clear()
        continue

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome('./chromedriver.exe')


browser.get('http://127.0.0.1:5500/index.html')

selected_element = browser.find_element(By.ID, "login-btn")
selected_element.click()

usern_element = browser.find_element(By.CLASS_NAME, "input")
usern_element.send_keys("bobby39")
time.sleep(2)

pass_element = browser.find_element(By.CLASS_NAME, "input2")
pass_element.send_keys("Dot")
time.sleep(2)

log_btn = browser.find_element(By.ID, "login-btn")
log_btn.click()
time.sleep(2)

filterup_btn = browser.find_element(By.ID, "filter-btn")
filterup_btn.click()
time.sleep(2)

filterdown_btn = browser.find_element(By.ID, "filter2-btn")
filterdown_btn.click()
time.sleep(2)

reimb_button = browser.find_element(By.ID, "Approve/Deny-btn")
reimb_button.click()
time.sleep(2)

reimbID_element = browser.find_element(By.ID, "id-input")
reimbID_element.send_keys("6")
time.sleep(2)

rating_element = browser.find_element(By.ID, "rating-input")
rating_element.send_keys("Approved")
time.sleep(2)

submit_btn = browser.find_element(By.ID, "update-btn")
submit_btn.click()
time.sleep(2)

browser.close()